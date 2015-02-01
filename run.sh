#!/bin/bash
while :
do
    scrapy crawl stockq
    # 24 x 60 x 60 = 86400
    sleep 86300
done
