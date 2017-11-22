# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:06:20 2017

@author: g705586
"""
            
#https://github.com/zKillboard/zKillboard/wiki/API-(Killmails)
# 66128944
# https://zkillboard.com/kill/66128944/    web
    
#
#https://zkillboard.com/api/kills/killID/10000002/    

#https://zkillboard.com/kill/66129358/  megatro w sobaseka na gate w jita  


import requests
import json
import time 

systemDict=  {} 

with open("mapSolarSystems.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDict[my_list[2]] = my_list[3]
        

UREL1='https://zkillboard.com/kill/'
list_to_monitor=['Jita','Perimeter','Sobaseki','Niyabainen','Tama','Kedama','Nennamaila'
    'Akidagi','Kinakka']

while 1==1:
    url = 'https://redisq.zkillboard.com/listen.php?queueID=pipetka1023'   #nena
    headers = {'user-agent': 'my-app-test/0.0.1'}
    r = requests.get(url, headers=headers)
    #print(r.text)
    if r.text!='{"package":null}':
        parsed_json = json.loads(r.text)
     #   f_hours_from_now = datetime.now() + timedelta(hours=4)
        datka=parsed_json['package']
        killid=str(datka['killID'])
        sysa=str(datka['killmail']['solar_system_id'])
        totaldeneg='${:,.2f}'.format(datka['zkb']['totalValue'])
        if systemDict.get(sysa) in list_to_monitor:
            print('totaldeneg '+totaldeneg+'  '+sysa+ '   '+systemDict.get(sysa) 
                + '  '+UREL1+killid+'/')
    time.sleep(2)