import scrapy
from ..items import HousingscraperItem 

class HousingspiderSpider(scrapy.Spider):
    name = 'housingspider'
    allowed_domains = ['housing.com']
    start_urls = ['https://housing.com/in/buy/searches/P3hu97oz5fhqhlxxv']

    def parse(self, response):
        housing = HousingscraperItem()
        property_name = []
        price = []
        property_name = response.css('.css-zekqfr::text , .css-ybv4ci::text').extract()
        price = response.css('.css-18rodr0::text').extract()
        location = response.css('.css-4in8py .css-16drx2b:nth-child(1)::text').extract()
        area = response.xpath('.css-ebj250:nth-child(1) .css-1ty8tu4').extract()
        owner = response.xpath('//*[@class="css-0"]/text()').extract()
        avg_price_per_sqft = response.xpath('//*[@class="css-mifb2i"]/div[2]/div[2]/text()').extract()
        
        for i in range(len(property_name)):
            housing['property_name'] = property_name[i]
            housing['price'] = price[i]
            housing['location'] = location[i]
            housing['area'] = area[i]
            housing['owner'] = owner[i]
            housing['avg_price_per_sqft'] = avg_price_per_sqft[i]
            yield housing