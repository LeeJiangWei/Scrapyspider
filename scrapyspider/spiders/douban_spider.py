from scrapy.spiders import Spider
from scrapy import Request
from scrapyspider.items import DoubanMovieItem

class DoubanSpider(Spider):
    name = "douban"
    headers = {
        'User-Agent':""
    }
    start_urls = ["https://movie.douban.com/top250"]

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()'
            ).extract()
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()'
            ).extract()
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span[4]/text()'
            ).re(r'[0-9]+')
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)

#启动爬虫命令：scrapy crawl douban
#输出结果：scrapy crawl douban -o douban.csv