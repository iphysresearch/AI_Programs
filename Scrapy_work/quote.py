# -*- coding: utf-8 -*-
import scrapy

class OuoteSpider(scrapy.Spider):
    name = 'quote'

    #初始网站
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    #解析
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):

            author = quote.xpath('.//small[@class="author"]/text()').extract_first()
            text = quote.xpath('.//span[@class="text"]/text()').extract_first()
            #返回数据
            yield{
                'author' : author,
                'text' : text
            }


        #解析下一个页面
        next_page = response.xpath('.//li[@class="next"]/@href').extract()

        if next_page  is not None:
            next_page = response.urljoin(next_page)
            #返回页面
            yield scrapy.Request(next_page, callback=self.parse)
            #

