* ​	网络爬虫简介

  * 网络爬虫的定义
    * 网络爬虫（又称为网页蜘蛛，网络机器人）就是模拟客户端发送网络请求，获取响应数据，一种按照一定的规则，自动地抓取网络信息的程序或脚本
  * 网络爬虫的作用
    * 从互联网上获取我们需要的信息
  * 爬虫和浏览器的区别
    * 浏览器会将响应数据进行渲染，但爬虫不会进行渲染，爬虫是从响应数据中获取有用的数据

* requests

  * requests介绍

    * requests是一个优雅而简单的Python HTTP请求库
    * requests的作用是发送请求获取响应数据

  * requests安装

    ```python
    pip install requests
    ```

  * requests使用

    ```python
    # 1.导入模块
    import requests
    
    # 2.发送请求，获取响应
    response = requests.get("http://www.baidu.com")
    
    # 3.从响应中获取数据
    
    # 设置响应字符集
    response.encoding = 'utf8'
    
    # response.text : 响应体 str类型
    print(response.text)
    
    # requests.content ：响应体bytes数据，默认utf8
    print(response.content.decode())
    ```

* Beautiful Soup库

  * 介绍

    * Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库

  * 安装

    ```python
    # 安装Beautiful Soup 4
    pip install bs4
    # 安装lxml
    pip install lxml
    ```

  * BeautifulSoup对象

    * BeautifulSoup对象代表要解析的整个文档树，它支持遍历文档树 和 搜索文档树中描述的大部分的方法

    * 创建BeautifulSoup对象

      ```python
      from bs4 import BeautifulSoup
      soup = BeautifulSoup('<html>data</html>', 'lxml')
      print(soup)
      ```

    * find方法

      * 作用：搜索文档树

      * api

        ```python
        find(name=None, attrs={}, recursive=True, string=None, **kwargs)
        ```

        * 参数
          * name：标签名
          * attrs：属性字典
          * recursive：是否递归循环查找
          * text：根据文本内容查找
        * 返回
          * 查找到的第一个元素对象
          * find_all()方法返回所有元素对象

        ```python
        # 查找a标签:返回第一个
        a = soup.find('a')
        # 查找a标签;返回所有a标签的列表
        a_s = soup.find_all('a')
        # 查找id=link1的标签
        a = soup.find(id='link1')
        a = soup.find(attrs={'id': 'link1'})
        # 根据文本内容查找
        text = soup.find(text='Elsie')
        
        # find方法返回一个Tag对象
        a = soup.find('a')
        print(type(a)) # <class 'bs4.element.Tag'>
        
        soup.select('某种选择器（id,class,标签）') # 返回一个列表
        soup.select('.tang > ul > li > a') # 空格表示多个层级，> 表示一个层级
        ```
      
      * Tag对象
      
        * 介绍：Tag对象对应于原始文档中的XML或HTML标签，Tag有很多方法和属性，可用遍历文档树 和 搜索文档树以及获取标签内容
        * Tag对象常见属性
          * name：获取标签名称
          * attrs：获取标签所有属性的键和值
          * text：获取标签的文本字符串
  
* 正则表达式

  * 概念：正则表达式(regular expression) 是一种字符串匹配的模式（pattern）

  * 作用：

    * 检查一个字符串是否含有某种子串
    * 替换匹配的子串
    * 提取某个字符串中匹配的子串

  * 常见语法

    | 字符     | 描述                                               | 正则表达式 | 匹配字符串 |
    | -------- | -------------------------------------------------- | ---------- | ---------- |
    | 一般字符 | 匹配自身                                           | abc        | abc        |
    | .        | 匹配任意除换行符'\n'外的字符，DOTALL模式可以匹配\n | a.c        | abc        |
    | \        | 转义字符，使后一个字符改变原来的意思               |            |            |
    | [...]    | 字符集                                             |            |            |

		```python
		# 导入正则模块
		import re
		
		# 字符匹配
		rs = re.findall('abc', 'abc')
		rs1 = re.findall('a.c', 'adc')
		rs2 = re.findall('a\.c', 'a.c')
		rs3 = re.findall('a[bc]d', 'abd')
		print(rs3)
		```
		
		* 预定义字符集
		
		  | 字符 | 描述                         | 正则表达式 | 匹配字符串 |
		  | ---- | ---------------------------- | ---------- | ---------- |
		  | \d   | 数字[0-9]                    |            |            |
		  | \D   | 非数字[^\d]                  |            |            |
		  | \s   | 空白字符：[<空格>\t\r\n\f\v] |            |            |
		  | \S   | 非空白字符：【^\s】          |            |            |
		  | \w   | 单词字符：[A-Za-z0-9_]       |            |            |
		  | \W   | 非单词字符：[^\w]            |            |            |
		  |      |                              |            |            |
		
		* 数量词
		
		  | 字符 | 描述                    | 正则 | 匹配字符串 |
		  | ---- | ----------------------- | ---- | ---------- |
		  | *    | 匹配前一个字符0或无限次 |      |            |
		  | +    | 匹配前一个字符1或无限次 |      |            |
		  | ？   | 匹配前一个字符0次或1次  |      |            |
		  | {m}  | 匹配前一个字符m次       |      |            |
		
		* ```python
		  # 预定义的字符集
		  rs = re.findall('\d', '123')
		  rs = re.findall('\w', 'Aabc123_中文')
		  print(rs)
		  
		  # 数量词
		  rs = re.findall('a\d*', 'a123')
		  rs = re.findall('a\d+', 'a1')
		  rs = re.findall('a\d?', 'a2')
		  rs = re.findall('a\d{2}', 'a11')
		  print(rs)
		  ```
		
	* re.findall()方法
	
	  * API
	
	    * findall(pattern, string, flags=0)
	    * 作用：扫描整个string字符串，返回所有与pattern匹配的列表
	    * 参数
	      * pattern：正则表达式
	      * string：从哪个字符串中查找
	      * flags：匹配模式
	    * 返回
	      * 返回string中与pattern匹配的结果列表
	
	  * 分组的使用
	
	    ```python
	    rs = re.findall('a.+bc', 'a\nbc', re.DOTALL) 
	    print(rs) # ['a\nbc']
	    rs1 = re.findall('a(.+)bc', 'a\nbc', re.DOTALL)
	    print(rs1) # ['\n']
	    # 分组后，返回值只返回()中的内容，()两边的内容负责确定提取数据所在位置
	    ```
	
	* r原串
	
	  * 正则中使用r原始字符串，能够忽略转义符号带来的影响
	  * 待匹配的字符中有多少个\，r原串正则中就添加几个
	
	  ```python
	  # 1.在不使用r原串的时候，遇到转义符怎么做
	  rs = re.findall('a\\\\nbc', 'a\\nbc')
	  print(rs)
	  # 正则表达式中匹配一个转义符 需要\\\\四个斜杠
	  
	  # r原串在正则中可以消除转义符带来的影响
	  rs = re.findall(r'a\nbc', 'a\nbc')
	  print(rs)
	  
	  # 扩展：r原串可以解决写正则的时候，不符合PEP8规范的问题
	  rs = re.findall(r'\d', 'a123')
	  print(rs)
	  ```
	
