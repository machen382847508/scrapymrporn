#-*- coding: UTF-8 -*-

import MySQLdb
from porn import Porn

class DButils():
    db = None
    _cursor = None
    def __init__(self):
        db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='x5', db='mrporn', charset='utf8')
        self._cursor = db.cursor()

    def get_non_download(self):
        sql = "SELECT PORNID,PORNNAME,PORNURL,PORNCONTENT,PORNPAGE,PORNDOWNLOAD FROM PORNS WHERE PORNDOWNLOAD = 'F' ORDER BY PORNID LIMIT 1"
        self._cursor.execute(sql)
        result = self._cursor.fetchone()
        porn = Porn(result[0],result[1],result[2],result[3],result[4],result[5])
        return porn

    def update_get_pre_download(self,pornid):
        sql = "UPDATE PORNS SET PORNDOWNLOAD = 'R' WHERE PORNDOWNLOAD = 'F' AND PORNID = "+str(pornid)
        self._cursor.execute(sql)
        sql = "SELECT PORNID,PORNNAME,PORNURL,PORNCONTENT,PORNPAGE,PORNDOWNLOAD FROM PORNS WHERE PORNDOWNLOAD = 'R' AND PORNID = "+str(pornid)
        self._cursor.execute(sql)
        result = self._cursor.fetchone()
        porn = Porn(result[0], result[1], result[2], result[3], result[4], result[5])
        return porn