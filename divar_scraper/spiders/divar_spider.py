import scrapy


class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = ['https://divar.ir/s/tehran/real-estate']
    limit = 100
    count = 0
    current_page = 1

    def parse(self, response, **kwargs):
        for card in response.css('a.kt-post-card.kt-post-card--outlined'):
            yield {
                'title': card.css('div.kt-post-card__title::text').get(),
                'description': card.css('div.kt-post-card__description::text').get(),
                'link': f'https://divar.ir/{card.attrib["href"]}',
            }
            self.count += 1
            if self.count == self.limit:
                break

        if self.count < self.limit:
            self.current_page += 1
            next_page = f"{self.start_urls[0]}?page={self.current_page}"
            yield response.follow(next_page, callback=self.parse)
