# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HauntTheWebDownItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    email = scrapy.Field()
    form = scrapy.Field()
    comments = scrapy.Field()
    location_url = scrapy.Field()
