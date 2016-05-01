# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:46:42 2016

@author: joby
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
   
    for _, element in ET.iterparse(filename):
       if 'user' in element.attrib:
            uname = element.attrib['uid']
            users.update([uname])
       element.clear()     
    return users


def test():

    users = process_map('../los-angeles_california.osm')
    pprint.pprint(users)
    #assert len(users) == 6
    print 'Number of Unique Users: ',len(users)
    return users


users = test()
    