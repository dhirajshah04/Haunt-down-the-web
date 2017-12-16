from haunt_the_web_down.items import HauntTheWebDownItem
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import BaseSpider


class MySpider(BaseSpider):
    name = "haunt_the_web_down"
    allowed_domains = ['packtpub.com']
    start_urls = ['https://www.packtpub.com']
    def parse(self,response):
        hxs = Selector(response)
        book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extract()
        for title in book_titles:
            book =  HauntTheWebDownItem()
            book["title"]=title
            yield book