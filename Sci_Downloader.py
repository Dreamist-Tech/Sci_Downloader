import requests
from bs4 import BeautifulSoup

"""
Author: Kunyu Wang
Email: kunyuwang.real@gmail.com
"""
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

public = "https://sci-hub."
url_pool = ["ren","tw","si","se"]

for each in url_pool:
    temp = requests.get(public+each,headers=headers,stream=True,timeout=10)
    if temp.status_code==200:
        url_avaliable = public+each
        break
    else:
        print("\n 没有可用链接！")
        quit()

DOI = input('Please input DOI:')

url = url_avaliable + "/" + DOI
res = requests.get(url,headers=headers,stream=True)

soup = BeautifulSoup(res.text,'html.parser')
target = soup.find("iframe",id="pdf")["src"].split("#")[0]
pdf_res = requests.get(target,headers=headers,stream=True)

filename = "test1" +".pdf"

pdf_size = int(pdf_res.headers['content-length'])  # 内容体总大小
data_size = 0

with open(filename, "wb+") as f:
    for data in pdf_res.iter_content(chunk_size=1024):
        f.write(data)
        data_size = data_size + len(data)
        percentage = (data_size / pdf_size) * 100
        print("\r 文件下载进度：%d%%(%d/%d) - %s" % (percentage, data_size, pdf_size, filename), end=" ")
if percentage == 100:
    print("\n Success!")
else:
    print("\n Failed!")