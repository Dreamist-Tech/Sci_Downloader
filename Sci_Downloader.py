# -*- coding: utf-8 -*-
"""
@author: Kunyu Wang
Email: kunyuwang.real@gmail.com
"""

import tkinter as tk
from requests import get
from bs4 import BeautifulSoup

window = tk.Tk()
window.title('Dreamist-Tech')
window.geometry('480x360')

# 软件名称
label_name = tk.Label(window,
                 text = 'Sci-Downloader Beta2.0',
                 bg = 'yellow',
                 width = 50,
                 height = 2)
# 作者信息
label_footer = tk.Label(window,
                 text = 'Author: Kunyu Wang\nEmail: kunyuwang.real@gmail.com',
                 bg = 'yellow',
                 width = 50,
                 height = 2)
# 下载状态
status = tk.StringVar()
label_download_status = tk.Label(window,
                 textvariable=status,
                 bg = 'orange',
                 width = 50,
                 height = 2)
# 输入DOI
DOI = tk.Entry(window,
               width = 50,
               justify = 'center'
               )
# 显示信息
msg = tk.StringVar()
label_msg = tk.Label(window,
                     textvariable=msg,
                     width = 50,
                     height = 2,
                     bg = 'pink')

def Search_pdf():
    
    global headers
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    global url
    global filename
    
    msg.set('正在搜索,请稍等...')
    DOI_temp = DOI.get()
    
    public = 'https://www.sci-hub.'
    url_pool = ['shop','ren','si','tw','se']
    
    for each in url_pool:
        try:
            get(public+each, headers=headers, timeout=10)
            url_avaliable = public+each
            break
        except:
            msg.set('更换线路...')
    
    url = url_avaliable + '/' + DOI_temp
    res = get(url,headers=headers,stream=True)
    soup = BeautifulSoup(res.text,'html.parser')
    url = soup.find('iframe',id='pdf')['src'].split('#')[0]
    filename = soup.find('i').text.split('.')[0] + '.pdf'
    
    if url.split('//')[0] !='https:':
        url = 'https:' + url
    
    msg.set('已找到可用下载链接！请点击下载')
    
def Download_pdf(): # 调用2：获得pdf大小，分割n线程

    # proxies = {'http':'http://60.251.33.224:80',
    #                 'http':'http://112.118.205.64:80',
    #                 'http':'http://165.22.98.86:8080',
    #                 'http':'http://202.5.221.69:80',
    #                 'http':'http://202.5.221.66:80',
    #                 'http':'http://125.46.0.62:53281'}
    proxies = {}
    res = get(url, headers=headers, proxies=proxies, stream=True)
    pdf_size = int(res.headers['content-length'])
    data = 0
    with open(filename,'wb') as fp:
        for chunk in res.iter_content(chunk_size=102400):
            fp.write(chunk)
            data = data + len(chunk)
            percentage = data/pdf_size *100
            status.set('Downloading: %d %% ( %d / %d )' % (percentage, data, pdf_size))
        
    if percentage!=100:
        msg.set('失败，请重新下载...')
    else:
        msg.set('下载完成！')
        
# 搜索键
button_Search = tk.Button(window,
                   text = '搜索',
                   width = 10,
                   height = 1,
                   command = Search_pdf
                   )

# 下载键
button_Download = tk.Button(window,
                   text = '下载',
                   width = 10,
                   height = 1,
                   command = Download_pdf
                   )

label_name.pack(side='top',pady = 5)

DOI.pack(pady = 5)

button_Search.pack(pady = 5)
button_Download.pack(pady = 5)

label_msg.pack()
label_download_status.pack()
label_footer.pack(side='bottom',pady = 5)

window.mainloop()

