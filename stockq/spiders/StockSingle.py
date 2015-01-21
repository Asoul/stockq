# -*- coding: utf-8 -*-=
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import Spider
from scrapy.item import Item, Field
import unicodecsv
import os.path
import sys

class StockItem(Item):
    url = Field()

class StockSingle(Spider):
    name = "simple"
    allowed_domains = ["stockq.org"]
    start_urls = ["http://www.stockq.org/stock/history/2009/09/20090901_tc.php"]
    

    def parse(self, response):
        file_name = 'test.csv'
        # file_name = './data/' + response.url[-15:-7] + '.csv'
        if not os.path.isfile(file_name):
            csvfile = open(file_name, 'wb')
            writer = unicodecsv.writer(csvfile, delimiter=',')
            error_flag = False
            for table in response.xpath('//table[@class="marketdatatable"]'):
                for tr in table.xpath('tr[position() > 1]'):
                    row = []
                    for td in tr.xpath('td/font'):
                        print td
                        tmp = ''
                        if td.xpath('a/text()'):# type 1
                            tmp = td.xpath('a/text()').extract()[0]
                        elif td.xpath('font/text()'):#type 2
                            tmp = td.xpath('font/text()').extract()[0]
                        elif td.xpath('span/text()') and td.xpath('text()'):#type 3
                            tmp = td.xpath('span/text()').extract()[0] + td.xpath('text()').extract()[0]
                        elif td.xpath('span/text()'):#type 4
                            tmp = td.xpath('span/text()').extract()[0]
                        elif td.xpath('text()'):#type 5
                            tmp += td.xpath('text()').extract()[0]
                        else:# QQ type
                            error_flag = True
                        row.append(tmp)
                    writer.writerow(row)
            if error_flag:
                error_log = open('./error.log', 'a')
                error_log.write("%s\n" % (response.url))