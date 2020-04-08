# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:11:05 2020

@author: Kunyu Wang
"""
from requests import get
def Download(url, n, start, end, fp):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    headers["Range"] = "bytes=%d-%d" % (start, end)
    res = get(url, headers=headers)
    fp.seek(start)
    fp.write(res.content)