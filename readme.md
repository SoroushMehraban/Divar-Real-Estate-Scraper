# Divar real estate scraper
This scraping tool is implemented using scrapy to scrape divar real estate adverts.

## Usage
1. Install scrapy using `pip install scrapy`
2. Change `limit` in `divar_spider.py` to which limit you want (number of adverts that is going to be crawled).
3. run the scrapy using `scrapy crawl -O divar.json`
4. You can see the result in the **divar.json** file.

