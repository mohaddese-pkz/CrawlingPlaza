import scrapy
class PlazaItem(scrapy.Item):
    # define the fields for items:
    title = scrapy.Field()
    price = scrapy.Field()
    originalImage = scrapy.Field()
    galleryImage = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    guaranty = scrapy.Field()
    register = scrapy.Field()
    specifications = scrapy.Field()

class PlazaItem2(scrapy.Item):
    # define the fields for item['existent']:
    existent = scrapy.Field()
