# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:42:44 2016

@author: joby
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program counts the tags in the file.
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tag_dict={'root':1}    
    for _,element in ET.iterparse(filename):
        for child in element:
            if child.tag in tag_dict.keys():
                tag_dict[child.tag]+=1
            else:
                 tag_dict[child.tag]=1
            for nchild in child:
                if nchild.tag in tag_dict.keys():
                    tag_dict[nchild.tag]+=1
                else:
                    tag_dict[nchild.tag]=1
        element.clear()        
    return tag_dict    
        # YOUR CODE HERE


def test():

    tags = count_tags('../los-angeles_california.osm')
    pprint.pprint(tags)
      

if __name__ == "__main__":
    test()