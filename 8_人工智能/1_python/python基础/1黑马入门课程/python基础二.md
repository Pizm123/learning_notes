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
  
* 文件操作

  * 文件操作的作用

    * 文件操作的作用就是把一些内容（数据）存储存放起来，可以让程序下一次执行的时候直接使用，而不必重新制作一份，省时省力

  * 文件的基本操作

    * 打开文件

      ```python
      f = open(name, mode)
      # name 是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
      # mode 设置打开文件的模式（访问模式）：只读、写入、追加等 mode参数可以省略，默认为r 只读
      ```

      * 访问模式

        | 模式 | 描述                                                         | 备注                                                         |
        | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
        | r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式 | 只读模式文件不存在时会报错，不能使用write()方法              |
        | w    | 打开一个文件只用于写入。如果该文件已经存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果文件不存在则会创建新文件 | 写入模式文件不存在时会创建文件，write()写入数据时会覆盖原有数据 |
        | a    | 打开一个文件用于追加，文件已经存在，文件指针会放在文件结尾   | 写入模式文件不存在时会创建文件，write()写入数据时会将数据追加到文件中 |
        | rb   | 二进制格式只读，文件指针在开头                               |                                                              |
        | r+   | 文件读写，文件指针在开头                                     |                                                              |
        | rb+  | 二进制格式读写，文件指针在开头                               |                                                              |
        | wb   | 二进制格式只写，文件指针在开头                               |                                                              |
        | w+   | 文件读写，文件指针在开头                                     | 与r+区别应该在于不存在文件会创建                             |
        | wb+  | 二进制格式读写，文件指针在开头                               |                                                              |
        | ab   | 二进制追加，指针结尾                                         |                                                              |
        | a+   | 文件读写，指针结尾                                           |                                                              |
        | ab+  | 二进制读写，指针结尾                                         |                                                              |

    * 读写等操作

      * 写

        ```python
        f = open("test.txt", 'w')
        f.write("111")
        ```

      * 读

        * read()

          ```python
          # 格式：文件对象.read(num)
          # num表示要从文件中读取的数据的长度（字节），不传num参数表示读取全部
          f = open("test.txt")
          print(f.read())
          f.close()
          ```

        * readlines() 

          readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回一个列表，每一行是一个元素

          ```python
          # 格式：文件对象.readlines()
          f = open("test.txt")
          print(f.readlines())
          # ['111\n', '222\n', '333']
          f.close()
          ```

        * readline()

          一次读取一行内容

          ```python
          # 格式：文件对象.readline()
          f = open("test.txt")
          con = f.readline()
          print(con)
          con = f.readline()
          print(con)
          f.close()
          ```

    * 关闭文件

      ```python
      f.close()
      ```

    * seek()文件操作函数

      * 作用：用来移动文件指针。

        ```python
        # 语法：文件对象.seek(偏移量, 起始位置)
        # 起始位置：0：文件开头；1：当前位置；2：文件结尾
        f = open("test.txt")
        f.seek(2,0)
        print(f.read())
        f.close()
        ```

  * 文件备份

    ```python
    def copy_file(filepath):
        index = filepath.rfind('.')
        new_filename = filepath[:index] + "[备份]" + filepath[index:]
        print(new_filename)
    
        old = open(filepath, 'rb')
        new = open(new_filename, 'wb')
        while True:
            content = old.read(1024)
            if len(content) == 0:
                break
            new.write(content)
        old.close()
        new.close()
    
    
    copy_file("test.1.txt")
    ```

  * 文件和文件夹的操作

    * 文件

      * 文件重命名

        ```python
        # os.rename('源文件名','新文件名')
        import os 
        os.rename('test.1.txt', 'test.txt')
        ```

      * 文件删除

        ```python
        # os.remove('文件名')
        import os 
        os.remove('test.txt')
        ```

    * 文件夹

      * 创建文件夹

        ```python
        # os.mkdir(文件夹名字) 文件夹存在时报错
        import os
        os.mkdir("test")
        ```

      * 删除文件夹

        ```python
        # os.rmdir(文件夹名字) 不存在则报错
        import os
        os.rmdir('test')
        ```

      * 获取当前目录

        ```python
        os.getcwd()
        ```

      * 改变默认目录

        ```python
        os.chdir(目录)
        # 相当于cd命令
        ```

      * 获取目录列表

        ```python
        os.listdir(目录) # 参数可不填，默认当前目录
        ```

      * 重命名

        ```python
        os.rename('源目录','新目录')
        ```

