#!/bin/bash
cd /root/stockq
scrapy crawl stockq
git add .
git commit -m "daily update"
git push
