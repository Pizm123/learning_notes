### 一、HDFS概述

​	

* 在现代的企业环境中，单机容量往往无法存储大量数据，需要跨机器存储。统一管理分布在集群上的文件系统称为分布式文件系统 。

* HDFS（Hadoop Distributed File System）是 Apache Hadoop 项目的一个子项目. Hadoop 非常适于存储大型数据 (比如 TB 和 PB), 其就是使用 HDFS 作为存储系统. HDFS 使用多台计算机存储文件, 并且提供统一的访问接口, 像是访问一个普通文件系统一样使用分布式文件系统. 
* 分布式文件系统解决的问题就是大数据存储。它们是横跨在多台计算机上的存储系统。分布式文件系统在大数据时代有着广泛的应用前景，它们为存储和处理超大规模数据提供所需的扩展能力。

![image-20211228105502060](.\image\image-20211228105502060.png)

#### 二、HDFS的特点

![image-20211228105836389](.\image\image-20211228105836389.png)

	* HDFS文件系统可存储超大文件，时效性稍差。
	* HDFS具有硬件故障检测和和自动快速恢复功能。
	* HDFS为数据存储提供很强的扩展能力。
	* HDFS存储一般为一次写入，多次读取，只支持追加写入，不支持随机修改。
	* HDFS可在普通廉价的机器上运行。



### 三、HDFS的架构

* HDFS采用Master/Slave架构
* 一个HDFS集群有两个重要的角色，分别是NameNode和DataNode。
* HDFS的四个基本组件：HDFS Client、NameNode、DataNode、Secondary NameNode

![image-20211229172315512](.\image\image-20211229172315512.png)

1. Client
   * 客户端
   * 文件切分。文件上传HDFS的时候，Client将文件切分成一个一个的Block，然后进行存储
   * 与NameNode交互，获取文件的位置信息。
   * 与DataNode交互，读取或者写入数据。
   * Client提供一些命令来管理和访问HDFS，比如启动或者关闭HDFS
2. NameNode
   * 就是master，他是一个主管、管理者
   * 管理HDFS元数据（文件路径、文件的大小、文件的名字、文件权限、文件的block切片信息...）
   * 配置副本策略（block副本存储的策略）
   * 处理客户端读写请求
3. DataNode
   * 就是Slave。NameNode下达命令，DataNode执行实际的操作。
   * 存储实际的数据块。
   * 执行数据块的读/写操作。
   * 定时向NameNode汇报block信息。
4. Secondary NameNode
   * 并非NameNode的热备。当NameNode挂掉的时候，它并不能马上替换NameNode并提供服务。
   * 辅助NameNode，分担其工作量。
   * 在紧急情况下，可辅助恢复NameNode。

### 四、HDFS的副本机制

* HDFS被设计成能够在一个大集群中跨机器可靠的存储超大文件。它将每个文件存储成一系列的数块，这个数据块被称为block，除了最后一个，所有数据块都是同样大小的。
* 为了容错，文件的所有block都会有副本。每个文件的数据块大小和副本系数都是可配置的。
* hadoop2中，文件的block块大小默认是128M。

![image-20211229174229938](.\image\image-20211229174229938.png)

### 五、HDFS的Shell命令

* Shell命令介绍

  * 安装好hadoop环境之后，可以执行hdfs相关的shell命令对hdfs文件系统进行操作，比如文件的创建、删除、修改文件权限等。

  * 对HDFS的操作命令类似于Linux的shell对文件的操作，如ls、mkdir、rm等。

  * Hadoop提供了文件系统的shell命令使用格式如下：

    ```shell
    hadoop fs <args>  # 既可以操作HDFS，也可以操作本地系统
    
    hdfs dfs <args>    # 只能操作HDFS系统
    ```

* Shell命令

  1. **ls命令**

  ```shell
  # 格式 hadoop fs -ls URI
  # 作用：类似于Linux的ls命令，显示文件列表
  hadoop fs -ls  /         #显示文件列表
  hadoop fs –ls -R  /   #递归显示文件列表
  ```

   	2. mkdir命令

  ```shell
  # 格式：hadoop fs -mkdir -[p] <paths>
  # 以<paths>中的URI作为参数，创建目录。使用-p参数可以递归的创建目录
  hadoop fs -mkdir /dir1
  hadoop fs  -mkdir -p /aaa/bbb/ccc
  ```

  3. put命令

  ```shell
  # 格式：hadoop fs -put <localsrc> ... <dst>
  # 作用：将单个的源文件或者多个源文件srcs从本地文件系统上传到目标文件系统中。
  # 应用：
  hadoop fs -put /root/1.txt /dir1 # 上传文件
  	
  ```
  
  4. get命令
  
  ```shell
  # 格式：hadoop fs -get <src> <localdst>
  # 作用：将HDFS文件拷贝到本地文件系统。
  # 应用：
  hadoop fs -get /1.txt /root
  ```
  
  5. mv命令
  
  ```shell
  # 格式：hadoop fs -mv <src> <dst>
  # 作用 将hdfs的文件从原路径src移动到目标路径dst，该命令不能跨文件系统
  # 应用：
  hadoop fs -mv /dir1/1.txt /dir2
  ```
  
  6. rm命令
  
  ```shell
  # 格式：hadoop fs -rm [-r][-skipTrash] URI[URI...]
  # 作用：
  # 删除参数指定的文件和目录，参数可以有多个，删除目录需要加-r参数
  # 如果指定-skipTrash选项，那么在回收站可用的情况下，该选项将跳过回收站而直接删除文件；
  # 否则，在回收站可用是，在HDFS中执行此命令，会将文件暂时放到回收站中
  # 应用：
  hadoop fs -rm /1.txt #删除文件
  
  ```
  
  7. cp命令
  
   ```shell
   # 格式：hadoop fs -cp <src> <dst>
   # 作用：将文件拷贝到目标路径中
   # 应用：
   hadoop fs -cp /dir1/1.txt /dir2
   ```
  
  8. cat命令
  
  ```shell
  # 格式：hadoop fs -cat<filepath>
  # 作用：将参数所指示的文件内容输出到控制台
  # 应用：
  hadoop fs -cat /dir1/1.txt
  ```

#### 六、HDFS的基准测试

​		实际生产环境当中，hadoop的环境搭建完成之后，第一件事情就是进行压力测试，测试我们的集群的读取和写入速度，这些操作被称为基准测试。

* **写入速度测试**

  ```shell
  # 向HDFS文件系统中写入数据,10个文件,每个文件10MB,文件存放到/benchmarks/TestDFSIO中
  hadoop jar /app/hadoop/hadoop-2.10.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.10.1.jar TestDFSIO -write -nrFiles 10 -fileSize 10MB
  ```

* **读取速度测试**

  ```shell
  #在HDFS文件系统中读入10个文件，每个文件10M
  hadoop jar /app/hadoop/hadoop-2.10.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.10.1.jar TestDFSIO -read -nrFiles 10 -fileSize 10MB
  ```

* **清除测试数据**

  ```shell
  hadoop jar /app/hadoop/hadoop-2.10.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.10.1.jar TestDFSIO -clean
  ```

  

