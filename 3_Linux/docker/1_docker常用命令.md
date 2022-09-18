### docker常用命令

1. 从服务拉取镜像

   ```shell
   # docker pull [镜像名称]
   docker pull nginx
   
   #下载仓库所有Redis镜像
   docker pull -a redis
   #下载私人仓库镜像
   docker pull bitnami/redis
   ```

2. 查看镜像
   ```shell
   #列出本地镜像
   docker images
   #含中间映像层
   docker images -a
   #只显示镜像ID
   docker images -q
   #含中间映像层
   docker images -qa   
   #显示镜像摘要信息(DIGEST列)
   docker images --digests
   #显示镜像完整信息
   docker images --no-trunc
   #显示指定镜像的历史创建；参数：-H 镜像大小和日期，默认为true；--no-trunc  显示完整的提交记录；-q  仅列出提交记录ID
   docker history -H redis
   ```
   
3. 删除镜像
   ```shell
   # docker rmi [镜像名称]:[镜像版本]
   docker rmi nginx:latest
   #强制删除(针对基于镜像有运行的容器进程)
   docker rmi -f redis
   #多个镜像删除，不同镜像间以空格间隔
   docker rmi -f redis tomcat nginx
   #删除本地全部镜像
   docker rmi -f $(docker images -q)
   ```
   
4. 推送镜像到服务
   ```shell
   # docker push [镜像名称]
   docker push nginx
   ```
   
5. 保存镜像为一个压缩包
   ```shell
   # docker save -o [保存的目标文件名称] [镜像名称]
   docker save -o nginx.tar.gz nginx
   ```
   
6. 加载压缩包为镜像
   ```shell
   # docker load -i [压缩包]
   docker load -i nginx.tar
   ```
   
7. 镜像搜索

   ```shell
   #搜索仓库MySQL镜像
   docker search mysql
   #--filter=stars=600：只显示 starts>=600 的镜像
   docker search --filter=stars=600 mysql
   #--no-trunc 显示镜像完整 DESCRIPTION 描述
   docker search --no-trunc mysql
   #--automated ：只列出 AUTOMATED=OK 的镜像
   docker search  --automated mysql 
   ```

8. docker run：创建并运行一个容器，处于运行状态

   ``` shell
   docker run --name mynginx -p 80:80 -d nginx
   ```

   - docker run ：创建并运行一个容器
   - --name : 给容器起一个名字，比如叫做mynginx
   - -p ：将宿主机端口与容器端口映射，冒号左侧是宿主机端口，右侧是容器端口
   - -d：后台运行容器
   - nginx：镜像名称，例如nginx

9. 让一个运行的容器暂停

   ```shell
   # docker pause [容器名称]
   docker pause mynginx
   ```

