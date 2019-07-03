import json
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import ArkOperatorDetailItem


class ArkDetailSpider(Spider):
    name = 'ark-d'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    def start_requests(self):
        url = 'http://wiki.joyme.com/arknights/'
        with open("ark.json", 'r') as file:
            temp = json.loads(file.read())
            for i in range(len(temp)):
                operator_name = temp[i]['name_zh'][0]
                yield Request(url+operator_name, headers=self.headers)

    def parse(self, response):
        item = ArkOperatorDetailItem()
        main_box = response.xpath('//div[@class="mwiki_hide"][1]')

        name_box = main_box.xpath('.//div[@class="tj-bg"][1]')
        data_box = main_box.xpath('.//div[@class="tj-bg"][2]')

        item['img_src'] = main_box.xpath('.//div[@class="floatnone"][1]/a/img/@src').extract()[0]

        item['name_zh'] = name_box.xpath('./table/tr[2]/td/text()').extract()[0].strip()
        item['name_en'] = name_box.xpath('./table/tr[1]/td/text()').extract()[0].strip()

        item['operator_class'] = data_box.xpath('./table/tr[1]/td[1]/text()').extract()[1].strip()
        item['sex'] = data_box.xpath('./table/tr[2]/td[2]/text()').extract()[0].strip()
        item['camp'] = data_box.xpath('./table/tr[2]/td[1]/text()').extract()[0].strip()
        item['stars'] = data_box.xpath('./table/tr[1]/td[2]/text()').extract()[0].strip()
        item['painter'] = data_box.xpath('./table/tr[3]/td/text()').extract()[0].strip()
        item['cv'] = data_box.xpath('./table/tr[4]/td/text()').extract()[0].strip()
        item['feature'] = data_box.xpath('./table/tr[5]/td/text()').extract()[0].strip()
        item['tags'] = data_box.xpath('./table/tr[6]/td/text()').extract()[0].strip()

        item['doc'] = main_box.xpath('.//div[@class="tj-bg"][@style][1]/table/tr[2]/td/p/text()').extract() #这个是一个list
        item['record'] = main_box.xpath('.//div[@class="tj-bg"][@style][2]/table/tr[2]/td/text()').extract()[0].strip()
        # item['fighting_skill_1'] =
        # item['fighting_skill_2'] =
        # item['fighting_skill_3'] =
        # print(main_box.xpath('.//div[@class="tj-bg"][@style][2]/table/tr[2]/td/text()').extract())
        yield item


# 启动爬虫命令：scrapy crawl ark-d
# 输出结果：scrapy crawl ark -o ark-d.csv
