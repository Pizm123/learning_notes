import requests
from lxml import etree


def test():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 ',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '.Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
    }
    session = requests.Session()
    url = "https://www.mingyantong.com"
    # proxies = {
    #     'https': 'http://127.0.0.1:10809'
    # }
    # 发起请求
    response = session.get(url, headers=headers)
    # 页面数据
    page_text = response.text
    tree = etree.HTML(page_text)
    href = tree.xpath('//*[@id="xqbdtrackouyu"]/@href')[0]
    ju_url = url + href
    print(ju_url)
    resp1 = session.get(ju_url)
    print(resp1.status_code)
    print(resp1.text)

    # print(page_text)
    # # 解析页面数据
    # tree = etree.HTML(page_text)


if __name__ == '__main__':
    test()
