# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:11:41 2016

@author: joby
"""

#!/usr/bin/env python
"""
"""
# A list of 'addr:city' that are not in LA region. 
# This is used in running the MongoDB queries to return only documents from 
# cities that are in the region.
# We could use this list in data_json.py to completely avoid these documents while 
# creating the json file 
Way_NotLA = [u'Meckesheim', u'Maszk\xf3w', u'Ny\xedregyh\xe1za-Fels\u0151p\xe1zsit',
             u'Giffers', u'Niederzier', u'Bad Nauheim', u'Nyon', u'Urbania', u'Willowbrook',
             u'Wildetaube', u'Waterloo', u'Montrose', u'Malabon', u'Bo\u017ca Wola'
             , u'Dundee', u'Virginia Beach', u'Exeter', u'Mannheim', u'Richland Center',
             u'Hagen', u'G\u0142ucho\u0142azy', u'Rhede', u'Oakland Park', u'Vilnius',
             u'Toluca de Lerdo', u'Stara Kamienica', u'Collins',
             u'\u041e\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u0456\u044f',
             u'San Diego', u'Bratislava', u'Paderborn', u'E\u0142k', u'Stuttgart', u'Saue',
             u'Puerto Montt', u'Kirchberg an der Murr', u'Namborn', u'Brackenheim', u'Northampton',
             u'Loffenau', u'Albersdorf', u'Lubatowa',
             u'\u0627\u0644\u0627\u0635\u0645\u0639\u064a \u0627\u0644\u062c\u062f\u064a\u062f',
             u'Flyinge', u'Chi\u0219in\u0103u', u'Raubling', u'Piechowice', u'Rybnica',
             u'Wa\u0142brzych', u'Aichtal', u'L\xf8gst\xf8r', u'\u8c4a\u5ddd\u5e02',
             u'Montigny-le-Bretonneux', u'Acharting', u'\u0411\u0435\u0440\u0434\u0438\u0447\u0456\u0432',
             u'Aschheim', u'Rywa\u0142d', u'Westchester', u'Yerevan', u'Antwerpen',
             u'Bowling Green', u'Hayle', u'19455', u'Birmingham', u'Bayreuth',
             u'\u0535\u0580\u0587\u0561\u0576', u'Wien', u'Bradenton', u'Tuscaloosa',
             u'M\xfchlenbarbekl', u'Dresden', u'Paderne', u'Lublin', u'Dabel', u'Gloggnitz',
             u'\u041a\u0438\u0440\u043e\u0432', u'Frankfurt am Main', u'Saskatoon',
             u'Wendlingen am Neckar', u'Rennes', u'Heimbach', u'Mill Creek',
             u'\u0141\xf3d\u017a', u'\u9ad8\u96c4\u5e02', u'Imielin', u'Weimar (Lahn)',
 u'\u0427\u0430\u0439\u043a\u043e\u0432\u0441\u043a\u0438\u0439', u'Stolberg (Rhld.)',
 u'Szklarska Por\u0119ba', u'\u06a9\u0627\u0634\u0627\u0646', u'Delmenhorst',
 u'Annweiler am Trifels', u'Jelenia G\xf3ra', u'Marietta', u'Hamburg', u'Leesburg',
 u'Winterthur', u'Binche', u'Norfolk', u'\u0411\u0430\u044f\u043d\u043e\u0432\u043a\u0430',
 u'Bad Hersfeld', u'McCall Park', u'Nu\xdfdorf am Haunsberg', u'Germering', u'Tainach', 
 u'Hartlepool', u'Bethesda',  u'Heusden', u'Mogersdorf', u'Vigneux-sur-Seine', u'Ebermergen',
 u'Neus\xe4\xdf', u'Augsburg', u'Schwarzenfeld', u'Heist-op-den-Berg', u'Pfaffenhofen an der Ilm',
 u'Kromn\xf3w', u'Naters', u'St. Charles', u'Findlay', u'Ingbirchworth', u'Plankstadt',
 u'Kirchberg an der Raab', u'Buffalo', u'\u041a\u0438\u0457\u0432', u'Scheiditz', u'Battle Ground',
 u'aschheim', u'Cardigan', u'Belfast', u'Accrington', u'Gevelsberg', u'Oderberg', u'Gachenbach',
 u'Fram', u'Rutesheim', u'\u039a\u03b1\u03bb\u03bb\u03b9\u03b8\u03ad\u03b1',
 u'Mountain Center', u'Boscoreale', u'Pfaffenhofen', u'Schlieben', u'Bolton', 
 u'Dinan Bashnoian Wala', u'\u010cren\u0161ovci', u'Stutensee', u'M\xfclheim an der Ruhr',
 u'Rheinhausen', u'Stevens Point', u'August\xf3w', u'Ra\u010de', u'T\xfcttleben', u'Gera',
 u'Kottmar', u'\u0422\u0438\u0440\u0430\u0441\u043f\u043e\u043b\u044c',
 u'\u0421\u041e\u041a "\u0411\u041e\u041b\u042c\u0428\u0410\u042f \u0413\u0423\u0422\u0410"', 
 u'B\xfcrgel', u'Iwonicz-Zdr\xf3j', u'Waubaushene', u'Legnica', u'Sch\xf6mberg', 
 u'Podplat', u'Zwickau', u'Amherstburg', u'Quakenbr\xfcck',
 u'\u0421\u0442\u0443\u043f\u0438\u043d\u043e', u'Dorsten', u'Lafayette',
 u'Sun City', u'Encinitas', u'Grosbous', u'Stokke', u'Sandefjord', u'Regau', u'Kouvola',
 u'Aurich', u'Uniej\xf3w', u'Fa\xdfberg', u'Au\xdferbraz', u'Lipowica', u'Feistritztal', 
 u'Pirot', u'Schwendt', u'Saginaw', u'Romanshorn', u'Rimforest', u'Lexington', u'Felbridge',
 u'Hessle', u'Miejsce Piastowe', u'Doetinchem', u'Mount Laurel', u'Pozna\u0144', u'Manchester',
 u'Kassel',  u'\u041b\u0456\u0442\u043a\u0438', u'S\xe3o Paulo',
 u'\u041a\u043e\u0441\u0442\u0440\u043e\u043c\u0430', u'Rochester', u'Adelanto',
 u'\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433',
 u'\u041a\u0430\u0440\u0430\u0433\u0430\u043d\u0434\u0430', u'MIlwaukee', 
 u'Brzezia \u0141\u0105ka', u'Oregon', u'Berlin', u'F\xfcrth', u'Meckenheim',
 u'\u062a\u0628\u0631\u06cc\u0632', u'Kathmandu', u'Ascoli Satriano', u'Eskoriatza',
 u'Moormerland', u'Bretignolles-sur-Mer', u'Ansbach', u'Aldersey', u'Gillingham',
 u'San Lucas Sacatep\xe9quez', u'Waldeck', u'Schaafheim', u'Weyhe', u'Colombare di Sirmione',
 u'Ochsenhausen', u'Oberderdingen', u'Kayseri', u'Saugus', u'Gorlice', u'Fier',
 u'Arrowbear', u'Arnsberg', u'Imielin---', u'Elmshorn', u'Burton Joyce', u'Kra\u015bnik',
 u'\u0421\u043d\u0435\u0433\u0438\u0440\u0438', u'\u0411\u0435\u043e\u0433\u0440\u0430\u0434',
 u'Lw\xf3wek \u015al\u0105ski', u'\u4e0a\u6d77', u'Shanghai', u'Arrowbear Lake', u'Athens', 
 u'Ostelsheim', u'Noville', u'Koksijde', u'Heidelberg', u'Esvres', u'Villa Nueva', u'Ronse', 
 u'Bamberg', u'East Highland', u'Budapest', u'\u041c\u043e\u0441\u043a\u0432\u0430',
 u'Loxahatchee', u'Bydgoszcz', u'Obermaiselstein', u'sambakouni', u'Bristow', 
 u'Riedstadt-Crumstadt', u'Orchard Hills',
 u'\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a', u'Gig Harbor',
 u'Reno', u'Council Bluffs', u'Milwaukee', u'Portland', u'\u81fa\u5317\u5e02',
 u'Sugar Loaf', u'\u5b89\u5fbd\u7701\u94dc\u9675\u5e02\u679e\u9633\u53bf', u'Guasti', 
 u'Hamminkeln', u'D\xfcsseldorf', u'Pfreimd', u'J\xe4ms\xe4', u'Taucha', u'Bloomington',
 u'D\xe4nikon', u'Castel San Pietro', u'\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c',
 u'Ny\xedregyh\xe1za', u'Kirkcaldy', u'\u0417\u0435\u043c\u0443\u043d', u'Ljubljana Zalog',
 u'W\xf6llstadt', u'Meiningen', u'Kampala', u'Torre Annunziata', u'Kaufbeuren', u'Ipor\xe3',
 u'Denpasar', u'Schwabach', u'Cucamonga', u'Belmont', u'Quilpu\xe9', u'G\xf6ttingen', u'Lemon',
 u'Bajamar', u'Grasberg', u'Millom', 
 u'\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433',
 u'Vi\u0161nja Gora', u'Edinburgh', u'Quito', u'\u041b\u043e\u0433\u043e\u0439\u0441\u043a',
 u'Passail', u'Marchtrenk', u'F\xfcrstenau',
 u'\u041a\u0430\u0432\u0430\u043b\u0435\u0440\u043e\u0432\u043e', u'Katowice', u'Neerpelt',
 u'T\xf8nsberg', u'\u041a\u043e\u0441\u0442\u043e\u043f\u0456\u043b\u044c', u'Winnenden',
 u'Finnentrop', u'Mentone', u'Kiesenhof', u'\u0427\u0435\u0440\u0451\u043c\u0443\u0445\u043e\u0432\u043e',
 u'Beacon Hill', u'saugus', u'Cz\u0119stochowa', u'Charzykowy', u'Wojcieszyce',
 u'Valley Glen', u'Backnang', u'Essen', u'Ke\xe7i\xf6ren/Ankara', u'Chemnitz',
 u'Villa Canales', u'Mazatenango', u'Mission Hills', u'Sorrowful Maiden Summer Camp', 
 u'\u58ef\u570d\u9109', u'L\xfcchow',
 u'\u041c\u0430\u043b\u044b\u0435 \u042f\u043d\u0443\u0448\u043a\u043e\u0432\u0438\u0447\u0438',
 u'Bad D\xfcrkheim', u'\u0423\u043b\u044c\u044f\u043d\u043e\u0432\u0441\u043a',
 u'\u0420\u0443\u0441\u0442\u0430\u0439', u'Glen Avon', u'Leoben', u'Baltimore',
 u'Winterberg', u'Macclesfield', u'Aschau am Inn', u'Lindow', u'Lohr a. Main', u'Steinhagen',
 u'Cherry Valley', u'Erlau', u'Preston', u'Nassereith', u'Lake View Terrace',
 u'Blankenheim', u'Besko', u'Goch', u'Wesseling', u'Citrus Heights',
 u'\u041f\u043b\u044e\u0441\u0441\u0430', u'Dinkelsb\xfchl', u'Omaha', u'M\xfcnster',
 u'\u0423\u0436\u0433\u043e\u0440\u043e\u0434', u'Bad Oeynhausen', u'Plymouth', u'Sherbrooke',
 u'\u0141\u0119\u017cany', u'New Haven', u'Yeadon', u'Leipzig',
 u'\u0427\u0443\u0441\u043e\u0432\u043e\u0439', u'Speyer', u'La Mesa', u'Vanyarc', u'Girardot']

######################################
#PIPELINES USED TO QUERY THE COLLECTION
######################################
pipeline1 = [{"$match":{"address.city":{"$exists":True}}},
            {"$group":{'_id':'$address.city',"count":{"$sum":1}}},
            {"$group":{'_id':None,"count":{"$sum":1}}}] # List all the cities
            
pipeline2 = [{"$match":{"address.city":{"$exists":True},"type":"node"}},
            {"$group":{'_id':'$address.city',"count":{"$sum":1}}},
            {"$group":{'_id':None,"count":{"$sum":1}}}] # cities in nodes /excluding ways            
            
pipeline3 = [{"$match":{"address.city":{"$exists":True}}},
            {"$group":{'_id':'$address.city',"count":{"$sum":1}}},
            {"$sort":{'count':-1}}] # sort cities with max entries
            
pipeline4 = [{"$match":{"address.city":{"$exists":True},"type":"node"}},
            {"$group":{'_id':'$address.city',"count":{"$sum":1}}},
            {"$sort":{'count':-1}}] # sort cities with max entries/ Exclude "ways"
            
pipeline5 = [{"$match":{"address.city":{"$exists":True,'$nin':Way_NotLA}}},
            {"$group":{'_id':'$address.city',"count":{"$sum":1}}},
            {"$sort":{'count':-1}}] #Both Node and Way but excluding non-LA cities           
            
pipeline6 = [{"$match":{"address.postcode":{"$exists":True}}},
            {"$group":{'_id':'$address.postcode',"count":{"$sum":1}}},
            {"$sort":{'count':-1}},
            {"$limit":10}] # sort postal codes with max entirs
                                         
     
pipeline7 = [{"$match":{"address.postcode":{"$exists":True},"address.city":{"$exists":True,'$nin':Way_NotLA}}},
            {"$group":{'_id':'$address.city',"postal_code":{'$addToSet':'$address.postcode'}}},
            {'$unwind':"$postal_code"},
            {'$group':{"_id":'$_id','count':{'$sum':1}}},            
            {'$sort':{'count':-1}},
            {"$limit":10}            
            ] # count number of uniques postal codes for a given city.                        
    
            
pipeline8 = [{"$group":{'_id':'$created.user','count':{'$sum':1}}},
            {'$sort':{'count':-1}}
            #,            {"$limit":10}            
            ] # The USER with most entries

pipeline9 = [{'$match':{"address.city":{'$exists':True,'$nin':Way_NotLA}}},
            {"$group":{'_id':'$created.user',"city_name":{'$addToSet':'$address.city'}}},
            {'$unwind':'$city_name'},
            {'$group':{'_id':'$_id','count':{'$sum':1}}},
            {'$sort':{'count':-1}},
            {"$limit":50}            
            ]  # Which USER has contributed to most cities.  
            
pipeline10 = [{'$match':{"address.postcode":{'$exists':True}}},
            {"$group":{'_id':'$created.user',"postal_code":{'$addToSet':'$address.postcode'}}},
            {'$unwind':'$postal_code'},
            {'$group':{'_id':'$_id','count':{'$sum':1}}},
            {'$sort':{'count':-1}},
            {"$limit":90}            
            ]  # Which USER has most postal code contributions.          
            
pipeline11 = [{'$match':{"address.city":{'$nin':Way_NotLA},
            "amenity":{'$exists':True,'$in':['restaurant','Restaurant']}}},
             {'$project':{'_id':'$_id',"amenity":"$amenity",'name':'$name','pos':'$pos'}}]
            #Get all restaurants. Turns out there are 3131 in the datafile.
             

pipeline12 = [{'$match':{"amenity":{'$exists':True,
                              '$in':['restaurant','Restaurant']},"address.city":{'$nin':Way_NotLA}}}]
# Return entire documents with resaturants. 
           
# Staple's CEnter = 34.04302 	-118.26684
pipeline13 =   [{'$geoNear':{'near':[ -118.26684, 34.04302 ],'spherical':True,
'maxDistance':10/3963.2,
'distanceField':'distance','includeLocs':'pos','distanceMultiplier':3963.2,
    'spherical':True,'limit':100,'query':pipeline12}}]
# The above does not restrict to only documents with 'amenities':'restaurant' 
# despite the 'query':pipeline
    
pipeline14 = [{'$geoNear':{'near':[ -118.26684, 34.04302 ],
                           'spherical':True,'maxDistance':10/3963.2,
                          'distanceField':'distance','includeLocs':'pos',
                          'distanceMultiplier':3963.2,'limit':50000}},                              
                              {'$match':{"amenity":{'$exists':True,
                              '$in':['restaurant','Restaurant']}}},
                           {'$project':{'_id':'$_id',"amenity":"$amenity",
                           'name':'$name','dist':"$distance",'pos':'$pos'}}]
# IN the above pipeline "query": has been replaces by another pipeline query                           



# How about pipeline13 with db.command(). See end of the script.

                 
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    db.losangeles1.create_index([('pos','2dsphere')]) 
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = pipeline2
    return pipeline

def city_names(db, pipeline):
    return [doc for doc in db.losangeles1.aggregate(pipeline)]
    #return [doc for doc in result.aggregate(pipeline)]

if __name__ == '__main__':
    db = get_db('cities')
    pipeline = make_pipeline()
    from pymongo import GEO2D
    db.losangeles1.create_index([('pos','2dsphere')])     
    #result = city_names(db, pipeline8)
    result = city_names(db, pipeline4)
    import pprint
    pprint.pprint(result)
# The following should be uncommmented to see restaurants within 1000 ft of Staple's Center.
# This command does not have the downsides of pipleline13 and 14 
# to generate the restaurant list. 
    
    #Staples_Restaurant =db.command('geoNear','losangeles1',
    #              near={'type':'Point',
    #                    'coordinates':[-118.26684, 34.04302]},
    #             spherical=True,
    #             maxDistance=330,
    #             distanceField='distance',
    #            includeLocs='pos',
    #             query={"amenity":{'$in':['restaurant']},"name":{'$regex':['.soupl.']}})
