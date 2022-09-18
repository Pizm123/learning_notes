# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class ImgsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """
        根据图片地址进行图片数据的请求
        :param item:
        :param info:
        :return:
        """
        if str(item['img_url']).endswith('.jpg'):
            yield scrapy.Request(item['img_url'])

    def file_path(self, request, response=None, info=None, *, item=None):
        """
        指定图片存储的路径
        :param request:
        :param response:
        :param info:
        :param item:
        :return:
        """
        img_name = request.url.split('/')[-1]
        return img_name

    def item_completed(self, results, item, info):
        """
        返回给下一个即将被执行的管道类
        :param results:
        :param item:
        :param info:
        :return:
        """
        return item
