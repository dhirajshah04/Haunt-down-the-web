from haunt_the_web_down.items import HauntTheWebDownItem
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
import re


class MySpider(BaseSpider):
    name = "haunt_the_web_down"
    allowed_domains = ['packtpub.com']
    start_urls = ['https://www.packtpub.com']
    def parse(self,response):
        hxs = Selector(response)

        # book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extract()
        # for title in book_titles:
        #     book =  HauntTheWebDownItem()
        #     book["title"]=title
        #     yield book


        #code for extracting emails
        emails = hxs.xpath("//*[contains(text(),'@')]").extract()
        for email in emails:
            com = HauntTheWebDownItem()
            com['email'] = email
            com['location_url']=response.url
            yield com

        #code for extracting forms

        forms = hxs.xpath('//form/@action').extract()
        for form in forms:
            formy = HauntTheWebDownItem()
            formy["form"] = form
            formy["location_url"]= response.url
            yield formy


        #code for extracting comments 
        comments = hxs.xpath('//comment()').extract()
        for comment in comments:
            com = HauntTheWebDownItem()
            com["comments"] = comment
            com["location_url"]=response.url
            yield com


        visited_links=[]
        links = hxs.xpath('//a/@href').extract()
        link_validator= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

        for link in links :
            if link_validator.match(link) and not link in visited_links :
                visited_links.append(link)
                yield Request(link,self.parse)

            else:
                full_url=response.urljoin(link)
                visited_links.append(full_url)
                yield Request(full_url,self.parse)