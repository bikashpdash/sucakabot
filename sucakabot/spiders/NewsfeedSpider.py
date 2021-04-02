from scrapy.spiders import XMLFeedSpider
from sucakabot.items import XmlfeedItem

class NewsfeedSpider(XMLFeedSpider):
    name = 'news'
    allowed_domains = ['indiatimes.com']
    start_urls = [
        'https://timesofindia.indiatimes.com/rssfeeds/1221656.cms',
        'http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms',
        'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms'
    ]
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = XmlfeedItem()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['description'] = node.xpath('description/text()').get()
        item['pubDate'] = node.xpath('pubDate/text()').get()
        return item



