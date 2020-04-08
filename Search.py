# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:05:18 2020

@author: Kunyu Wang
"""

from requests import get
from bs4 import BeautifulSoup

def Search(DOI):
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    public = "https://sci-hub."
    url_pool = ["ren"]
    
    for each in url_pool:
        try:
            get(public+each,headers=headers,stream=True)
            url_avaliable = public+each
            break
        except:
            print("\n 更换线路...")
    
    url = url_avaliable + "/" + DOI
    res = get(url,headers=headers,stream=True)
    soup = BeautifulSoup(res.text,'html.parser')
    target = soup.find("iframe",id="pdf")["src"].split("#")[0]
    filename = soup.find("i").text.split(".")[0] + ".pdf"
    
    if target.split("//")[0] !="https:":
        target = "https:"+target
    return [target,filename]

if __name__=="__main__":
    [url,filename]=Search("10.3390/s19183972")