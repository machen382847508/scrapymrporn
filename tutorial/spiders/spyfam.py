# -*- coding: utf-8 -*-
import scrapy


class SpyfamSpider(scrapy.Spider):
    name = 'mrporn'
    allowed_domains = ['www.mrporn.hk']
    start_urls = ['https://www.mrporn.hk/videos.php?duration=long&page=1']


    def parse(self, response):

        text = response.css('span.small::text').get()
        totalnum = int(text.split(' ',1)[0])/36+1

        for i in range(1,3):
            print("https://www.mrporn.hk/videos.php?duration=long&page="+str(i))
            yield response.follow("https://www.mrporn.hk/videos.php?duration=long&page="+str(i), self.parsestart)


    def parsestart(self, response):

        for vidbot in response.css('span.vidtitlebot '):
            yield {
                'pornname': vidbot.css('a::text').get(),
                'pornurl': vidbot.css('a::attr(href)').get()
            }

            #进入相关网页
            porn_page = vidbot.css('a::attr(href)').get()
            if porn_page is not None:
                porn_page = response.urljoin(porn_page)
                yield response.follow(porn_page, callback=self.spiderporn)


    #获取电影地址
    def spiderporn(self, response):
        vedio = response.css('source::attr(src)').get()
        print(vedio)

