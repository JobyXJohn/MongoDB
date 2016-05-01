# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 07:17:29 2016

@author: joby
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import numpy as np
"""

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
See the 'process_map' and 'test' functions for examples of the expected format.
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
CREATED = [ "version", "changeset", "timestamp", "user", "uid",'lon','lat','id','ref','role','type']

def key_type(element, keys,i):
   
    if element.tag == "tag":
        elestr = element.attrib['k']
        #print elestr
        if problemchars.search(elestr):
            keys["problemchars"]+=1
            #print elestr, '=>=>=>',element.attrib['v'] 
        elif lower_colon.search(elestr):
            keys["lower_colon"]+=1     
            #if 'is_in' in elestr and not 'city' in elestr :
                #print elestr, '=>=>=>',element.attrib['v']
        elif lower.search(elestr):
            keys["lower"]+=1           
        else:
            keys["other"]+=1
            #print elestr
        i+=1
    else:
        for k in element.attrib:
            if not k in CREATED:
                elestr = element.attrib[k]
            #if problemchars.search(k):
                print k,elestr
                    
         
        #if np.mod(i,2000)==0:
            #print elestr
    return keys,i


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    i=0
    for _, element in ET.iterparse(filename):
        keys,i = key_type(element, keys,i)        
        element.clear()        
    return keys



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('../los-angeles_california.osm')
    pprint.pprint(keys)
    #assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()