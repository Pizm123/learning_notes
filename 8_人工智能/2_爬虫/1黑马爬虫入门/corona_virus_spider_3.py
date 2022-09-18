import requests
import json
from bs4 import BeautifulSoup
import re
import time
from tqdm import tqdm


class CoronaVirusSpider(object):
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    @staticmethod
    def get_content_from_url(url):
        """
        根据URL获取响应内容的字符串数据
        :param url:
        :return:
        """
        response = requests.get(url)
        home_page = response.content.decode()
        return home_page

    @staticmethod
    def parse_home_page(home_page, script_id):
        """
        解析首页内容，获取解析后的Python对象
        :param script_id:
        :param home_page: 首页内容
        :return: 解析后的Python数据对象
        """
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id=script_id)
        text = script.text
        # 3. 从疫情数据中，获取json格式的字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # 4. 把json格式的字符串转换成Python类型
        data = json.loads(json_str)
        return data

    def parse_corona_virus(self, last_day_corona_virus_of_china, desc):
        # 定义列表
        corona_virus = []
        # 2. 遍历各国疫情数据，获取统计的URL
        for country in tqdm(last_day_corona_virus_of_china, desc):
            statistics_data_url = country['statisticsData']
            # 3. 发送请求, 获取各国从指定日期至今的json数据
            time.sleep(0.1)
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # 4. 把json数据转换为Python对象，添加列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                if country.get('countryShortCode'):
                    one_day['countryShortCode'] = country['countryShortCode']
            corona_virus.extend(statistics_data)
        return corona_virus

    @staticmethod
    def load(path):
        """
        根据路径加载json数据
        :param path: json文件路径
        :return: 文件
        """
        with open(path, encoding='utf8') as fp:
            data = json.load(fp)
        return data

    @staticmethod
    def save(data, path):
        # 5. 以json格式保存到文件中
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 解析首页内容
        last_day_corona_virus = self.parse_home_page(home_page, 'getListByCountryTypeService2true')
        # 保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集20200125以来各国疫情数据
        :return:
        """
        # 1. 加载各国疫情数据
        last_day_corona_virus = self.load('data/last_day_corona_virus.json')
        corona_virus = self.parse_corona_virus(last_day_corona_virus, '采集20200125以来各国疫情信息')
        # 5. 把列表以json格式保存到文件中
        self.save(corona_virus, 'data/corona_virus.json')

    def crawl_last_day_corona_virus_of_china(self):
        """
        采集最近一日各省疫情数据
        :return:
        """
        # 1. 发送请求，获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        # 解析数据
        data = self.parse_home_page(home_page, 'getAreaStat')
        # 保存数据
        self.save(data, 'data/last_day_corona_virus_of_china.json')

    def crawl_corona_virus_of_china(self):
        """
        采集20200125以来全国各省疫情数据
        :return:
        """
        # 1. 加载各国疫情数据
        last_day_corona_virus_of_china = self.load('data/last_day_corona_virus_of_china.json')
        # 获取全国各省市疫情数据
        corona_virus_of_china = self.parse_corona_virus(last_day_corona_virus_of_china, '采集20200125以来全国各省疫情信息')
        # 3. 把列表以json格式保存到文件中
        self.save(corona_virus_of_china, 'data/corona_virus_of_china.json')

    def run(self):
        """
        疫情数据爬虫启动方法
        :return:
        """
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()
        # self.crawl_last_day_corona_virus_of_china()
        self.crawl_corona_virus_of_china()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()
