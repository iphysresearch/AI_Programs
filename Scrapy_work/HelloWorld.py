# -*- coding: utf-8 -*-
import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    #初始网站
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for question in response.xpath('//div[@class="question-summary"]'):

            title = question.xpath('.//div[@class="summary"]/h3/a/text()').extract()
#            link = response.urljoin(question.xpath('.//div[@class="summary"]/h3/a/@href').extract())  #还不明白错在哪里
            votes = question.xpath('.//div[@class="votes"]/span/strong/text()').extract()
            answers = question.xpath('.//div[@class="status answered-accepted"]/strong/text()').extract()

            yield{
                'title':title,
#                'link':link,
                'votes':votes,
                'answers':answers
            }