* 面向对象

  * 理解面向对象

    * 面向对象是一种抽象化的编程思想，很多编程语言中都有的一种思想

    * 面向对象就是将编程当成时一个事物，对外界来说，事物是直接使用的，不用去管他内部的情况。而编程就是设置事物能够做什么事。

  * 类和对象

    * 类和对象的关系，用类去创建一个对象

    * 类

      * 类是对一系列具有相同特征（属性）和行为（方法）的事物的统称，是一个抽象的概念，不是真实存在的事务。

      * 语法

        ```python
        class 类名():
            代码
        # 类名要满足标识符命名规则，同时遵循大驼峰命名习惯
        ```

    * 对象

      * 对象是类创建出来的真实存在的事物

      * 语法

        ```python
        对象名 = 类名()
        ```

      ```python
      class Washer():
          def wash(self):
              print("洗衣服")
      washer = Washer()
      washer.wash()
      ```

    * self

      self指的是调用该函数的对象

  * 添加和获取对象属性

    * 属性：属性即时特征，比如：洗衣机的宽度、高度、重量

    * 语法：

      ```python
      # 对象名.属性名 = 值
      class Washer():
          def wash(self):
              print("洗衣服")
              print(f"{self.width}")
      washer = Washer()
      washer.width = 400
      washer.height = 500
      ```

  * 魔法方法

    * ```python
      # 在python中，__xx__（）的函数叫做魔法方法，指的是具有特殊功能的函数。
      # __init__()方法 初始化对象
      class Washer():
          def __init__(self):
              self.width = 500
              self.height = 800
              
      # 带参数的__init__()
      class Washer():
          def __init__(self,width,height):
              self.width = width
              self.height = height
      haier1 = Washer(10,20)
      
      ```

    * ```python
      # 魔法方法 __str__()
      # 当使用print输出对象时，默认打印对象的内存地址。如果类定义了__str__()方法，那么就会打印这个方法中return的数据
      ```

    * ```python
      # 魔法方法 __del__()
      # 当删除对象时，python解释器也会默认调用__del__()方法
      ```

  * 案例一：烤地瓜

    ```python
    # 烤地瓜
    class SweetPotato:
        def __init__(self):
            print("-------烤地瓜系统初始化-------")
            # 被烤的时间
            self.cook_time = 0
            # 地瓜的状态
            self.cook_state = '生的'
            # 调料列表
            self.condiments = []
            # 退出系统标志
            self.is_exit = 'no'
            # 菜单id
            self.menu_id = 0
    
        def __str__(self):
            return f"这个地瓜烤了{self.cook_time}分钟，状态是：{self.cook_state}，添加的调料有{self.condiments}"
    
        def select_menu(self):
            print("1、烤地瓜")
            print("2、加点调料")
            print("3、吃地瓜")
            print("4、退出系统")
            self.menu_id = int(input("请选择需要的功能:"))
            if self.menu_id == 1:
                time = int(input("请输入烤地瓜的时间："))
                self.cook(time)
            elif self.menu_id == 2:
                condiment = input("请输入需要添加的调料：")
                self.add_condiments(condiment)
            elif self.menu_id == 3:
                print(f"恭喜您！吃到了一个{self.cook_state},并且添加了{self.condiments}的烤地瓜")
            elif self.menu_id == 4:
                self.is_exit = input("您确定需要退出烤地瓜系统么？ yes or no：")
            else:
                print("输入的指令不正确，请重新输入：")
    
        def cook(self, time):
            """烤地瓜方法"""
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time < 5:
                self.cook_state = '半生不熟'
            elif 5 <= self.cook_time < 8:
                self.cook_state = '熟了'
            elif self.cook_time >= 8:
                self.cook_state = '烤糊了'
    
        def add_condiments(self, condiment):
            """添加调料"""
            self.condiments.append(condiment)
    
    
    if __name__ == '__main__':
        sp1 = SweetPotato()
        while True:
            sp1.select_menu()
            if sp1.menu_id == 4 and sp1.is_exit == 'yes':
                print("烤地瓜系统退出成功")
                break
    ```

  * 搬家具系统

    ```python
    # 搬家具
    class House:
        def __init__(self, address, area):
            # 地理位置
            self.address = address
            # 房间面积
            self.area = area
            # 剩余面积
            self.free_area = area
            # 家具列表
            self.furniture_list = []
    
        # 添加家具
        def add_furniture(self, furniture):
            if self.free_area >= furniture.area:
                self.furniture_list.append(furniture.name)
                self.free_area -= furniture.area
            else:
                print("家具太太了，剩余面积不够了")
    
        def __str__(self):
            return f'房子坐落于{self.address}, 占地面积{self.area}平米，剩余面积{self.free_area}平米，家具有{self.furniture_list}'
    
    
    class Furniture:
        def __init__(self, name, area):
            # 家具名称
            self.name = name
            # 占地面积
            self.area = area
    
    
    house = House('北京', 100)
    bed = Furniture('双人床', 30)
    house.add_furniture(bed)
    bed = Furniture('双人床', 80)
    house.add_furniture(bed)
    print(house)
    ```

  * 经典类和新式类

    * 经典类（2.0）

      ```python
      class 类名:
          代码
          ......
      ```

    * 新式类（3.0）

      ```python
      class 类名(object):
          代码
      ```

  * 继承

    * 继承的概念

      * python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性的方法

      * 在Python中，所有类默认继承object类，object类是顶级类或基类，其他子类叫派生类

        ```python
        # 父类A
        class A(object):
            def __init__(self):
                self.num = 1
        
            def info_print(self):
                print(self.num)
        
        
        class B(A):
            pass
        
        
        result = B()
        result.info_print()

    * 单继承

      * 一个子类继承一个父类

      ```python
      class Master(object):
          def __init__(self):
              self.kongfu = '[煎饼]'
      
          def make_cake(self):
              print(f"制作{self.kongfu}煎饼果子")
      
      
      class Prentice(Master):
          pass
      
      
      pre = Prentice()
      
      print(pre.kongfu)
      ```

    * 多继承

      * 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法

      ```python
      class Master(object):
          def __init__(self):
              self.kong_fu = '[古法煎饼]'
      
          def make_cake(self):
              print(f"运用{self.kong_fu}制作煎饼果子")
      
      
      class School(object):
          def __init__(self):
              self.kong_fu = '[school煎饼果子配方]'
      
          def make_cake(self):
              print(f"运用{self.kong_fu}制作煎饼果子")
      
      
      class Prentice(School, Master):
          pass
      
      
      pizm = Prentice()
      
      print(pizm.kong_fu)
      
      pizm.make_cake()
      ```

    * 子类重写父类的同名属性和方法

      ```python
      # 子类
      class Prentice(School, Master):
          def __init__(self):
              self.kong_fu = '[pizm独创煎饼果子配方]'
          
          def make_cake(self):
              print(f"运用{self.kong_fu}制作煎饼果子")
      
      
      pizm = Prentice()
      
      print(pizm.kong_fu)
      
      # 打印父类继承关系
      print(类名.__mro__)
      ```

    * 子类调用父类的同名属性和方法(通过类名调用)

      ```python
      # 子类
      class Prentice(School, Master):
          def __init__(self):
              self.kong_fu = '[pizm独创煎饼果子配方]'
      
          def make_cake(self):
              self.__init__() # 将子类属性init
              print(f"运用{self.kong_fu}制作煎饼果子")
      
          def make_master_cake(self):
              Master.__init__(self) # 将父类属性init
              Master.make_cake(self)
      
          def make_school_cake(self):
              School.__init__(self)
              School.make_cake(self)
      ```

    * 多层继承

      ```python
      class TuSun(Prentice):
          pass
      
      sun = TuSun()
      sun.make_cake()
      ```

    * super()

      ```python
      # 通过类名调用父类方法时 代码量大切 扩展性低。通过super()调用父类方法
          def make_old_cake(self):
              # 方法一
              # Master.__init__(self)
              # Master.make_cake(self)
              # School.__init__(self)
              # School.make_cake(self)
              
              # 方法二 super()
              # 2.1 super(当前类名, self).函数()
              # super(Prentice, self).__init__()
              # super(Prentice, self).make_cake()
              
              # 2.2 无参数super
              super().__init__()
              super().make_cake()
      ```

      

    * 私有属性、私有方法

      * 作用：私有属性和私有方法在继承时不会继承给子类

      * 私有属性、方法的语法：属性名、方法名前加两个下划线 

        ```python
            # __属性名
            # __方法名
            def __init__(self):
                self.kong_fu = '[pizm独创煎饼果子配方]'
                self.__money = 2000000
        
            def __print_info(self):
                print(self.__money)
        ```

      * 获取和修改私有属性值

        ```python
            def get_money(self):
                return self.__money
        
            def set_money(self, money):
                self.__money = money
        ```

    * 面向对象三大特征

      * 封装

        * 将属性和方法书写到类里面的操作即为封装
        * 封装可以为属性和方法添加私有权限

      * 继承

        * 子类默认继承父类的所有属性和方法
        * 子类可以重写父类属性和方法

      * 多态

        * 传入不同的对象，产生不同的结果

        * 多态指的是一类事物有多种形态（一个抽象类有多个子类，因而多态的概念依赖于继承）

        * 定义：多态时一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果

        * 好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化

        * 实现步骤

          * 定义父类，提供公共方法
          * 定义子类，并重写父类方法
          * 传递子类对象给调用者，可以看到不同子类执行效果不同

        * 体验多态

          ```python
          class Dog(object):
              def work(self):
                  print("指哪打哪...")
          
          
          class ArmyDog(Dog):
              def work(self):
                  print('追击敌人...')
          
          
          class DrugDog(Dog):
              def work(self):
                  print('追查毒品...')
          
          
          class Person(object):
              def work_with_dog(self, dog):
                  dog.work()
          
          
          ad = ArmyDog()
          dd = DrugDog()
          
          pizm = Person()
          pizm.work_with_dog(ad)
          pizm.work_with_dog(dd)
          ```

    * 类属性和实例属性

      * 设置和访问类属性

        * 类属性就是类对象所拥有的属性，它被该类所有的实例对象所共有

        * 类属性可以使用类对象或实例对象访问

          ```python
          class Dog(object):
              tooth = 10
          
          
          wangcai = Dog()
          dahuang = Dog()
          
          print(Dog.tooth)
          print(wangcai.tooth)
          print(dahuang.tooth)
          ```

        * 类属性的优点

          * 记录的某项数据始终保持一致时，则定义类属性
          * 实例属性要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有的，仅占一份内存，更加节省内存空间

        * 修改类属性

          * 只能通过类修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个实例属性

            ```python
            Dog.tooth = 20
            ```

    * 类方法和静态方法

      * 类方法特点

        * 需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数。

      * 类方法使用场景

        * 当方法中需要使用类对象（如访问私有类属性 等）时，定义类方法

        * 类方法一般和类属性配合使用

          ```python
          class Dog(object):
              __tooth = 10
          
              @classmethod
              def get_tooch(cls):
                  return cls.__tooth
          
          
          print(Dog.get_tooch())
          wangcai = Dog()
          print(wangcai.get_tooch())
          ```

      * 静态方法

        * 静态方法的特点

          * 需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）
          * 静态方法也能够通过实例对象和类对象去访问

        * 静态方法的使用场景

          * 当方法中既不需要使用实例对象（实例对象、实例属性）也不需要使用类对象（类属性、类方法、创建实例等）时。定义静态方法

          * 取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗

            ```python
            class Dog(object):
                __tooth = 10
            
                @staticmethod
                def info_print():
                    print("这是一个Dog类")
            
            
            Dog.info_print()
            
            Dog().info_print()
            ```

* 异常

  * 了解异常

    * 当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的“异常”

    * 异常的写法

      ```python
      try:
          可能发生错误的菜吗
      except:
          如果出现异常执行的代码
      ```

  * 捕获异常

    * 语法

      ```python
      try:
          可能发生错误的菜吗
      except 异常类型:
          如果捕获到该异常类型执行的代码
      ```

    * 体验

      ```python
      try:
          print(num)
      except NameError:
          print("有错误")
      ```

    * 捕获多个执行异常

      ```python
      try:
          print(num)
          print(1/0)
      except (NameError, ZeroDivisionError):
          print("有错误")
      ```

    * 捕获异常描述信息

      ```python
      try:
          print(num)
          print(1/0)
      except (NameError, ZeroDivisionError) as e:
          print(e)
      ```

    * 捕获所有异常

      ```python
      # Exception是所有程序异常类的父类
      try:
          print(num)
      except Exception as e:
          print(e)
      ```

  * 异常的else

    * else表示的是如果没有异常要执行的代码

      ```python
      try:
          print(1)
      except Exception as e:
          print(e)
      else:
          print("else")
      ```

  * 异常的finally

    * finally表示的是无论是否异常都要执行的代码，例如关闭文件

      ```python
      try:
          f = open('test.txt', 'r')
      except Exception as e:
          f = open('test.txt', 'w')
      else:
          print("else")
      finally:
          f.close()
      ```

  * 异常的传递

    ```python
    import time
    
    try:
        f = open('test.txt')
        try:
            while True:
                content = f.readline()
                if len(content) == 0:
                    break
                time.sleep(2)
                print(content)
        except:
            print("意外终止了读取数据")
        finally:
            f.close()
    except:
        print('该文件不存在')
    ```
    
  * 自定义异常

    * 在Python中，抛出自定义异常的语法为raise异常类对象

      ```python
      class ShortInputError(Exception):
          def __init__(self, length, min_len):
              self.length = length
              self.min_len = min_len
      
          def __str__(self):
              return f'不能少于{self.min_len}个字符'
      
      
      def main():
          try:
              con = input('请输入密码：')
              if len(con) < 3:
                  raise ShortInputError(len(con), 3)
          except Exception as e:
              print(e)
          else:
              print("密码输入完成")
      
      
      main()
      ```

* 模块、包

  * 了解模块

    * Python模块(Module)，是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。
    * 模块能定义函数，类和变量，模块里也能包含可执行的代码

  * 导入模块

    * 导入模块的方式

      ```python
      # 三种基本方式
      import 模块名 （import 模块1,模块2）
      from 模块名 import 功能名 （from 模块名 import 功能1,功能2） # 这种方式调用时不用加 模块名.
      from 模块名 import *
      # 别名
      # 模块定义别名
      import 模块名 as 别名
      # 功能定义别名
      from 模块名 import 功能 as 别名
      ```

  * 制作模块

    * 制作模块的作用

      * 在Python中，每个Python文件都可以作为一个模块，模块的名字就是文件的名字。也就是说自定义模块名必须符合标识符命名规则。

    * 制作模块

      * 定义模块

        ```python
        # 文件名 my_module1.py
        def test_a(a, b):
            print(a + b)
        ```

      * 测试模块

        ```python
        # my_module1.py
        # 只在当前文件中调用该函数,其他导入的文件内不符合该条件，则不执行testA函数调用
        # __name__变量的值，在当前文件执行代码时为 __main__，在其他文件调用时值为 文件名
        if __name__ == '__main__':
            test_a(1, 2)
        ```

      * 使用模块

        ```python
        import my_module1
        
        my_module1.test_a(1, 3)
        ```

    * 模块定位顺序

      * 导入模块时，Python解释器对模块位置的搜索顺序是：
        * 当前目录
        * shell变量PYTHONPATH下的每个目录
        * 默认路径。linux：/usr/local/lib/python
      * 注意
        * 自己的文件名不要和已有模块名重复，否则导致模块功能无法使用
        * 使用from 模块名 import 功能的时候，如果功能名字重复，调用到的是最后定义或导入的功能

  * ```python
    __all__列表	
    ```

    * 如果一个模块文件中有 ```__all__```变量，当使用from xxx import * 导入时，只能导入这个列表中的元素

      ```py
      from my_module1 import *
      
      test_a(1, 3)
      # test_b(1, 3)

  * 包

    * 包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字```__init__.py```文件，那么这个文件夹就称之为包。

    * 制作包

      * pycharm新建软件包

    * 导入包

      ```python
      # 方法一
      import mypackage.my_module1
      
      mypackage.my_module1.info_print1()
      
      # 方法二
      # from 包名 import *时，必须在__init__.py文件中添加 __all__ = [],控制允许导入的模块列表
      from 包名 import *
      模块名.目标
      ```

  * ```__dict__``` ：收集类对象、实例对象的属性返回一个字典

    ```python
    class A(object):
        a = 0
    
        def __init__(self):
            self.b = 1
    
    
    aa = A()
    print(A.__dict__)
    print(aa.__dict__)
    ```

    