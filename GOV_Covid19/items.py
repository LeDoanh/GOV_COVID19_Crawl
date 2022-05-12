# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class COVID19_pandemic(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    _id = Field()
    name = Field()
    cases = Field()
    casesToday = Field()
    death = Field()
    # time = Field()
    # treating = Field()
    # recovered = Field()
    pass
