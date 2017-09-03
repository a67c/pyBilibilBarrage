import scrapy
#引入容器
from scrapytest.CourseItems import CourseItem

class Myspider(scrapy.Spider):
    #设置name
    name = "Myspider"
    #设定域名
    allowed_domains = ["bilibili.com"]
    #填写爬取地址
    start_urls = ["http://comment.bilibili.com/2015358.xml"]
    #编写爬取方法
    def parse(self, response):
        #实例一个容器保存爬取的信息
        item = CourseItem()
        #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #直接爬取弹幕内容
        arr = [];
        str0 = ''
        for box in response.xpath('/i/d/text()'):
            #获取div中的课程标题
            #item['content'] = box.extract();
            str0 += box.extract()+',';
           # arr.append(box.extract())
            #返回信息
            #print(str0)
            #item
            
            
        item['content'] = str0;
        yield item