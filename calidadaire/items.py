# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PollutantsMeasure(Item):
    # define the fields for your item here like:
    HOUR    = Field()
    STATION = Field()
    PM10    = Field()
    O3      = Field()
    NO2     = Field()
    SO2     = Field()
    CO      = Field()
    PM25    = Field()
