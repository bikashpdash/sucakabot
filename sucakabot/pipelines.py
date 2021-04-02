# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json  
import os

appdir=os.environ['HOME']+'/sucaka'

class SucakabotPipeline:
    def process_item(self, item, spider):
        return item



class JsonWriterPipeline:
    
    def open_spider(self, spider):
        if not os.path.exists(appdir) :
            os.makedirs(appdir)
        
        self.file = open(appdir+'/items.jl', 'w')
    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        print(item)
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
