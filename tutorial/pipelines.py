# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class TutorialPipeline(object):

    def __init__(self):
        dbargs = dict(
            host = '127.0.0.1',
            db='mrporn',
            user='root',
            passwd='x5',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)



    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item

    def insert_into_table(self,conn,item):
        conn.execute("INSERT INTO PORNS(PORNNAME,PORNURL,PORNCONTENT,PORNPAGE) VALUES (%s,%s,%s,%s)"
                     ,(item['pornname'],item['pornurl'],item['porncontent'],int(item['pornpage'])))