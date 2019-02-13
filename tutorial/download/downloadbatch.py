#-*- coding: UTF-8 -*-
from __future__ import print_function
import os
import requests
import time
import urllib


class GetFile():
    down_time = 0
    def __init__(self, url):
        self.url = url
        self.re = requests.head(url, allow_redirects=True)

    def getsize(self):
        try:
            self.file_total = int(self.re.headers['Content-Length'])
            return self.file_total
        except:
            print('无法获取下载文件大小')
            exit()

    def getfilename(self):  # 获取默认下载文件名
        filename = ''
        if 'Content-Disposition' in self.re.headers:
            n = self.re.headers.get('Content-Disposition').split('name=')[1]
            filename = urllib.parse.unquote(n, encoding='utf8')
        elif os.path.splitext(self.re.url)[1] != '':
            filename = os.path.basename(self.re.url)
        return filename

    def downfile(self, filename):  # 下载文件
        start = time.time()
        size = 0
        response = requests.get(self.url, stream=True)
        chunk_size = 1024
        content_size = self.getsize()
        if response.status_code == 200:
            print("[文件大小]:%0.2f MB" %(content_size / chunk_size /1024))
            with open(filename,"wb") as file:
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size = os.path.getsize(filename)
                    print('\r'+'[下载进度]:%s%.2f%%' %('>'*int(size * 50 / content_size ), float(size * 100 / content_size)),end=" ")

        end = time.time()
        print('\n'+'全部下载完成!用时%.2f秒'%(end-start))






