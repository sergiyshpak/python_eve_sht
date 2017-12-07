# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:06:20 2017

@author: g705586
"""
            
#https://github.com/zKillboard/zKillboard/wiki/API-(Killmails)
# 66128944
# https://zkillboard.com/kill/66121569/    web
    
#
#https://zkillboard.com/api/kills/killID/66121569/    

#https://zkillboard.com/kill/66129358/  megatro w sobaseka na gate w jita  

#%%
import requests


systemDict= {} 
securDict=  {}
hisekKillsDict={}

i=0
with open("shortmap", "r") as ins:
    for line in ins:
        if i>0:    #skip first
            my_list = line.split(",")
            #print(my_list[2]+"   " +my_list[3])
            systemDict[my_list[1]] = my_list[2]
            securDict[my_list[1]] = my_list[3]
            if float(my_list[3])>0.5:
                hisekKillsDict[my_list[1]]=0
        i=i+1

           
#%%




url = 'https://api.eveonline.com/map/kills.xml.aspx'
headers = {'user-agent': 'my-app-test/0.0.1'}
r = requests.get(url, headers=headers)
#print(r.text)
    
import xml.etree.ElementTree as etree  
    
tree= etree.fromstring(r.text)
rowes=tree[1][0]

for  row in rowes:
  #  print ( row.attrib.get('solarSystemID'), row.attrib.get('factionKills') )
    if float(securDict[row.attrib.get('solarSystemID')])>0.5:
        hisekKillsDict[row.attrib.get('solarSystemID')]=int(row.attrib.get('factionKills'))
        
#%%        
from collections import OrderedDict
ohisek=OrderedDict(sorted(hisekKillsDict.items(), key=lambda t: t[1]))

import itertools
import collections

x = itertools.islice(ohisek.items(), 0, 20)

for key, value in x:
    print (systemDict[key], value)


