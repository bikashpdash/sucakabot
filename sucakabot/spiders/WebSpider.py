import scrapy
from scrapy.loader import ItemLoader
from ..items import WebcontentItem
import json

class WebSpider(scrapy.Spider):
    name = "web"
    def start_requests(self):
        urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
        'https://www.w3schools.com/tags/tag_object.asp'
        ]        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        
        l = ItemLoader(item = WebcontentItem(), response = response)
                    
        l.add_value("url",response.url)
        l.add_xpath("title","//title/text()")
        l.add_xpath("meta_keywords","//meta[@name='Keywords']/@content")
        l.add_xpath("meta_description","//meta[@name='Description']/@content")
        l.add_xpath("body","//body")
        
        #links=[]
        #for link in self.link_extractor.extract_links(response):
        #    links.append(link)
        
        #l.add_value("links",links)
        
        return l.load_item()
        
    
    
