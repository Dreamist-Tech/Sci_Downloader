# -*- coding: utf-8 -*-
"""
@author: Kunyu Wang
Email: kunyuwang.real@gmail.com
"""

from Search import *
from Download import *

DOI = input("请输入文章DOI：")
n = 1 # 并行下载，目前不好用
[url,filename] = Search(DOI)
pdf = Downloader(url,filename,n)
pdf.Download()