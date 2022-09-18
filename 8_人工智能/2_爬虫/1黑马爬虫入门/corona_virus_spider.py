import requests
import json
from bs4 import BeautifulSoup
import re
import time

last_day_corona_virus = []


def load_data():
    # 1. 发送请求,获取疫情数据首页
    response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
    # 2. 从首页提取最近一日的各国疫情数据
    home_page = response.content.decode()
    soup = BeautifulSoup(home_page, 'lxml')
    script = soup.find(id='getListByCountryTypeService2true')
    text = script.text
    # 3. 从疫情数据中，获取json格式的字符串
    json_str = re.findall(r'\[.+\]', text)[0]
    # 4. 把json格式的字符串转换成Python类型
    global last_day_corona_virus
    last_day_corona_virus = json.loads(json_str)


def save_data():
    # 5. 以json格式保存到文件中
    with open('data/last_day_corona_virus.json', 'w', encoding='utf8') as fp:
        json.dump(last_day_corona_virus, fp, ensure_ascii=False)


def show_result():
    for i in last_day_corona_virus:
        print("大洲：%s\t国家：%s\t现存确诊:%s\t"
              "累计确诊:%s\t死亡:%s\t治愈:%s\t"
              % (i['continents'].ljust(3, ' '),
                 i['provinceName'].ljust(10, ' '),
                 str(i['currentConfirmedCount'] if i['currentConfirmedCount'] >= 0 else 0).ljust(10, ' '),
                 str(i['confirmedCount'] if i['confirmedCount'] >= 0 else 0).ljust(10, ' '),
                 str(i['deadCount']).ljust(8, ' '),
                 str(i['curedCount']).ljust(8, ' ')))


if __name__ == '__main__':
    print("疫情信息数据爬虫")
    while True:
        print("1、获取最新各国疫情数据")
        print("2、显示疫情数据信息")
        print("3、退出系统")
        menu_num = int(input('请选择功能序号：'))
        if menu_num == 1:
            print("爬虫正在获取疫情数据信息，请稍等...")
            load_data()
            time.sleep(2)
            print("疫情数据信息获取成功")
        elif menu_num == 2:
            show_result()
        elif menu_num == 3:
            print("系统退出成功")
            break
        else:
            print("您输入的功能序号有误，请重新输入")

