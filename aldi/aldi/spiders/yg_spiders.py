import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/the-first-order/',
	    'https://www.worldnovel.online/novel/plague-doctor/',
	    'https://www.worldnovel.online/novel/martial-peak/',
	    'https://www.worldnovel.online/novel/martial-god-asura/',
	    'https://www.worldnovel.online/novel/my-disciples-are-all-villains/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')