#### 一、Hive概论

​	Hive是一个构建在Hadoop上的数据仓库框架。最初，Hive是由Faceboo开发，后来移交由Apache软件基金会开发，并作为一个Apache开源项目。

* Hive是基于Hadoop的一个数据仓库工具，可以将结构化的数据文件映射为一张数据库表，并提供类SQL查询功能。
* Hive它能够存储很大的数据集，可以直接访问存储在Apache HDFS或其他数据存储系统（Apache HBase）中的文件。
* Hive支持MapReduce、Spark、Tez这三种分布式计算引擎。

#### 二、Hive架构

​	Hive是建立在Hadoop上的数据仓库基础架构。它提供了一系列的工具，可以存储、查询和分析存储分布式存储系统中的大规模数据集。Hive定义了简单的类SQL查询语言，通过底层的计算引擎，将SQL转为具体的计算任务进行执行。

![image-20220104160715834](.\image\image-20220104160715834.png)

#### 三、Hive计算引擎

* MapReduce

  它将计算分为两个阶段，分别为Map和Reduce。对于应用来说，需要想方设法将应用拆分成多个map、reduce的作业，以完成一个完整的算法。

  MapReduce整个计算过程会不断重复地往磁盘里读写中间结果，导致计算速度比较慢，效率比较低。

  ![image-20220104161318537](.\image\image-20220104161318537.png)

  ![image-20220104161247719](.\image\image-20220104161247719.png)

* Tez

  Tez把Map/Reduce过程拆分成若干个子过程，同时可以把多个Map/Reduce任务组合成一个较大的DAG任务，减少了Map/Reduce之间的文件存储。

  ![image-20220104161622734](.\image\image-20220104161622734.png)

* Spark

  Apache Spark是一个快速的，多用途的集群计算系统，相对于Hadoop MapReduce将中间结果保存在磁盘中，Spark使用了内存保存中间结果，能在数据尚未写入硬盘时在内存中进行运算，通知Spark提供SQL支持。

  Spark实现了一种叫做RDDs的DAG执行引擎，其数据缓存在内存中可以进行迭代处理。

![image-20220104162050294](.\image\image-20220104162050294.png)



#### 四、Hive安装和启动

* **安装**

  

* **启动Hive**

#### 五、Hive的数据库和表

* Hive数仓和传统关系型数据库类似，管理数仓数据也是通过该数据库和表

  ![image-20220105140347828](.\image\image-20220105140347828.png)

#### 六、Hive数据库操作

* 创建数据库-默认方式

  ```sql
  create database if not exists myhive;
  show databases; #查看所有数据库
  # 说明：
  # 1：if not exists:该参数可选，表示如果数据库存在则不创建（不加该参数则报错），不存在则创建。
  # 2：hive的数据库默认存放在/user/hive/warehouse目录
  ```

* 创建数据库-指定存储路径

  ```sql
  create database myhive2 location '/myhive2';
  show databases; # 查看所有数据库
  # 1: localtion: 用来指定数据库的存放目录
  ```

* 查看数据库详细信息

  ```sql
  desc database myhive;
  ```

  ![image-20220105144632401](.\image\image-20220105144632401.png)

* 删除数据库

  删除一个空的数据库，如果数据库下面由数据表，那么就会报错

  ```sql
  drop database myhive;
  ```

  强制删除数据库，包含数据库下面的表一起删除

  ```sql
  drop database myhive2 cascade;
  ```

* 创建数据库表语法

  ![image-20220105145813027](.\image\image-20220105145813027.png)

  ```sql
  CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name 
  [(col_name data_type [COMMENT col_comment], ...)] 
  [COMMENT table_comment] 
  [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] 
  [CLUSTERED BY (col_name, col_name, ...) 
  [SORTED BY (col_name [ASC|DESC], ...)] INTO num_buckets BUCKETS] 
  [ROW FORMAT row_format] 
  [LOCATION hdfs_path]
   …
  ```

* 表字段数据类型-原始类型

  ![image-20220105150135032](.\image\image-20220105150135032.png)

* 表字段数据类型-复杂类型

  ![image-20220105151901487](.\image\image-20220105151901487.png)

* 内部表操作-创建表

  未被external修饰的是内部表（managed table），内部表又称管理表。内部表不适合用于共享数据

  ```sql
  create database mytest; #创建数据库
  use mytest; #选择数据库
  create table stu(id int,name string);
  show tables; # 查询数据
  ```

  创建表之后，Hive会在对应的数据库文件夹创建对应的表目录

* 内部表操作-查看表结构/删除表

  * 查看表结构

  ```sql
  desc stu; # 查看表结构基本信息
  desc formatted stu; #查看表结构详细信息
  ```

  ![image-20220105154202248](.\image\image-20220105154202248.png)

  * 删除表

  ```sql
  drop table stu;
  ```

* 内部表操作-数据添加

  * 方式1：直接插入数据

    对于Hive中的表，可以通过insert into 指令向表中插入数据。

    ```sql
    use mytest; # 选择数据库
    create table stu(id int,name string); # 创建表
    #向表中插入数据
    insert into stu values(1,'zhangsan');
    insert into stu values(2,'lisi');
    
    select * from stu; # 查询数据
    ```

    该方式每次插入都会在表目录中生成对应的数据文件，不推荐使用。
    
  * 方式2：load数据加载
  
    Load命令用于将外部数据加载到Hive表中。
  
    ```sql
    # 语法
    LOAD DATA [LOCAL] INPATH 'filepath' [OVERWRITE] INFO TABLE tablename [PARTITION(partcol1=vall,partcol2=val2 ...)]
    # 说明
    # LOCAL表示从本地文件系统加载，否则是从HDFS加载
    ```
  
    ```sql
    # 应用1-本地加载
    # 创建表，同时指定文件的分隔符
    create table if not exists stu2(id int,name string)
    row format delimited fields terminated by '\t';
    # 向表加载数据
    load data local inpath '/export/data/hivedatas/stu.txt' into table stu2;
    ```
  
    ```sql
    ```
  
    

