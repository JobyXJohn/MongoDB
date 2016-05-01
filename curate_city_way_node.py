# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:42:22 2016

@author: joby

This script take the result of mongoDB queries in
mongo_aggregate1.py and stores them in lists node_city
and way_city. (pipeline4 and pipeline3 respectively).


"""

#node_city=  assign  result where result is obtained from pipeline4 
# see mongo_aggregate1.py: pipeline4
node_city = []
for i in range(0,len(result)):
    if result[i]['_id'] not in node_city:
        node_city.append(result[i]['_id'])

# way_city= assign to result where result is obtained from pipeline3
# see mongo_aggregate1.py: pipeline3
#This for loop is run only after pipeline3 populates 'result'
way_city =[]
for i in range(0,len(result)):
    if result[i]['_id'] not in way_city:
        way_city.append(result[i]['_id'])
##########################################

way_city_cur=[]
node_city_cur=node_city # holds all cities in LA region. 
node_lower =[x.lower() for x in node_city_cur]
node_title =[x.title() for x in node_city_cur]
for i in range(0,len(way_city)):
    city_name = way_city[i]
    splitname = city_name.split(' ')
    # Check if city belongs to nodecity or is in california at least
    if splitname[-1].lower() == 'ca' or city_name.lower() in node_lower or city_name.title() in node_title:
        node_city_cur.append(city_name)
    else:
        way_city_cur.append(city_name) # list of city names to be avoided.

from sets import Set
Way_NotLA = Set(way_city_cur).difference(Set(node_city_cur))

# Way_NotLA holds the list of cities to be avoided while processing the json file
# See Way_NotLA so obtained at the beginning of mongo_aggregate1.py
