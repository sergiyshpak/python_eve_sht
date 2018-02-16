# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:14:38 2018

@author: g705586
"""
#%%
import requests
import time 
#%%
urls=['https://eve-industry.org/calc/?techlevel=1&id=4314&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?techlevel=1&id=4316&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=heliu&techlevel=1&id=4315&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=hydroge&techlevel=1&id=4316&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=discove&techlevel=1&id=32854&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=harmoni&techlevel=1&id=42885&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=optimizati&techlevel=1&id=42882&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=thrasher&techlevel=1&id=16243&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=catalys&techlevel=1&id=16241&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=drone+link&techlevel=1&id=23528&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=125mm+ga&techlevel=1&id=819&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=Auto+Target&techlevel=1&id=1208&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=equit&techlevel=1&id=41376&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=drago&techlevel=1&id=23058&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=einh&techlevel=1&id=23062&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=medium+proce&techlevel=1&id=4396&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=nuclear+x&techlevel=1&id=17673&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=scan+range&techlevel=1&id=33181&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=small+ancillary+cu&techlevel=1&id=31359&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5',
      'https://eve-industry.org/calc/?q=warp+core+s&techlevel=1&id=11613&runs=1&jobs=1&te=20&me=10&materials_modifier=1&cte=20&cme=10&c_materials_modifier=1&enc=5&dc1=5&dc2=5&decryptor=0&skill_m=0.80&implant_m=1.0&facility_m=1&solarSystem_m=Osmon&taxRate_m=10&skill_mc=0.80&implant_mc=1.0&facility_mc=1&solarSystem_mc=Osmon&taxRate_mc=10&skill_te=0.75&implant_te=1.0&facility_te=1&solarSystem_te=Osmon&taxRate_te=10&skill_me=0.75&implant_me=1.0&facility_me=1&solarSystem_me=Osmon&taxRate_me=10&skill_c=0.75&implant_c=1.0&facility_c=1&solarSystem_c=Osmon&taxRate_c=10&facility_i=1&solarSystem_i=Osmon&taxRate_i=10&advanced_industry=5'

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
    
    
"""    