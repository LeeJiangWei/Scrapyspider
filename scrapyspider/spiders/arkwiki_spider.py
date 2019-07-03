from scrapy.spiders import Spider
from scrapy import Request
from scrapyspider.items import ArkOperatorItem


class ArkWikiSpider(Spider):
    name = 'ark'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    def start_requests(self):
        url = "http://wiki.joyme.com/arknights/%E5%B9%B2%E5%91%98%E6%95%B0%E6%8D%AE%E8%A1%A8"
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = ArkOperatorItem()
        operators = response.xpath('//table[@id="CardSelectTr"]/tr')
        # print("operators:", operators)
        for operator in operators:
            item['name_zh'] = operator.xpath(
                './td[2]/a/text()'
            ).extract()
            item['sex'] = operator.xpath(
                './@data-param3'
            ).extract()
            item['operator_class'] = operator.xpath(
                './@data-param1'
            ).extract()
            item['stars'] = operator.xpath(
                './@data-param2'
            ).re(r'[1-6]')
            item['tags'] = operator.xpath(
                './@data-param5'
            ).extract()
            item['img_src'] = operator.xpath(
                './td[1]/div/div/a/img/@src'
            ).extract()
            yield item

#启动爬虫命令：scrapy crawl ark
#输出结果：scrapy crawl ark -o ark.csv