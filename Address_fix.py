# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:53:44 2016

@author: joby
"""

"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
from xml.dom.minidom import parse, parseString

OSMFILE = "../los-angeles_california.osm"
#OSMFILE = "../example.osm"
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
           "Cir":"Circle",
           "E":"East", "E.":"East",
           "W":"West","W.":"West",
           "S":"South","S.":"South","N":"North","N.":"North",
           "Bl":'Boulevard',"Blvd":'Boulevard',
           "Dr":'Drive',
           "Hwy":'Highway'}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def audit_city_name(city_names, city_name):
    m = street_type_re.search(city_name)
    if m:
        city_type = m.group()
        if city_type not in     'Los Angeles':
            city_names[city_type].add(city_name)            


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def is_city_name(elem):
    return (elem.attrib['k'] == "addr:state")

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    city_names = defaultdict(set)    
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"): 
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                if is_city_name(tag):
                    audit_city_name(city_names,tag.attrib['v'])
                    
                    #if 'xdfe' in tag.attrib['v']:                     
                    #    #xmlstr = ET.tostring(elem, encoding='utf8', method='xml')
                    #    #pprint(prettify(ET.Element('way')))
                    #    for tag in elem.iter("tag"):                         
                    #        print tag.attrib
                            
                        
        elem.clear()            
    osm_file.close()
    print street_types
    return street_types,city_names


def update_name(name, mapping):
    lname = name.split(' ');
    lname[-1] =mapping[lname[-1].title()] # title ensures element in same form
                                          # as   
    newname = " ".join(lname)
    return newname


def test():
    st_types,city_names = audit(OSMFILE)
    #assert len(st_types) == 3
    #pprint.pprint(dict(st_types))
    pprint.pprint(city_names)    
    mkl = [x.lower() for x in mapping.keys()] # list of mapping keys in lower cs
    for st_type, ways in st_types.iteritems():
                
        for name in ways:
            print '****',name,st_type,st_type.lower()
            if (st_type in mapping) or (st_type.lower() in mkl):
                #ind = mkl.index(st_type.lower())
                #print '*********',mkl[ind].title()
                better_name = update_name(name, mapping)
                print name, "=>", better_name
#           
                
                #print name, "=>", better_name
#            if name == "West Lexington St.":
#                assert better_name == "West Lexington Street"
#            if name == "Baldwin Rd.":
#                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()    