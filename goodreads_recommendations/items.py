# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def strip_spaces(value):
    return value.lstrip(' ').rstrip(' ')

class GoodreadsRecommendationsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor=MapCompose(strip_spaces), output_processor=TakeFirst())
    author = scrapy.Field(input_processor=MapCompose(strip_spaces), output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
