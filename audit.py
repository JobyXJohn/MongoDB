# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:48:42 2016

@author: joby
"""
# We find 1590 unique street types
#OBviously this is wrong and looking at the result reveals that this is because
# most of them are numbers or street names without the street type. 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
from collections import defaultdict
import re

#osm_file = open("../los-angeles_california.osm", "r")
osm_file = open("../los-angeles_california.osm", "r")

street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
street_types = defaultdict(int)
city_names = defaultdict(int)

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()

        street_types[street_type] += 1
        
def audit_city_name(city_names, this_city):
    #collect unique city names
    if this_city in city_names:
        city_names[this_city] +=1
        #print '&&&&&&&', this_city        
    else:
        city_names[this_city]=1
        

def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v) 

def is_street_name(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")

def is_city_name(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:city")    

def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v'])   
        if is_city_name(elem):
            #print elem.attrib['v']
            audit_city_name(city_names, elem.attrib['v'])
        elem.clear()    
    print_sorted_dict(street_types)
        
    print 'Total Cities', len(city_names) 

   

if __name__ == '__main__':
    audit()
    sum=0
    