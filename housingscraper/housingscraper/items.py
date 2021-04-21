import scrapy

class HousingscraperItem(scrapy.Item):
    property_name = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    area = scrapy.Field()
    owner = scrapy.Field()
    avg_price_per_sqft = scrapy.Field()
