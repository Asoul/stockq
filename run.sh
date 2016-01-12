#!/bin/bash
cd /home/asoul/stockq
/usr/local/bin/scrapy crawl stockq
/usr/bin/git add .
/usr/bin/git commit -m "daily update"
/usr/bin/git push
