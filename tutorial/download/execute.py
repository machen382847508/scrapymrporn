#-*- coding: UTF-8 -*-
import re
import threading
from dbutil import DButils
from downloadbatch import GetFile

if __name__ == '__main__':
    ADDRESS = "E:\\Users\\tutorial\\tutorial\\movies\\"
    db = DButils()
    nonporn = db.get_non_download()
    reg = "(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
    while not re.match(reg, nonporn.porncontent):
        print("网址格式错误")

    file1 = GetFile(nonporn.porncontent)
    file_total = file1.getsize()
    filename = file1.getfilename()
    print ("下载的文件为：" + str('%.2f' % (file_total / 1024 / 1024)) + "MB")
    print ("开始下载文件:" + str(filename))
    preporn = db.update_get_pre_download(nonporn.pornid)
    t1 = threading.Thread(target=file1.downfile, args=(str(ADDRESS+filename),))
    t1.start()



