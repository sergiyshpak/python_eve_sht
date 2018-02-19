# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:14:38 2018

@author: g705586
"""
#%%
import requests
import time 
#%%
urls=[ 
       'https://eve-industry.org/calc/?q=Templar&techlevel=1&id=23056&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Dragonfly&techlevel=1&id=23058&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Firbolg&techlevel=1&id=23060&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Einherji&techlevel=1&id=23062&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=gram&techlevel=1&id=41385&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=satyr&techlevel=1&id=41382&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=locust&techlevel=1&id=41379&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Equite&techlevel=1&id=41376&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Shadow&techlevel=1&id=2949&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       # tyrfingg?? anyway no future  'https://eve-industry.org/calc/?q=Tyrfing&techlevel=1&id=32343&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Cyclops&techlevel=1&id=32326&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=mantis&techlevel=1&id=32345&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5'
       
       
       'https://eve-industry.org/calc/?q=Malleus&techlevel=1&id=32341&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=ametat&techlevel=1&id=41355&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Termite&techlevel=1&id=41361&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Antaeus&techlevel=1&id=41363&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Gungnir&techlevel=1&id=41365&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Cenobite&techlevel=1&id=41367&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Scarab&techlevel=1&id=41369&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Siren&techlevel=1&id=41371&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
       'https://eve-industry.org/calc/?q=Dromi&techlevel=1&id=41373&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5'
       
      ]
headers = {'user-agent': 'my-app-test/0.0.1'}

print('{0:39s}  {1:>15s} {2:>15s} {3:>15s} {4:>15s}'.format('Nazva','perItemSell','OneRunSell','zatraro','profito'))
print('-------------------')
for url in urls:
    
    r = requests.get(url, headers=headers)
    #print(r.text)
    #%%
    tab_start=r.text.find('<table class="info" id="materials2">')
    profit_start=r.text.find('<strong>Profit</strong></td>',tab_start)
    #%%
    nazva_start=profit_start+60
    nazva_end=r.text.find('</td>',nazva_start)
    nazva=r.text[nazva_start:nazva_end].strip()
    #%%
    oneitem_sell_start=r.text.find('<td class="isk">',nazva_end)+17
    oneitem_sell_end=r.text.find('ISK',oneitem_sell_start)
    oneitem_sell=r.text[oneitem_sell_start:oneitem_sell_end].strip()
    #%%
    pluso_o1=r.text.find('<span style="color:#859900">')+28
    pluso_o2=r.text.find('ISK',pluso_o1)
    pluso=r.text[pluso_o1:pluso_o2].strip()    
    
    zatraro_o1=r.text.find('<span style="color:#dc322f">')+29
    zatraro_o2=r.text.find('ISK',zatraro_o1)
    zatraro=r.text[zatraro_o1:zatraro_o2].strip()    
        
    profito_o1=r.text.find('<span style="color:#859900;">')+29        
    profito_o2=r.text.find('ISK',profito_o1)
    profito=r.text[profito_o1:profito_o2].strip()    
    #%%
    
    print('{0:39s}  {1:>15s} {2:>15s} {3:>15s} {4:>15s}'.format(nazva,oneitem_sell,pluso,zatraro,profito))
    #print (nazva+"    "+pluso+"     "+zatraro+"     "+profito)
    

"""

<table class="info" id="materials2">
..
    <tr class="catheader">
        <td colspan="5">
        <strong>Profit</strong></td>
    </tr>
    <tr>
        <td>Nitrogen Fuel Block</td>
        <td>40</td>
        <td style="text-align:right">200.00 m<sup>3</sup></td>
        <td class="isk">
            21,139.99 ISK  
            <img onclick="adjust('4051');" class="adjust" alt="adj" src="./Icon-gears.png" />
        </td>
        <td class="isk">
            <span style="color:#859900">845,599.60 ISK  </span>
        </td>
    </tr>
    <tr>
        <td colspan="3"></td>
        <td>Costs</td>
        <td  class="isk"><span style="color:#dc322f">-771,021.72 ISK  </span><td>
    </tr>
    <tr>
        <td colspan="3"></td>
        <td>Profit</td>
        <td class="isk">
            <strong>
                <span style="color:#859900;">
                    74,577.88 ISK  
                </span>
            </strong>
        </td>
    </tr>
    




Nazva                                        perItemSell      OneRunSell         zatraro         profito
-------------------
Templar I                                   3,373,003.72    3,373,003.72    2,726,683.09      646,320.63
Dragonfly I                                 2,974,999.49    2,974,999.49    2,503,162.24      471,837.25
Firbolg I                                   4,096,764.78    4,096,764.78    2,605,588.59    1,491,176.19
Einherji I                                  3,944,081.63    3,944,081.63    2,794,475.71    1,149,605.92
Gram I                                      2,989,917.44    2,989,917.44    1,781,743.82    1,208,173.62
Satyr I                                     2,589,998.98    2,589,998.98    1,812,295.28      777,703.70
Locust I                                    2,899,998.99    2,899,998.99    1,662,904.48    1,237,094.51
Equite I                                    2,744,997.69    2,744,997.69    1,956,129.16      788,868.53
Shadow                                    692,999,499.81  692,999,499.81   10,205,502.06  682,793,997.75
Cyclops I                                   9,997,999.28    9,997,999.28    8,013,947.76    1,984,051.52
Malleus I                                   9,371,362.78    9,371,362.78    8,174,351.10    1,197,011.68
Ametat I                                   10,988,798.80   10,988,798.80    9,053,820.95    1,934,977.85
Termite I                                  13,998,200.00   13,998,200.00    8,989,231.18    5,008,968.82
Antaeus I                                  12,949,789.47   12,949,789.47    8,665,333.28    4,284,456.19
Gungnir I                                  11,980,251.10   11,980,251.10    8,696,697.81    3,283,553.29
Cenobite I                                  8,431,627.26    8,431,627.26    6,349,013.87    2,082,613.39
Scarab I                                    7,434,782.61    7,434,782.61    5,821,342.56    1,613,440.05
Siren I                                     7,706,600.93    7,706,600.93    6,320,855.41    1,385,745.52
Dromi I                                     7,947,905.92    7,947,905.92    6,250,019.08    1,697,886.84
    
"""    




