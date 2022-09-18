# docker部署dubbo-admin项目

### 一、后端

1. 后端项目打成 jar 包

2. 创建 docker 文件目录 dubbo-admin

3. dubbo-admin 目录下放入 jar 包，创建 Dockfile 文件

   ```shell
   FROM java:8
   VOLUME /tmp
   COPY app.jar app.jar
   EXPOSE 8085
   ENTRYPOINT   ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
   ```

   构建镜像文件   docker build -t dubbo .

6. 创建容器   docker run --name dubboserver -it -d -p 8085:8085 dubbo

 

### 二、前端

1. 前端项目编译， npm run build, 生成 dist 文件夹

2. 创建 docker 文件目录 dubbo-vue

3. dubbo-vue 目录下放入 dist 文件夹、创建文件夹 nginx 下创建文件 default.conf

   ```shell
   server {
    listen        80;
    server_name   192.168.126.128; # 修改为 docker 服务宿主机的 ip
   
    location / {
    	root    /usr/share/nginx/html;
    	index   index.html index.htm;
    	try_files $uri $uri/ /index.html =404;
    }
    error_page    500 502 503   504   /50x.html;
    location = /50x.html {
   	 root   html;
    }
   }
   #server_name 改成宿主机 ip
   ```

   

4. 创建文件 Dockerfile

```shell
FROM nginx
COPY dist/ /usr/share/nginx/html/
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
```

