# -*- coding: utf-8 -*-
import scrapy

class CnblogSpider(scrapy.Spider):
    name = 'cnblogs'
    #限定域名
    allowed_domains = ["cnblogs.com"]
    #初始网站
    start_urls = ['http://www.cnblogs.com/pick/#p%s' %p for p in range(1,21) ]

    def parse(self, response):
        for article in response.xpath('//div[@class="post_item"]'):
#            title = article.xpath('.//div[@class="post_item_body"]/h3/a/text()').extract_first().strip()
            
            title = article.xpath('.//a[@class="titlelnk"]/text()').extract_first().strip()
            link =  response.urljoin(article.xpath('.//div[@class="post_item_body"]/h3/a/@href').extract_first().strip())
            #link =  article.xpath('.//div[@class="post_item_body"]/h3/a/@href').extract_first().strip()
#            summary = article.xpath('.//div[@class="post_item_body"]/p[@class="post_item_summary"]/text()').extract()
            summary = article.xpath('.//p[@class="post_item_summary"]/text()').extract()
            author = article.xpath('.//div[@class="post_item_foot"]/a/text()').extract_first()
            author_url = article.xpath('.//div[@class="post_item_foot"]/a/@href').extract_first()
            comment = article.xpath('.//span[@class="article_comment"]/a/text()').extract()

            yield{
                'title':title,
                'link':link,
                'summary':summary,
                'author':author,
                'author_url':author_url,
                'comment':comment
            }

            

