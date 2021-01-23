#############################################################################
# Author: dlett-projects @github.com                                        #
# Date: 1/14/2021                                                           #
# Purpose: Crawler designed to scrape OEM websites for MSRP,MPG,HP,Torque   #
#############################################################################

import scrapy

class AutomotiveSpider(scrapy.Spider):
    name = "spider1"
    start_urls = [
            'https://www.toyota.com/camry/',
            # 'https://automobiles.honda.com/accord-sedan',
            # 'https://www.mazdausa.com/shopping-tools/build-and-price=',
            # 'https://www.ford.com/cars/fusion/',
            # 'https://',
            # 'https://',
            # 'https://',
    ]

    def parse(self, response):
        for response in response.xpath('//div[@class="mlp-welcome-content.content"]'):
            yield {
                'VehicleID': response.xpath('//head/title//text()').extract(),
                'msrp': response.xpath('.//div[@class="mlp-welcome-content content"]/div[2]/div/strong').extract(),
                'mpg': response.xpath('.//div[@class="mlp-welcome-content content"]/div[2]/div[2]/strong').extract(),
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page is not None:
            next_page_join = response.urljoin(next_page)
            yield scrapy.Request(next_page_join, callback=self.parse)
    #Terminal Commands: scrapy crawl spider1 -o spider1.json

    #This block will create a local html page of the scraped url
    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'spider1-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
    #Terminal Commands: scrapy crawl spider1



