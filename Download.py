# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:11:05 2020

@author: Kunyu Wang
"""

from requests import get

def Download(url,filename):
    attempt = 1
    while attempt<4:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
        res = get(url, headers=headers)
        pdf_size = int(res.headers['content-length'])
        data_size = 0
        with open(filename,"wb+") as fp:
            for chunk in res.iter_content(chunk_size=8096):
                fp.write(chunk)
                data_size = data_size+len(chunk)
                percentage = (data_size/pdf_size)*100
                print("\r下载进度：%d%%(%d/%d)" % (percentage, data_size ,pdf_size), end="")
        if percentage==100:
            print("\n下载成功！")
            break
        else:
            attempt = attempt + 1
            print("\n下载失败！\n第"+str(attempt)+"次尝试...")
if __name__=="__main__":
    
    url = "https://sci-hub.shop/downloads/2019-10-20/09/zhang2019.pdf"
    Download(url,"test.pdf")