#引入文件
import scrapy

class CourseItem(scrapy.Item):
    #弹幕内容
    content = scrapy.Field()