10. 让一个容器从暂停状态恢复运行

   ```shell
   # docker unpause [容器名称]
   docker unpause mynginx

11. 停止一个运行的容器

    ```shell
    # docker stop [容器名称]
    docker stop mynginx
    #杀掉一个运行中的容器
    docker kill redis
   ```

12. 让一个停止的容器再次运行

    ```shell
    # docker start [容器名称]
    docker start mynginx
    ```

13. 删除一个容器

    ```shell
    # docker rm [容器名称]
    docker rm mynginx
    # 强制删除 docker rm -f [容器名称] 
    docker rm -f mynginx
    #删除多个容器
    docker rm -f $(docker ps -a -q)
    docker ps -a -q | xargs docker rm
    #-l 移除容器间的网络连接，连接名为 db
    docker rm -l db
    #-v 删除容器，并删除容器挂载的数据卷
    docker rm -v redis
    ```

14. 进入容器

    ``` shell
    #在centos 容器中打开新的交互模式终端，可以启动新进程
    #参数：-i  即使没有附加也保持STDIN 打开；-t  分配一个伪终端
    docker exec -it mynginx bash
    
    #以交互模式在容器中执行命令，结果返回到当前终端屏幕
    docker exec -i -t centos ls -l /tmp
    
    #以分离模式在容器中执行命令，程序后台运行，结果不会反馈到当前终端
    docker exec -d centos  touch cache.txt 
    
    #直接进入centos 容器启动命令的终端，不会启动新进程，多个attach连接共享容器屏幕
    #参数：--sig-proxy=false  确保CTRL-D或CTRL-C不会关闭容器
    docker attach --sig-proxy=false centos 
    ```

    命令解读：

    - docker exec ：进入容器内部，执行一个命令

    - -it : 给当前进入的容器创建一个标准输入、输出终端，允许我们与容器交互

    - mynginx ：要进入的容器的名称

    - bash：进入容器后执行的命令，bash是一个linux终端交互命令

15. 查看容器日志

    ```shell
    # docker logs [容器名称]
    docker logs mynginx
    # 持续查看日志 docker logs -f [容器名称]
    docker logs -f mynginx
    #查看redis容器日志，参数：-f  跟踪日志输出；-t   显示时间戳；--tail  仅列出最新N条容器日志；
    docker logs -f -t --tail=20 redis
    #查看容器redis从2019年05月21日后的最新10条日志。
    docker logs --since="2019-05-21" --tail=10 redis
    ```

16. 查看容器状态：

    ```shell
    docker ps
    #查看正在运行的容器的ID
    docker ps -q
    #查看正在运行+历史运行过的容器
    docker ps -a
    #显示运行容器总文件大小
    docker ps -s
    #显示最近创建容器
    docker ps -l
    #显示最近创建的3个容器
    docker ps -n 3
    #不截断输出
    docker ps --no-trunc 
    #获取镜像redis的元信息
    docker inspect redis
    ```

17. 容器进程

    ```shell
    #top支持 ps 命令参数，格式：docker top [OPTIONS] CONTAINER [ps OPTIONS]
    
    #列出redis容器中运行进程
    docker top redis
    #查看所有运行容器的进程信息
    for i in  `docker ps |grep Up|awk '{print $1}'`;do echo \ &&docker top $i; done
    ```

    

18. 生成镜像

    ```shell
    #基于当前redis容器创建一个新的镜像；
    #参数：
    #-a 提交的镜像作者；
    #-c 使用Dockerfile指令来创建镜像；
    #-m :提交时的说明文字；
    #-p :在commit时，将容器暂停
    docker commit -a="DeepInThought" -m="my redis" [redis容器ID]  myredis:v1.1
    ```

    

19. 容器与主机间的数据拷贝

    ```shell
    #将rabbitmq容器中的文件copy至本地路径
    docker cp rabbitmq:/[container_path] [local_path]
    #将主机文件copy至rabbitmq容器
    docker cp [local_path] rabbitmq:/[container_path]/
    #将主机文件copy至rabbitmq容器，目录重命名为[container_path]（注意与非重命名copy的区别）
    docker cp [local_path] rabbitmq:/[container_path]
    ```

    

20. 数据卷操作命令

    * 数据卷操作的基本语法如下：
    * docker volume [COMMAND]
    * docker volume命令是数据卷操作，根据命令后跟随的command来确定下一步的操作，如下以数据卷名称为html为例：

    ```shell
    # create 创建一个volume
    docker volume create html
    # inspect 显示一个或多个volume的信息
    docker volume inspect html
    # ls 列出所有的volume
    docker volume ls 
    # prune 删除未使用的volume
    docker volume prune
    # rm 删除一个或多个指定的volume
    docker volume rm html
    ```

    

21. Dockerfile文件编写及镜像构建

    ```shell
    # 指定基础镜像
    FROM ubuntu:16.04
    # 配置环境变量，JDK的安装目录
    ENV JAVA_DIR=/usr/local
    
    # 拷贝jdk和java项目的包
    COPY ./jdk8.tar.gz $JAVA_DIR/
    COPY ./eureka-server-1.0-SNAPSHOT.jar /tmp/eurekaserver.jar
    
    # 安装JDK
    RUN cd $JAVA_DIR \
     && tar -xf ./jdk8.tar.gz \
     && mv ./jdk1.8.0_144 ./java8
    
    # 配置环境变量
    ENV JAVA_HOME=$JAVA_DIR/java8
    ENV PATH=$PATH:$JAVA_HOME/bin
    
    # 暴露端口
    EXPOSE 8080
    # 入口，java项目的启动命令
    ENTRYPOINT java -jar /tmp/eurekaserver.jar
    ```

    * 镜像构建

    ```shell
    docker build -t eureka:1.0 .
    ```


18. docker-compose

    * docker-compose.yml配置文件

    ```yaml
    version: "3.2"
    
    services:
      nacos:
        image: nacos/nacos-server
        environment:
          MODE: standalone
        ports:
          - "8848:8848"
      mysql:
        image: mysql:5.7.25
        environment:
          MYSQL_ROOT_PASSWORD: root
        volumes:
          - "$PWD/mysql/data:/var/lib/mysql"
          - "$PWD/mysql/conf:/etc/mysql/conf.d/"
      userservice:
        build: ./userservice
      orderservice:
        build: ./orderservice
      gateway:
        build: ./gateway
        ports:
          - "8080:8080"
    ```

    * docker-compose常用命令

    ```shell
    # 构建镜像启动容器 
    docker-compose up -d
    # 查看日志
    docker-compose log -f
    # 停止容器
    docker-compose down
    ```

    

19. docker registry 私有仓库搭建 

    ```yaml
    # docker-compose.yml
    version: '3.0'
    services:
      registry:
        image: registry
        volumes:
          - ./registry-data:/var/lib/registry
      ui:
        image: joxit/docker-registry-ui:static
        ports:
          - 8080:80
        environment:
          - REGISTRY_TITLE=pizm私有仓库
          - REGISTRY_URL=http://registry:5000
        depends_on:
          - registry
    ```

20. Docker容器信息

    ```shell
    #查看docker容器版本
    docker version
    #查看docker容器信息
    docker info
    #查看docker容器帮助
    docker --help
    ```

    
