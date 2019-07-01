# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanMovieItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()

class ArkOperatorItem(scrapy.Item):
    name_zh = scrapy.Field()
    # name_en = scrapy.Field()
    sex = scrapy.Field()
    operator_class = scrapy.Field()
    stars = scrapy.Field()
    tags = scrapy.Field()
    img_src = scrapy.Field()