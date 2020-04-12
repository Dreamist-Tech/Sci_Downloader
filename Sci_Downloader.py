# -*- coding: utf-8 -*-
"""
@author: Kunyu Wang
Email: kunyuwang.real@gmail.com
"""

from Search import Search
from Download import Downloader

DOI = input("请输入文章DOI：")
n = 1 # 并行下载，目前不好用
[url,filename] = Search(DOI)
pdf = Downloader(url,filename,n)
pdf.Download()