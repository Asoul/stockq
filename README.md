# stockq
這是一個會爬 stockq 的 crawler，可以把近幾年的每天資料抓下來以做分析。
## Usage
詳細設定要去每個檔案裡更改目標的 url
#####多個頁面
<code>scrapy crawl stockq</code>
#####單個頁面
<code>scrapy crawl simple</code>
## 帶新增功能
1. 抓新增時會看現在日期往回抓，不要每次都全試試看所有連結