# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:11:05 2020

@author: Kunyu Wang
"""

from requests import get
from threading import Thread

class Downloader(object):
    
    def __init__(self,url,filename,n):
        self.url = url
        self.filename = filename
        self.n = n
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
        # self.proxies = {'http':'http://60.251.33.224:80',
        #                 'http':'http://112.118.205.64:80',
        #                 'http':'http://165.22.98.86:8080',
        #                 'http':'http://202.5.221.69:80',
        #                 'http':'http://202.5.221.66:80',
        #                 'http':'http://125.46.0.62:53281'}
        self.proxies = {}
    
    def get_pdfinfo(self): # 调用1：获得pdf大小，分割n线程
        res = get(self.url, headers=self.headers, proxies=self.proxies)
        self.pdf_size = int(res.headers['content-length'])
        pdf_persize = int(self.pdf_size/self.n)
        start = []
        end = []
        for i in range(0,self.n):
            start.append(i*pdf_persize)
            end.append((i+1)*pdf_persize-1)
        end[self.n-1] = self.pdf_size
        return [start,end]
        
    def Download_interval(self,start,end,fp): # 调用2：分线程下载
        attempt = 1
        while attempt < 4:
            res = get(self.url, headers={'Range':'bytes=%d-%d' % (start,end)}, proxies=self.proxies, stream=True)
            data = 0
            for chunk in res.iter_content(chunk_size=102400):
                fp.write(chunk)
                data = data + len(chunk)
                percentage = data/self.pdf_size *100
                print('\r[%s] Downloading: %d %% ( %d / %d )' % (self.filename, percentage, data, self.pdf_size),end = '')
            
            if len(res.content)<(end-start):
                attempt = attempt + 1
                print('重试...')
            else:
                print('下载完成！')
                break

    def Download(self): # 运行1
        temp = []
        [start,end] = self.get_pdfinfo()
        fp = open(self.filename,'wb')
        for j in range(0,self.n):
            th = Thread(target = self.Download_interval,args=(start[j],end[j],fp,))
            th.setDaemon(True)
            th.start()
            temp.append(th)   
        for j in temp:
            j.join()
        fp.close()
        
if __name__ == '__main__':
    url = 'http://www.sci-hub.ren/downloads/2019-10-20/09/zhang2019.pdf'
    d = Downloader(url,'test.pdf',1)
    d.Download()