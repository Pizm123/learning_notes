import requests
from lxml import etree
import os
import json
from tqdm import tqdm
# 系统注册表
import winreg
# 线程池
from concurrent.futures import ThreadPoolExecutor


class IpPool(object):
    # 系统代理开关 enable: 0关闭，1开启
    KEY_ProxyEnable = "ProxyEnable"
    # 系统代理地址
    KEY_ProxyServer = "ProxyServer"
    # 系统代理忽略
    KEY_ProxyOverride = "ProxyOverride"
    # 忽略代理ip
    ignore_ip = "172.*;192.*;"
    # 注册表配置
    KEY_XPATH = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    # 线程池
    pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix='线程')

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 '
        }
        self.ips = []
        self.proxies_list = []

    @staticmethod
    def save(data, filepath):
        """
        保存ip列表到文件中
        :return:
        """
        if not os.path.exists('./ip_pool'):
            os.mkdir('./ip_pool')
        with open('./ip_pool/' + filepath, 'w') as fp:
            json.dump(data, fp, ensure_ascii=False)

    @staticmethod
    def load(filepath):
        """
        加载文件中的ip地址列表
        :return:
        """
        with open('./ip_pool/' + filepath) as fp:
            data = json.load(fp)
        return data

    @staticmethod
    def build_proxies_param(proxies):
        """
        构造requests请求的代理参数
        :param proxies:
        :return:
        """
        return {'http': 'http://' + proxies, 'https': 'https://' + proxies}

    def build_proxies(self):
        """
        构造ip:端口列表
        :return:
        """
        # self.ips.sort(key=lambda x: x['speed'])
        for ipaddress in self.ips:
            proxies = ipaddress['ip'] + ':' + ipaddress['port']
            # self.proxies_list.append(proxies)

    def batch_test_proxies(self):
        """
        批量测试ip代理可用性
        :return:
        """
        for ipaddress in self.ips:
            print(len(self.ips))
            proxies = ipaddress['ip'] + ':' + ipaddress['port']
            self.pool.submit(self.test_proxies, proxies)

    def test_proxies(self, proxies):
        """
        测试单个代理ip可用性
        :param proxies:
        :return:
        """
        proxies_param = self.build_proxies_param(proxies)
        try:
            response = requests.get('http://www.baidu.com/', headers=self.headers, proxies=proxies_param, timeout=10)
            if response.status_code == 200:
                print("测试代理ip%s,结果：代理ip正常" % proxies)
                self.proxies_list.append(proxies)
                return True
        except Exception as e:
            print("测试代理ip%s,结果：代理ip响应超时" % proxies)
            return False

    def get_ips(self):
        """
        获取快代理免费代理ip
        :return: 免费代理ip列表
        """
        for i in range(1, 6):
            url = 'https://free.kuaidaili.com/free/inha/' + str(i) + '/'
            # 发起请求
            response = requests.get(url, headers=self.headers)
            # 页面数据
            page_text = response.text
            # 解析页面数据
            tree = etree.HTML(page_text)
            tr_list = tree.xpath('//*[@id="list"]/table/tbody/tr')

            for tr in tqdm(tr_list, '第%s页代理ip爬取进度：' % i):
                ip = tr.xpath('./td[1]/text()')[0]
                port = tr.xpath('./td[2]/text()')[0]
                speed = tr.xpath('./td[6]/text()')[0]
                address = {'ip': ip, 'port': port, 'speed': str(speed).replace('秒', '')}
                self.ips.append(address)

    def update_ip_pool(self):
        """
        更新ip池地址
        :return:
        """
        # 获取快代理的免费代理ip
        self.get_ips()
        # 清空现有代理ip池
        self.proxies_list = []
        # 测试
        self.batch_test_proxies()
        # 代理列表保存到文件
        self.save(self.proxies_list, 'proxies_list.json')

    def get_proxies(self):
        """
        获取一个代理ip
        :return:
        """
        for proxies in self.proxies_list:
            if self.test_proxies(proxies):
                return proxies
            else:
                self.proxies_list.remove(proxies)

    def set_global_proxy(self, enable, proxy_ip):
        """
        设置系统全局代理
        :return:
        """
        h_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.KEY_XPATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(h_key, self.KEY_ProxyEnable, 0, winreg.REG_DWORD, enable)
        winreg.SetValueEx(h_key, self.KEY_ProxyServer, 0, winreg.REG_SZ, proxy_ip)
        winreg.SetValueEx(h_key, self.KEY_ProxyOverride, 0, winreg.REG_SZ, self.ignore_ip)
        winreg.CloseKey(h_key)

    def get_proxy_status(self):
        """
        获取全局代理状态
        :return:
        """
        h_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.KEY_XPATH, 0, winreg.KEY_READ)
        ret_val = winreg.QueryValueEx(h_key, self.KEY_ProxyEnable)
        winreg.CloseKey(h_key)
        return ret_val[0] == 1

    def open_global_proxy(self):
        """
        开启系统全局代理
        :return:
        """
        proxy_ip = self.get_proxies()
        print("设置全局代理ip：" + proxy_ip)
        self.set_global_proxy(1, proxy_ip)
        print("全局代理开启成功")

    def close_global_proxy(self):
        """
        关闭系统全局代理
        :return:
        """
        self.set_global_proxy(0, '')
        print("全局代理关闭成功")

    @staticmethod
    def show_menu():
        print("-----IP代理系统-----")
        print("1、更新代理IP池")
        print("2、获取一个可用代理IP")
        print("3、测试IP池代理可用性")
        print("4、获取系统全局代理状态")
        print("5、开启系统全局代理")
        print("6、关闭系统全局代理")
        print("7、退出系统")

    def run(self):
        """
        系统启动入口
        :return:
        """
        # 加载ip列表
        self.proxies_list = self.load('proxies_list.json')
        while True:
            self.show_menu()
            menu_id = int(input("请输入功能菜单编号："))
            if menu_id == 1:
                self.update_ip_pool()
            elif menu_id == 2:
                print(self.get_proxies())
            elif menu_id == 3:
                self.batch_test_proxies()
            elif menu_id == 4:
                if self.get_proxy_status():
                    print("系统全局代理状态为：开启")
                else:
                    print("系统全局代理状态为：关闭")
            elif menu_id == 5:
                self.open_global_proxy()
            elif menu_id == 6:
                self.close_global_proxy()
            elif menu_id == 7:
                is_exist = input("您是否要退出系统? yes or no：")
                if is_exist == 'yes':
                    print("系统退出成功")
                    break
            else:
                print("输入的功能菜单编号不正确，请重新输入")


if __name__ == '__main__':
    ip_pool = IpPool()
    ip_pool.run()
