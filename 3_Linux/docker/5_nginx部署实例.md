# docker上启动nginx,并配置修改nginx的配置文件

1.使用docker 下载nginx 镜像 docker pull nginx

2.启动nginx

docker run --name nginx -p 80:80 -d nginx

这样就简单的把nginx启动了，但是我们想要改变配置文件nginx.conf ，进入容器,命令：

docker exec -it nginx bash

nginx.conf配置文件在 /etc/nginx/ 下面，但是你使用vim nginx.conf 或者vi nginx.conf

会发现vi或者vim命令没有用，解决办法：apt-get update 完成之后 apt-get install vim

此时你就可以自己定制nginx.con文件了，改好配置文件之后重启容器，步骤，先把容器停了

docker stop nginx 然后重启 docker start nginx

这样不是很方便，还有第二种方式，挂载配置文件，就是把装有docker宿主机上面的nginx.conf配置文件映射到启动的nginx容器里面，这需要你首先准备好nginx.con配置文件,如果你应经准备好了，下一步是启动nginx

命令：docker run --name nginx -p 80:80 -v /home/docker-nginx/nginx.conf:/etc/nginx/nginx.conf -v /home/docker-nginx/log:/var/log/nginx -v /home/docker-nginx/conf.d/default.conf:/etc/nginx/conf.d/default.conf -d nginx

解释下上面的命令：

--name 给你启动的容器起个名字，以后可以使用这个名字启动或者停止容器

-p 映射端口，将docker宿主机的80端口和容器的80端口进行绑定

-v 挂载文件用的，第一个-v 表示将你本地的nginx.conf覆盖你要起启动的容器的nginx.conf文件，第二个表示将日志文件进行挂载，就是把nginx服务器的日志写到你docker宿主机的/home/docker-nginx/log/下面

第三个-v 表示的和第一个-v意思一样的。

-d 表示启动的是哪个镜像





### 进入docker容器

sudo docker exec -it 775c7c9ee1e1 /bin/bash  

### 文件挂载

docker run --name nginx -p 80:80 -v /home/docker-nginx/nginx.conf:/etc/nginx/nginx.conf -v /home/docker-nginx/log:/var/log/nginx -d nginx

docker run --name dubbo -p 8063:80 -d dubbo

