# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst,MapCompose
import html2text

def format_html_body(content):
    h = html2text.HTML2Text()
    h.ignore_links = True
    return h.handle(content)


class SucakabotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebcontentItem(scrapy.Item):
    url=scrapy.Field(output_processor=TakeFirst())
    title=scrapy.Field(output_processor=TakeFirst())
    meta_keywords=scrapy.Field(output_processor=TakeFirst())
    meta_description=scrapy.Field(output_processor=TakeFirst())
    body=scrapy.Field(input_processor=MapCompose(format_html_body),output_processor=TakeFirst())
    links=scrapy.Field()

class XmlfeedItem(scrapy.Item):
    guid=scrapy.Field()
    title=scrapy.Field()
    description=scrapy.Field()
    link=scrapy.Field()
    pubDate=scrapy.Field()
    
