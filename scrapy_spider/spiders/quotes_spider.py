# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import QuoteItem

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for q in quotes:
            item = QuoteItem()

            item["quote"] = q.xpath(".//span[@class='text']/text()").extract_first()
            item["author"] = q.xpath(".//small//text()").extract_first()

            yield item
        
        next_page_url = response.xpath("//li[@class='next']//a/@href").extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)

            
