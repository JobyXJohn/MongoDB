#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}

You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB. 

Note that in this exercise we do not use the 'update street name' procedures
you worked on in the previous exercise. If you are using this code in your final
project, you are strongly encouraged to use the code from previous exercise to 
update the street names before you save them to JSON. 

In particular the following things should be done:
- you should process only 2 types of top level tags: "node" and "way"
- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings. 
- if the second level tag "k" value contains problematic characters, it should be ignored
- if the second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- if the second level tag "k" value does not start with "addr:", but contains ":", you can
  process it in a way that you feel is best. For example, you might split it into a two-level
  dictionary like with "addr:", or otherwise convert the ":" to create a valid key.
- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:

<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>

  should be turned into:

{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}

- for "way" specifically:

  <nd ref="305896090"/>
  <nd ref="1719825889"/>

should be turned into
"node_refs": ["305896090", "1719825889"]
"""
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", 
            "Square", "Lane", "Road",  "Trail", "Parkway", "Commons","Circle",
            "East","West","North","South","Terrace","Way","Plaza"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street", "St.": "Street", 
           "Ave": "Avenue", "Ave.": "Avenue", "Av":"Avenue",
           "Rd.":"Road", "Rd":"Road",
           "PKWY":"Parkway",
           "Pl":"Place","Pl.":'Place',
           "Sq.":"Square","Sq":"Square",
           "Ln.":"Lane","Ln":"Lane",
           "Tr":"Trail", "Tr.":"Trail",
           "Cir":"Circle",'Cir.':"Circle",
           "E":"East", "E.":"East",
           "W":"West","W.":"West",
           "S":"South","S.":"South","N":"North","N.":"North",
           "Bl":'Boulevard',"Blvd":'Boulevard','Blvd.':'Boulevard',
           "Dr":'Drive',
           "Hwy":'Highway'}
mkl = [x.lower() for x in mapping.keys()]

   
def update_name(name, mapping):
    lname = name.split(' ');
    #print '***', mapping[lname[-1]]
    lname = [x.title() for x in lname]
    if lname[-1] in mapping or lname[-1] in mkl:
        lname[-1]=mapping[lname[-1].title()]
        newname = " ".join(lname)
    else:
        newname = name
    return newname    


CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def get_element(osm_file,tags=('node','way','realtionship')):
    context = ET.iterparse(osm_file,events = ('start','end'))
    _,root = next(context)
    for event,elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()
    
#{"pos.0":{"$gte":33.298,"$lte":34.583},
                           #"pos.1":{"$gte":-119.437,"$lte":-116.724}}},
    
def shape_element(element):
    
    thisnode = {}
    if element.tag == "node" or element.tag == "way" :
        
        thisnode['type'] = element.tag
        pos=[] # To Hold Lat and Longitiude
        creat_dict={} 
        lat,lon=None,None # no 'pos' field if they remain none.
        
        for key in element.attrib:
            #if thisnode['type'] =='node' and element.attrib['id'] == "97424441":
                #print '*******', key
            if key in CREATED:
                creat_dict[key] = element.attrib[key]                
            elif key == 'lat':
                lat =float(element.attrib[key])
                if lat < 33.298 or lat > 34.583: # check if node in LA region
                    lat =None                    
            elif key == 'lon':
                lon = float(element.attrib[key])
                if lon < -119.437 or lon > -116.724:# check if node in LA region
                    lon = None
            elif problemchars.search(element.attrib[key]):                
                pass
            else:
                #print key,'==>>',element.attrib[key]                
                thisnode[key]=element.attrib[key]                
                    
            if lat and lon: # Update when both are populated
                thisnode['pos']=[lon,lat]
                
        thisnode['created'] = creat_dict
        
        if element.tag == 'way':
            nodel = [] # list holding node_refs
            if element.text.find("nd"):
                #print 'nd tag is present',element.find('nd').text
                for nd in element.iter("nd"):
                    if nd.get('ref'):
                        #print 'subND .....',nd.get("ref")
                        nodel.append(nd.attrib["ref"])
                    thisnode['node_refs'] =nodel    
              
        address ={}
        for stag in element:
            if stag.tag=="tag" and stag.get('k'):
                print 'TAG atrrib',stag.attrib['k']                 
                if stag.attrib['k'].startswith('addr'):
                        # Process only those with ':'
                    if stag.attrib['k'].count(':')==1:                                             
                        ind = stag.attrib['k'].find(':')+1 # Index of ':'
                        addritem = stag.attrib['k'][ind:]  # All elements following colon
                        address[addritem] = stag.attrib['v']
                        ##### CURATE the streets ###
                        if addritem == 'street':
                            address[addritem] = update_name(stag.attrib['v'],mapping)
                        #else we do nothing (i.e. if the ':' count is not 1 ) 
                            
                    # only non address tags here      
                    elif stag.attrib['k'].count(':')>1: 
                        pass
                        #print tag.attrib['v']
                        #if is_street_name(tag):
                        #    audit_street_type(street_types, tag.attrib['v'])         
        if address: # Since address can be empty {}. update only when address!
            #pprint.pprint(address)        
            thisnode['address']=address
        #print '.........................'        
        #pprint.pprint(thisnode)
            
        if 'pos' in thisnode:
            return thisnode
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in enumerate(get_element(file_in)):
            
            el = shape_element(element)
            
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
            element.clear()        
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    #data = process_map('../los-angeles_california.osm', False)
    data = process_map('../example.osm', False)
    print 'aaaaaaaaaaaaaaa'    
    pprint.pprint(data[0:25])
    
#    correct_first_elem = {
#        "id": "261114295", 
#        "visible": "true", 
#        "type": "node", 
#        "pos": [41.9730791, -87.6866303], 
#        "created": {
#            "changeset": "11129782", 
#            "user": "bbmiller", 
#            "version": "7", 
#            "uid": "451048", 
#            "timestamp": "2012-03-28T18:31:23Z"
#        }
#    }
#    assert data[0] == correct_first_elem
#    assert data[-1]["address"] == {
#                                    "street": "West Lexington Street", 
#                                    "housenumber": "1412"
#                                      }
#    assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369", 
#                                    "2199822370", "2199822284", "2199822281"]

if __name__ == "__main__":
    test()