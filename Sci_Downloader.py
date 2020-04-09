# -*- coding: utf-8 -*-
"""
@author: Kunyu Wang
Email: kunyuwang.real@gmail.com
"""

from Search import Search
from Download import Download

DOI = input("请输入文章DOI：")
[url,filename] = Search(DOI)
Download(url,filename)