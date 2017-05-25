# -*- coding: utf-8 -*-
import scrapy

class QQnewsSpider(scrapy.Spider):
	name = 'qqnews'

	#初始网站
	start_urls = ['http://news.qq.com/world_index.shtml']

	#解析
	def parse(self, response):
		for url in response.xpath('//*[@id="news"]/div/div/div/div/em/a/@href'):
			full_url = response.urljoin(url.extract())
			yield scrapy.Request(full_url, self.parse_page)

	def parse_page(self, response):
		title = response.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()').extract_first()
		content = "\n".join(response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract())
		time = response.xpath('//span[@class="a_time"]/text()').extract_first()

		yield {
		'title' : title,
		'content' : content,
		'time' : time
		}

		

