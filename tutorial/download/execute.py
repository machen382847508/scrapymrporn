#-*- coding: UTF-8 -*-
import re
import threading
from dbutil import DButils
from downloadbatch import GetFile


lock = threading.Lock()
def downloadmain():
    db = DButils()
    lock.acquire()
    nonporn = db.get_non_download()

    reg = "(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
    while not re.match(reg, nonporn.porncontent):
        print("网址格式错误")

    file1 = GetFile(nonporn.porncontent)
    filename = file1.getfilename()
    preporn = db.update_get_pre_download(nonporn.pornid)
    lock.release()
    filename = preporn.porncontent.split('/')[-1]
    file1.downfile(str(ADDRESS+filename))
    db.update_finish_download(preporn.pornid)



if __name__ == '__main__':
    ADDRESS = "E:\\Users\\tutorial\\tutorial\\movies\\"
    threadnum = 3
    # 信号量，同时只允许3个线程运行
    threading.BoundedSemaphore(threadnum)

    theads = []
    for i in range(1,4):
        t = threading.Thread(target=downloadmain,name="down"+str(i))
        theads.append(t)
        t.start()

    for thead in theads:

        thead.join()