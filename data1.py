# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:02:14 2021

@author: Mansi Gaikwad
"""

import requests
from bs4 import BeautifulSoup



data1=requests.get("https://doctor.ndtv.com/diseases/multiple-sclerosis")
soup=BeautifulSoup(data1.content,"html.parser")

def ms():
    about_ms=soup.find('div',class_='box-line noBtmBrdr').text
    
    cause=soup.find('div',id='whatarethecauses',class_='box-line').text
    
    sym=soup.find('div',id='symptoms',class_='box-line').text
    
    diag=soup.find('div',id='diagnosis',class_='box-line').text
    
    treat=soup.find('div',id='treatment',class_='box-line').text
    
    mydata=[about_ms,cause,sym,diag,treat]
    return mydata

data2=requests.get("https://doctor.ndtv.com/diseases/anxiety")
soup1=BeautifulSoup(data2.content,"html.parser")

def anx():
    about_anx=soup1.find('div',id='whatisit',class_='box-line noBtmBrdr').text
                        
    cause=soup1.find('div',id='whatarethecauses',class_='box-line').text
                                
    symp=soup1.find('div',id='symptoms',class_='box-line').text
                                
    diag=soup1.find('div',id='diagnosis',class_='box-line').text
                                
    treat=soup1.find('div',id='treatment',class_='box-line').text
                                
    anxietydata=[about_anx,cause,symp,diag,treat]
    return anxietydata
                        



