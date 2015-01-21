# -*- coding: utf-8 -*-=
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
import unicodecsv, csv
import os.path

class StockItem(Item):
    url = Field()

def dfs(node):
    if node.xpath('*'):
        tmp = ''
        for child in node.xpath('*'):
            tmp += dfs(child)
        return tmp
    else:
        if node.xpath('text()').extract():
            return node.xpath('text()').extract()[0]
        else:
            return ''

class StockQSpider(CrawlSpider):
    name = "stockq"
    allowed_domains = ["stockq.org"]
    # start_urls = ["http://www.stockq.org/stock/history/2009/09/20090901_tc.php"]
    start_urls = ["http://www.stockq.org/stock/history/",
                  "http://www.stockq.org/stock/history/2007/",
                  "http://www.stockq.org/stock/history/2008/",
                  "http://www.stockq.org/stock/history/2009/",
                  "http://www.stockq.org/stock/history/2010/",
                  "http://www.stockq.org/stock/history/2011/",
                  "http://www.stockq.org/stock/history/2012/",
                  "http://www.stockq.org/stock/history/2013/"]
    rules = (
        Rule(
            SgmlLinkExtractor(allow = [".*20../../20......_tc.php"]),
            callback = 'parse_stock',
            # follow = False
        ),
    )
    def parse_stock(self, response):
        file_name = './data/' + response.url[-15:-7] + '.csv'
        if not os.path.isfile(file_name):
            csvfile = open(file_name, 'wb')
            writer = unicodecsv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for table in response.xpath('//table[@class="marketdatatable"]'):
                for tr in table.xpath('tr'):
                    row = []
                    for td in tr.xpath('td'):
                        row.append(dfs(td))
                    writer.writerow(row)
                writer.writerow([])