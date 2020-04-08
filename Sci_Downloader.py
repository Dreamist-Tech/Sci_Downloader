# -*- coding: utf-8 -*-
"""
@author: Kunyu Wang
Email: kunyuwang.real@gmail.com
"""

from requests import get
from threading import Thread

from Search import Search
from Download import Download

DOI = "10.3390/s19183972"
[url,filename] = Search(DOI)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
pdf_res = get(url, headers=headers)
pdf_size = int(pdf_res.headers['content-length'])  # pdf总大小
n = 4
pdf_size_per = int(pdf_size/n)
pdf_list_start = []
pdf_list_end = []

for block in range(0, pdf_size_per*n, pdf_size_per):
    pdf_list_start.append(block)
    pdf_list_end.append(block + pdf_size_per - 1)
print(pdf_list_end)
pdf_list_end[n-1] = pdf_size

fp = open(filename, 'wb')
fp.close()
fp = open(filename, "rb+")
temp = []
for i in range(0, n):
    t = Thread(target=Download,args=(url,n,pdf_list_start[i],pdf_list_end[i],fp))
    t.setDaemon(True)
    t.start()
    temp.append(t)
for i in temp:
    i.join()
fp.close()