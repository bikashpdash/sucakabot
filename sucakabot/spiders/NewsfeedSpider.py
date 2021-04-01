from scrapy.spiders import XMLFeedSpider

class NewsfeedspiderSpider(XMLFeedSpider):
    name = 'NewsfeedSpider'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['http://https://timesofindia.indiatimes.com/rssfeeds/1221656.cms']
    
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item['url'] = selector.select('url').get()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()
        return item
