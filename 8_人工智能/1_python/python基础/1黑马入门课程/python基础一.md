* python入门

  * python解释器

    * CPython
    * IPython
    * 其他解释器

  * IDE

    * PyCharm

  * 注释

    ```python
    # 单行注释
    """
    多行
    注释
    """
    
    '''
    多行注释
    '''
    ```

  * 变量

    * 变量的作用

      * 变量就是一个存储数据的时候当前数据所在的内存地址的名字

    * 定义变量

      ```
      变量名 = 值
      ```

    * 认识数据类型（type()方法返回数据类型）

      * 数值

        * int 整型
        * float 浮点型

      * 布尔型

        * True 真
        * False 假

      * str 字符串

      * list 列表

      * tuple 元组

      * set 集合

        * {1,2,3}

      * dict 字典

        

  * 标识符

    * 标识符命名规则

      * 数字、字母、下划线组成

      * 不能数字开头

      * 不能使用内置关键字

        * 内置关键字

          ```python
          False None True and as assert break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass paise return try while with yield
          ```

      * 严格区分大小写

    * 命名规范

      * 见名知义
      * 大驼峰
      * 小驼峰
      * 下划线

  * 常见bug

    * unexpected indent : 意外的缩进
    * name 'xxx' is not defined 变量未定义

  * 输出

    * 格式化输出

      ```python
      print("我的年龄是%d岁" % age)
      print("我的体重是%.2f" % 92.111) # .2f 保留两位小数
      print("我的学号是%06d" % 1) # %06d 输出显示位数，不足以0补全
      print("我的名字是%s,我今年%d岁了" % ("pizm",18)) 
      ```

      | 格式符号 | 转换               |
      | -------- | ------------------ |
      | %s       | 字符串             |
      | %d       | 有符号的十进制整数 |
      | %f       | 浮点数             |
      | %c       | 字符               |
      | ......   |                    |

    * %s拓展

      * %s可以替换%d、%f等

    *  f格式化字符串

      * 语法：f'{表达式}'

        ```
        print(f'我的名字是{age}')
        ```

    * 转义字符
      * \n : 换行
      * \t : 制表符 ,一个tab键的距离

    * print函数结束符

      ```python
      print('输出的内容',end="\n")
      ```

  * 输入

    * 语法：input("提示信息")

      ```python
      in1 = input("年龄:")
      ```

    * 特点

      * 程序执行到input时，等待用户输入后再向下执行
      * input接收输入后，一般存储到变量，方便使用
      * input会把接收到的任意用户输入的数据当作字符串处理

    * 转换数据类型

      * 函数

        | 函数           | 说名                                                 |
        | -------------- | ---------------------------------------------------- |
        | int(x,[,base]) | 将x转换成一个整数                                    |
        | float(x)       | 转换浮点数                                           |
        | str(x)         | 字符串                                               |
        | eval(str)      | 用来计算在字符串中的有效python表达式，并返回一个对象 |
        | tuple(s)       | 将序列s转换为一个元组                                |
        | list(s)        | 将序列s转换为一个列表                                |
        | 其他。。。     |                                                      |

        ```python
        # eval()
        str1 = '1'
        str2 = '1.1'
        str3 = '(1,2,3)'
        str4 = '[100,200,300]'
        print(type(eval(str1)))
        print(type(eval(str2)))
        print(type(eval(str3)))
        print(type(eval(str4)))
        ```

  * PyCharm交互式开发环境

    * python控制台

  * 运算符

    * 运算符的分类

      * 算数运算符

        ```python
        + - * / 
        // 整除 
        %  取余
        ** 指数
        () 小括号
        ```

        混合运算优先级顺序：() > ** > * / // % > + - 

      * 赋值运算符

        ```python
        # 单个变量赋值
        =
        # 多个变量赋值
        num1,float1,str1 = 10,0.5,'hello world'
        # 多变量赋相同值
        a = b = 10
        ```

      * 复合赋值运算符

        ```python
        += -= *= /= //= %= **=

      * 比较运算符

        ```python
        == != > < >= <=
        ```

      * 逻辑运算符

        ```python
        and or not
        ```

        * 数字之间逻辑运算

          ```python
          # and 运算符只要有一个值为0，则结果为0，否则结果为最后一个非0数字
          # or  运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
          ```

* 流程控制

  * 条件语句

    ```python
    if 条件:
        ......
    elif: 条件2:
        ......
    else:
        ......
    ```

  * 三目运算符

    ```python
    # 条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
    a if a > b else b
    ```

  * 循环

    * 循环的分类：while、for

    * while循环

      ```python
      while 条件：
      	......
      break
      continue
      ```

    * for循环

      ```python
      for 临时变量 in 序列:
          ......
      ```

    * 循环的else

      ```python
      # else 当循环正常结束之后要执行的代码，break退出时不执行
      while 条件:
          条件成立重复执行的代码
      eles:
          循环正常结束之后要执行的代码
          
      for 临时变量 in 序列:
          ......
      else:
          ......
      ```

* 数据序列

  * 字符串

    * 字符串特征

      ```python
      # 单引号
      a = 'hello world'
      # 双引号
      b = "hello world"
      # 三引号
      c = '''hello 
      world'''
      d = """hello world"""
      # 三引号的作用：换行，输出结果也会换行
      ```

    * 下标

      ```python
      # 下标又叫索引
      str1 = 'abc'
      str1[0]
      ```

    * 切片

      ```python
      # 语法 左闭右开
      序列[开始位置下标:结束位置下标:步长]
      str1 = 'abcdefg'
      print(str1[0:2]) # 步长默认为1
      print(str1[::-1]) # 步长为负数表示倒叙选取
      print(str1[-4,-1]) # 下标为负数 -1表示最后一个数据
      
      ```

  * 字符串常用操作方法

    * 查找

    ```python
    # 子串查找 
    find()、index()、count()
    # 语法：字符串序列.find(子串,开始位置下标,结束位置下标) ，
    # find查找无子串时返回-1，index查找无子串时报错
    # count()返回子串出现次数，无子串时返回0
    # rfind()、rindex() 从右侧开始查找
    ```

    * 修改

    ```python
    # 替换 
    replace()
    # 语法：字符串序列.replace(旧子串,新子串,替换次数)
    
    # 字符串分割 
    split()
    # 语法：字符串序列.split(分割字符,num)
    
    # 字符串合并 
    join()
    # 语法：连接符.join(多字符串组成的序列)
    
    # 其他函数
    capitalize() # 字符串第一个字符转大写
    title()  # 字符串每个单词首字母转大写 
    upper()  # 小写转大写
    lower()  # 大写转小写
    lstrip() # 删除左侧空白字符
    rstrip() # 删除右侧空白字符
    strip()  # 删除两侧空白字符
    ljust()  # 左对齐 语法：字符串序列.ljust(长度,填充字符)
    rjust()  # 右对齐，语法同上
    center() # 居中对齐,语法同上
    ```

    * 判断

    ```python
    # 判断以子串开头 语法：字符串序列.startswith(子串,开始位置下标,结束位置下标)
    startswith()
    # 判断以子串结束 语法: 字符串序列.endswith(子串,开始位置下标,结束位置下标)
    endswith()
    
    # 判断字符串至少有一个字符并都是字母
    isalpha()
    # 判断都是数字
    isdigit()
    # 判断字符串至少有一个字符并全是字母或数字
    isalnum()
    # 判断只包含空白
    isspace()
    ```

  * 列表

    * 列表可以一次性存储多个数据，且可以为不同数据类型，但一般存储相同类型

    * 列表的常用操作

      * 查找

        * 下标

        * 函数

          ```python
          # 返回指定数据所在下标
          index()
          # 查找元素数量
          count()
          # 列表长度
          len()
          # 判断是否存在
          'pizm' in name_list
          'pizm' not in name_list
          ```

      * 增加

        ```python
        # 列表结尾追加数据 语法：列表序列.append(数据)
        # append()追加列表时会将列表作为一个元素追加到原列表中 
        # extend()追加列表时会将每个元素拆开追加到原列表中
        append()、extend() 
        
        # 指定位置新增数据 语法：列表序列.insert(位置下标，数据)
        insert()
        ```

      * 删除

        ```python
        # 语法：del 目标 或者 del(目标)；可以删除整个列表或指定下标的元素
        
        # pop(下标) 删除指定下标，无下标默认删除最后一个，返回被删除数据
        
        # remove(元素) 删除指定元素
        
        # clear() 清空列表
        ```

      * 修改

        ```python
        # 修改指定下标
        name_list[0] = 新数据
        
        # 逆置 reverse()
        name_list.reverse()
        
        # 排序 sort(key=None,reverse=False) 默认升序，reverse = True 降序
        
        ```

      * 复制

        ```python
        # 复制列表数据，深拷贝
        copy()
        ```

      * 列表的循环遍历

        ```python
        # while 通过下标遍历
        # for
        for i in name_list:
            print(i)
        ```

      * 列表嵌套

  * 元组

    * 元组的应用场景

      * 元组与列表区别：元组内的数据不可修改

    * 定义元组

      * 元组特点
        * 定义元组使用小括号，且逗号隔开各个数据，数据可以是不同数据类型
        * 元组只有一个元素时元素后也加逗号，否则类型为单一元素的类型

    * 元组常见操作

      * 只支持查找

        ```python
        # 按下标查找
        tuple1[0]
        # 查找某个数据的下标
        index()
        # 统计元素出现次数
        count()
        # 元组长度
        len()
        ```

      * 元组中的元素是列表时，列表中的元素可以修改

  * 字典

    * 字典的应用场景

      * 字典以键值对形式出现，无序

    * 创建字典的语法

      * 字典的特点

        * 符号是{}
        * 数据为键值对形式出现
        * 各个键值对之间用逗号隔开

      * 定义

        ```python
        dict1 = {'name':'tom','age':20}
        dict1 = {}
        dict1 = dict()
        ```

    * 字典常见操作

      * 增/改

        ```python
        # 字典序列[key] = 值
        dict1['name'] = 'pizm'
        ```

      * 删除

        ```python
        # del dict1 删除字典
        # del dict1['name'] 删除键值对 ，key不存在时报错
        
        # dict1.clear() 清空字典
        ```

      * 查找

        ```python
        # dict1['name'] key值不存在时报错
        
        # get方法：语法：字典序列.get(key,默认值)，省略默认值参数时返回None
        get(key,默认值)
        
        # keys() 键列表
        dict1.keys() # 返回可迭代对象
        
        # values() 值列表
        dict1.values() # 返回可迭代对象
        
        # items() 键值对元组列表
        dict1.items() # 返回可迭代对象
        ```

    * 字典的循环遍历

      ```python
      # 遍历key
      for key in dict1.keys():
          print(key)
      # 遍历value
      for value in dict1.values():
          print(value)
      # 遍历item
      for item in dict1.items():
          print(item)
      for key,value in dict1.items():
          print(key)
          print(value)
      ```

  * 集合

    * 创建集合

      ```python
      s1 = {1,2,3}
      s2 = set('abcd')
      # 空集合
      s3 = set()
      ```

    * 集合数据的特点

    * 集合的常见操作

      * 增加

        ```python
        # add() 增加数据元素
        
        # update() 增加元素序列
        ```

      * 删除

        ```python
        # remove() 删除指定数据，数据不存在则报错
        
        # descard() 删除指定数据，数据不存在不会报错
        
        # pop() 随机删除某数据，并返回此数据
        ```

      * 查找

        ```python
        # in 判断数据在集合中
        # not in 判断数据不在集合中
        ```

  * 数据序列公共操作

    * 运算符

      | 运算符     | 描述             | 支持的容器类型           |
      | ---------- | ---------------- | ------------------------ |
      | +          | 合并             | 字符串、列表、元组       |
      | *          | 复制（str1 * 5） | 字符串、列表、元组       |
      | in、not in | 元素是否存在     | 字符串、列表、元组、字典 |

    * 公共方法

      | 函数        | 描述                                                         |
      | ----------- | ------------------------------------------------------------ |
      | len()       | 元素个数                                                     |
      | del、del()  | 删除                                                         |
      | max()       | 返回元素最大值                                               |
      | min()       | 返回元素最小值                                               |
      | range()     | 生成start到end的数字，步长为step，供for循环使用              |
      | enumerate() | 函数用于将一个可遍历的数据对象（列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中；语法：enumerate(可遍历对象, start=0);返回元组列表，（index,data） |

    * 容器类型转换

      ```python
      # 将某序列转换成元组
      tuple(原序列)
      # 转成列表
      list()
      # 转成集合
      set()
      ```

  * 推导式（生成式）

    * 作用：简化代码

    * 列表推导式

      * 作用：用一个表达式创建一个有规律的列表或控制一个有规律列表

      * 实现

        ```python
        # 列表推导式
        list1 = [i for i in range(10)]
        # 带if的列表推导式
        list2 = [i for i in range(10) if i % 2 == 0]
        # 多个for循环实现列表推导式
        list3 = [(i, j) for i in range(1, 3) for j in range(3)]
        ```

        

    * 字典推导式

      * 作用：快速合并列表为字典或提取字典中目标数据

      * 实现

        ```python
        # 字典推导式
        dict1 = {i: i ** 2 for i in range(1, 5)}
        
        # 合并列表,len统计个数小的
        dict2 = {list1[i]: list2[i] for i in range(len(list1))}
        
        # 提取字典中的目标数据
        counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
        count1 = {key: value for key, value in counts.items() if value >= 200}
        print(count1)
        ```

    * 集合推导式

      * 实现

        ```python
        list3 = [1, 1, 2]
        set1 = {i ** 2 for i in list3}
        ```

* 函数

  * 函数的作用

    * 函数就是将一段具有独立功能的代码快整合到一个整体并命名，在需要的位置调用这个名称即可完成对应的需求。
    * 函数在开发过程中，可以更高效的实现代码重用

  * 函数的使用步骤

    * 函数的定义

      ```python
      def 函数名(参数):
          ......
      ```

    * 函数的调用

      ```python
      函数名(参数)
      ```

      * 函数必须先定义后使用

  * 函数的参数作用

    * 参数让函数变得更灵活

  * 函数的返回值作用

    * 作用：调用函数后，返回需要的计算结果
    * return 表达式

  * 函数的说明文档

    * 方便的查看函数的作用

      ```python
      # 查看的说明文档
      help(函数名)
      
      # 函数说明文档的定义
      def 函数名(参数):
          """ 说明文档的位置 """
          
      # 函数说明文档高级使用 多行注释按回车
      def test(a, b):
          """
          这是函数的说明文档
          :param a: 参数1
          :param b: 参数2
          :return: 返回值
          """
          print(1)
      ```

  * 函数嵌套

    * 函数嵌套是指一个函数里面又调用了另一个函数

  * 变量的作用域

    * 变量作用域指的是变量生效的范围，主要分为两类：局部变量和全局变量

    * 局部变量：定义在函数体内部的变量，只在函数体内部生效。

      * 作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量

    * 全局变量：在函数体内、外都能生效的变量

      ```python
      # 在函数里修改全局变量的值
      def test():
          # global声明全局变量
          global a
      	a = 200
      ```

  * 多函数程序执行流程

  * 函数的返回值

    * 多返回值

      ```python
      def return_num():
          return 1, 2
      res = return_num() # 返回元组(1,2)
      a, b = return_num() # a=1,b=2
      ```

  * 函数的参数

    * 位置参数

      * 传递和定义参数的顺序及个数必须一致

    * 关键字参数

      * 函数调用时通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求

        ```python
        def user_info(name,age, gender):
            print(1)
        user_info('pizm', age=20, gender='女')
        user_info('pizm', gender='女', age=20)
        # 函数调用时，如果有位置参数，位置参数必须在关键字参数前面，但关键字参数之间无顺序要求 
        ```

    * 缺省参数

      * 缺省参数也叫默认参数，用于定义参数，为参数提供默认值，调用函数时可不传该默认参数的值

      * 注：所有位置参数必须出现在默认参数前，包括函数定义和调用

        ```python
        def user_info(name,age, gender='男'):
            print(1)
        user_info('TOM', 20)
        user_info('Rose', 18, '女')
        ```

    * 不定长参数

      * 不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时，可以用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。

      * 包裹位置传递

        ```python
        def user_info(*args):
            print(args)
        user_info('pizm', 18)
        # 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组, 
        ```

      * 包裹关键字传递

        ```python
        def user_info(**kwargs):
            print(kwargs)
        user_info(name='pizm', age=18)
        ```

        无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程

  * 拆包和交换两个变量的值

    * 拆包

      * 元组拆包

        ```python
        def return_num():
            return 100,200
        num1,num2 = return_num()
        ```

      * 字典拆包

        ```python
        dict1 = {'name': 'pizm', 'age': 18}
        a, b = dict1 # a、b 为key
        ```

    * 交换变量值

      ```python
      a, b = 1, 2
      a, b = b, a
      ```

  * 引用

    * 在python中，值时靠引用来传递的。可以用id()来判断两个变量是否为同一个值的引用。可以将id值理解为那块内存的地址标识（指针？）
    * 不可变类型数据值修改时，修改变量的引用
    * 可变类型数据值修改时，引用不变，内存中的值修改
    * 引用当作实参
      * 不可变类型：
        * 函数内修改参数值，不影响外部参数值
      * 可变类型：
        * 函数内修改参数值，会影响外部参数值

  * 可变和不可变类型

    * 可变类型
      * 列表
      * 字典
      * 集合
    * 不可变类型
      * 整型
      * 浮点型
      * 字符串
      * 元组
    
  * 函数应用：学员管理系统

    ```python
    # 学员列表
    students = []
    
    
    # 定义功能界面
    def info_print():
        print("-------请选择您需要的功能------")
        print("1、添加学员")
        print("2、删除学员")
        print("3、修改学员")
        print("4、查询学员")
        print("5、显示所有学员")
        print("6、退出系统")
        print("-" * 20)
    
    
    # 添加学员
    def add_info():
        """
        添加学员函数
        :return:
        """
    
        stu_name = input("请输入学员姓名：")
        for student in students:
            if stu_name == student['name']:
                print("当前学员已经存在")
                return
        # 学员字典
        stu_dict = {}
        stu_id = input("请输入学员学号：")
        stu_phone = input("请输入学员手机号")
        stu_dict['name'] = stu_name
        stu_dict['id'] = stu_id
        stu_dict['phone'] = stu_phone
    
        # 添加到学员列表
        students.append(stu_dict)
    
    
    # 删除学员信息
    def del_student():
        """
        删除学员信息
        :return:
        """
        del_name = input("请输入学员姓名：")
    
        for stu in students:
            if stu['name'] == del_name:
                students.remove(stu)
                break
        else:
            print('该学员不存在')
    
    
    # 修改学员信息
    def update_student():
        """修改函数"""
        name = input("请输入学员姓名：")
    
        for stu in students:
            if stu['name'] == name:
                stu['id'] = input("请输入学员学号：")
                stu['phone'] = input("请输入学员手机号：")
                break
        else:
            print('该学员不存在')
    
    
    # 查询学员
    def query_student():
        """查询学员信息"""
        name = input("请输入学员姓名：")
    
        for stu in students:
            if stu['name'] == name:
                print("学员姓名：%s 学号：%s 手机号：%s" % (stu['name'], stu['id'], stu['phone']))
                break
        else:
            print('该学员不存在')
    
    
    # 显示学员信息列表
    def show_students():
        if len(students) == 0:
            print("学员列表为空")
    
        print('学号\t姓名\t手机号')
        for student in students:
            print(f"{student['name']}\t{student['id']}\t{student['phone']}")
    
    
    if __name__ == '__main__':
        while True:
            # 1.显示功能界面
            info_print()
            # 2.用户输入功能序号
            user_num = int(input("请输入功能序号:"))
            # 3.按照功能序号执行不同的功能函数
            if user_num == 1:
                add_info()
            elif user_num == 2:
                del_student()
            elif user_num == 3:
                update_student()
            elif user_num == 4:
                query_student()
            elif user_num == 5:
                show_students()
            elif user_num == 6:
                is_exit = input('确定退出系统？ yes or no :')
                if is_exit == 'yes':
                    print("系统退出成功")
                    break
            else:
                print("输入的功能序号不正确，请重新输入")
    
    ```

* 递归

  * 递归的应用场景
    * 遍历文件夹所有文件
    * 算法，如快速排序
  * 递归的特点
    * 函数内部自己调用自己
    * 必须有出口

* lambda表达式

  * lambda表达式的应用场景

    * 如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化

  * lambda语法

    ```python
    lambda 参数列表 ：表达式
    fn2 = lambda: 100
    fn3 = lambda i1: i1 + 100
    ```

    * lambda表示式的参数可有可无，函数的参数在lambda表达式中完全适用
    * lambda表达式能接收任何数量的参数但只能返回一个表达式的值

  * lambda参数

    ```python
    # 一个参数
    fn1 = lambda a: a
    print(fn1('hello world'))
    
    # 默认参数
    fn2 = lambda a, b, c=100: a + b + c
    print(fn2(1, 2))
    
    # 不定长位置参数 *args
    fn3 = lambda *args: args
    print(fn3(10, 20, 30))
    
    # 不定长关键字参数 **args
    fn4 = lambda **kwargs: kwargs
    print(fn4(name='python', age=20))
    ```

  * lambda的应用

    ```python
    # 带判断的
    print((lambda a, b: a if a > b else b)(1, 2))
    
    # 列表数据按字典key值排序
    students = [
        {'name': 'Tom', 'age': 20},
        {'name': 'Rose', 'age': 19},
        {'name': 'Jack', 'age': 22}
    ]
    
    students.sort(key=lambda x: x['age'])
    
    print(students)
    
    students.sort(key=lambda x: x['age'], reverse=True)
    print(students)
    ```

* 高阶函数

  * 把函数作为参数传入，这样的函数成为高阶函数，高阶函数是函数式编程的体现。函数式编程就是指这种高度抽象的编程范式。

  * 体验高阶函数

    ```python
    def add_num(a, b, func):
        return func(a) + func(b)
    
    
    print(add_num(1, -2, abs))
    ```

  * 内置高阶函数

    * map(func, lst)：将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(py2)/迭代器(py3)返回

      ```python
      list1 = [1, 2, 3, 4, 5]
      
      res = map(lambda x: x ** 2, list1)
      
      print(list(res))
      ```

    * reduce(func, lst)：其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累计计算。

      ```python
      import functools
      
      list1 = [1, 2, 3, 4, 5]
      
      result = functools.reduce(lambda a, b: a * b, list1)
      
      print(result)
      ```

    * filter(func, lst) 函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。可以用list()转换成列表

      ```python
      list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      
      res = filter(lambda x: x % 2 == 0, list1)
      
      print(list(res))
      ```

      