# -*- coding: utf-8 -*-
import scrapy
from ..items import TutorialItem
import threading

class SpyfamSpider(scrapy.Spider):
    name = 'mrporn'
    allowed_domains = ['www.mrporn.hk']
    start_urls = ['https://www.mrporn.hk/videos.php?duration=short&page=1']


    def parse(self, response):
        # text = response.css('span.small::text').get()
        # totalnum = int(text.split(' ',1)[0])/36+2
        for i in range(1,6):
            request = scrapy.Request("https://www.mrporn.hk/videos.php?duration=short&page="+str(i), self.parsestart)
            request.meta['pagenum'] = i
            yield request

    def parsestart(self, response):
        for vidbot in response.css('span.vidtitlebot '):

            pornname = vidbot.css('a::text').get()
            #进入相关网页
            porn_page = vidbot.css('a::attr(href)').get()
            if porn_page is not None:
                porn_page = response.urljoin(porn_page)
                request = scrapy.Request(porn_page, callback=self.spiderporn)
                request.meta['pornname'] = pornname
                request.meta['pornurl'] = porn_page
                request.meta['pagenum'] = response.meta['pagenum']
                yield request

    #获取电影地址
    def spiderporn(self, response):
        porns = TutorialItem()
        vedio = response.css('source::attr(src)').get()
        porns['pornname'] = response.meta['pornname']
        porns['pornurl'] = response.meta['pornurl']
        porns['porncontent'] = vedio
        porns['pornpage'] = response.meta['pagenum']
        yield porns