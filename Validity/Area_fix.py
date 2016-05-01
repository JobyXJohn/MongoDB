# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:10:41 2016

@author: joby
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

def findtype(entry):
    if entry==None or entry=="" or entry =='NULL':
        fdtype = type(None)
    elif entry[0]=="{":
        fdtype = type(list())
    elif is_float(entry):
        if isnot_int(entry):
            fdtype = type(float())
        else:
            fdtype = type(int())
    else:
        fdtype = type(str())
    #print fdtype    
    return fdtype    
def isnot_int(value):
  try:
    int(value)
    return False
  except:
    return True

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def fix_area(area):
    areatype = findtype(area)
    if area==None or area=="" or area =='NULL':
        area = None
    elif area[0] == '{':
        areas = area[1:-1].split('|')
        lar = []
        for ars in areas:
            lar.append(len(ars.split('.')[1]))
        area = float(areas[lar.index(max(lar))])
    elif is_float(area):
        if isnot_int(area):
            area = float(area)
        else:
            area = int(area)
    else:
        area = str(area)   
        #print area
    # YOUR CODE HERE
    return area

def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                #print line["areaLand"]
                line["areaLand"] = fix_area(line["areaLand"])
                #print 'Fixed Value:',line["areaLand"]
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])
        
    assert data[3]["areaLand"] == None        
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()