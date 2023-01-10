# an example scrapy project to upload to zyte

import scrapy

# initialize the spider class for cost of living rank by country
class ExpatistanSpider(scrapy.Spider):
    name = 'expatistan'
    allowed_domains = ['expatistan.com']
    start_urls = ["https://expatistan.com/cost-of-living/country/ranking"]

    def parse(self, response):
        # select the table of cost of living rank by country
        table = response.xpath('//*[@id="content"]/div/div[1]/div[1]/table')
        rows = table.xpath('//tr')
        
        countries = rows.xpath('td[2]//text()').extract()
        indexes = [int(item) for item in rows.xpath('td[3]//text()').extract()]
        links = rows.xpath('td[2]//a/@href').extract()

        # iterate through the table and yield the results
        for country, index, link in zip(countries, indexes, links):
            yield {
                'country': country,
                'index': index,
                'link': link
            }