# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin

class GakuSpider(scrapy.Spider):
    name = 'gaku'
    allowed_domains = ['gakuman-tokyo.com']
    start_urls = ['https://www.gakuman-tokyo.com/tokyo/line/']

    def parse(self, response):
        
        urls = response.xpath("//*[@class='d-flex justify-content-between align-items-center flex-nowrap']/a/@href").getall()
        for url in urls:
            link = urljoin("https://www.gakuman-tokyo.com/tokyo/line/",url)
            yield response.follow(url=link, callback=self.parse_page, meta={'link': link})

    def parse_page(self, response):
        link = response.request.meta['link']
        bldg_page = response.xpath('*//h4/a/@href').getall()    
        bldg_name = response.xpath('*//h4/a/text()').getall()
        bldg_price = response.xpath('//*[@id="resultList"]/article/div[2]/table/tbody/tr[1]/td/text())').getall()
