import scrapy

class SpiderSpider(scrapy.Spider):
    name = 'numbeo-ccli'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/cost-of-living/rankings_current.jsp']

    def parse(self, response):
        table = response.xpath('//*[@id="t2"]')
        rows = table.xpath('//tr')
        
        city_country_strs = [item for item in rows.xpath('td[2]/a/text()').extract()]
        # code below 
        city, country = zip(*[item.split(', ') for item in city_country_strs])
        links = rows.xpath('td[2]/a/@href').extract()
        col_index = [float(item) for item in rows.xpath('td[3]/text()').extract()]
        rent_index = [float(item) for item in rows.xpath('td[4]/text()').extract()]
        col_rent_index = [float(item) for item in rows.xpath('td[5]/text()').extract()]
        groceries_index = [float(item) for item in rows.xpath('td[6]/text()').extract()]
        restaurant_price_index = [float(item) for item in rows.xpath('td[7]/text()').extract()]
        local_purchasing_power_index = [float(item) for item in rows.xpath('td[8]/text()').extract()]
        
        for city, country, links, col_index, rent_index, col_rent_index, groceries_index, restaurant_price_index, local_purchasing_power_index in zip(city, country, links, col_index, rent_index, col_rent_index, groceries_index, restaurant_price_index, local_purchasing_power_index):
            yield {
                'city': city,
                'country': country,
                'links': links,
                'col_index': col_index,
                'rent_index': rent_index,
                'col_rent_index': col_rent_index,
                'groceries_index': groceries_index,
                'restaurant_price_index': restaurant_price_index,
                'local_purchasing_power_index': local_purchasing_power_index,
            }
        pass
