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


class ArkOperatorDetailItem(scrapy.Item):
    name_zh = scrapy.Field()#中文名
    name_en = scrapy.Field()#英文名
    sex = scrapy.Field()#性别
    operator_class = scrapy.Field()#职业
    camp = scrapy.Field()#阵营
    stars = scrapy.Field()#星级
    painter = scrapy.Field()#画师
    cv = scrapy.Field()#声优
    feature = scrapy.Field()#特性
    tags = scrapy.Field()#标签
    img_src = scrapy.Field()#背景图路径
    doc = scrapy.Field()#基础档案
    record = scrapy.Field()#履历
    fighting_skill_1 = scrapy.Field()
    fighting_skill_2 = scrapy.Field()
    fighting_skill_3 = scrapy.Field()