* Json模块

  * 介绍

    * json模块是Python自带的模块，用于json与python数据之间的相互转换

      | JSON         | Python   |
      | ------------ | -------- |
      | object       | dict     |
      | array        | list     |
      | string       | str      |
      | number(int)  | int,long |
      | number(real) | flot     |
      | true         | True     |
      | false        | False    |
      | null         | None     |

  * Json转换成python

    * Json字符串转python

      * json.loads(s)

    * json格式的文件对象

      * json.load(fp)

      ```python
      import json
      
      # json_str = '''
      # [{"id":18788370,"createTime":1660112806000,"modifyTime":1660112806000,"tags":"","countryType":2,"continents":"欧洲","provinceId":"5","provinceName":"法国","provinceShortName":"","cityName":"","currentConfirmedCount":33620635,"confirmedCount":34141438,"confirmedCountRank":3,"suspectedCount":0,"curedCount":368023,"deadCount":152780,"deadCountRank":10,"deadRate":"0.44","deadRateRank":166,"comment":"","sort":0,"operator":"sunyanna","locationId":961002,"countryShortCode":"FRA","countryFullName":"France","statisticsData":"https://file1.dxycdn.com/2020/0315/929/3402160538577857318-135.json","incrVo":{"currentConfirmedIncr":54962,"confirmedIncr":55136,"curedIncr":0,"deadIncr":174},"showRank":true,"yesterdayConfirmedCount":2147383647,"yesterdayLocalConfirmedCount":2147383647,"yesterdayOtherConfirmedCount":2147383647,"yesterdayAsymptomaticCount":2147383647,"highDanger":"","midDanger":"","highInDesc":"","lowInDesc":"","outDesc":""}]
      # '''
      # rs = json.loads(json_str)
      # print(type(rs[0]))
      
      with open('data.json') as fp:
          l1 = json.load(fp)
          print(l1)
          print(type(l1))
      ```

  * python转换为json

    * python对象转换成json数据字符串

      * json.dumps(obj)

        ```python
        import json
        
        json_str = '''
        [{"id":18788370,"createTime":1660112806000,"modifyTime":1660112806000,"tags":"","countryType":2,"continents":"欧洲","provinceId":"5","provinceName":"法国","provinceShortName":"","cityName":"","currentConfirmedCount":33620635,"confirmedCount":34141438,"confirmedCountRank":3,"suspectedCount":0,"curedCount":368023,"deadCount":152780,"deadCountRank":10,"deadRate":"0.44","deadRateRank":166,"comment":"","sort":0,"operator":"sunyanna","locationId":961002,"countryShortCode":"FRA","countryFullName":"France","statisticsData":"https://file1.dxycdn.com/2020/0315/929/3402160538577857318-135.json","incrVo":{"currentConfirmedIncr":54962,"confirmedIncr":55136,"curedIncr":0,"deadIncr":174},"showRank":true,"yesterdayConfirmedCount":2147383647,"yesterdayLocalConfirmedCount":2147383647,"yesterdayOtherConfirmedCount":2147383647,"yesterdayAsymptomaticCount":2147383647,"highDanger":"","midDanger":"","highInDesc":"","lowInDesc":"","outDesc":""}]
        '''
        rs = json.loads(json_str)
        
        json_s = json.dumps(rs,ensure_ascii=False)
        print(json_s)
        ```

    * python类型数据以json格式存储到文件

      * json.dump(obj, fp)

        ```python
        with open('data1.json', 'w') as fp:
            json.dump(rs, fp, ensure_ascii=False)
        ```

* 疫情数据采集项目

  * 

