import scrapy
from scrapy_demo.items import ImgsproItem


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称，爬虫源文件的一个唯一标识
    name = 'first'
    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://sc.chinaz.com/tupian/fengjing.html']

    def parse_detail(self, response):
        img_url = response.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/p/a/@href').extract()[0]
        # print(img_url)
        item = ImgsproItem()
        item['img_url'] = img_url

        yield item

    def parse(self, response):
        detail_urls = response.xpath('/html/body/div[3]/div[2]/div/div/a/@href').extract()
        for detail_url in detail_urls:
            detail_url = 'https://sc.chinaz.com' + detail_url
            yield scrapy.Request(detail_url, callback=self.parse_detail)
