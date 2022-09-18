1. 查看文件目录

   ```shell
   lsattr -a [-adRvV]
   ```

2. 查看端口

   ```shell
   netstat -tunlp
   ```

3. 杀进程

   ```shell
    kill -9 进程号
   ```

4. 目录权限

   ```shell
   chmod -R 777 路径
   ```

5. 查看位置

   ```she
   pwd
   ```

6. 查看日志

   ```she
   tail -300f 日志路径
   less 日志路径
   ```

7. 新建文件夹

   ```shell
   mkdir
   ```

8. 删除文件

   ```shell
   #删除文件夹
   rm -rf 路径
   #删除文件
   rm -f 文件名
   #-r 就是向下递归，不管有多少级目录，一并删除
   #-f 就是直接强行删除，不作任何提示的意思
   ```

9. 移动文件或重命名文件

   ```shell
   mv 源文件路径 目标路径
   ```

10. 压缩、解压

    ```shell
    #解压 tar包
    tar –xvf file.tar
    #解压tar.gz
    tar -xzvf file.tar.gz
    #解压 tar.bz2
    tar -xjvf file.tar.bz2
    #解压tar.Z
    tar –xZvf file.tar.Z
    #解压rar
    unrar e file.rar
    #解压zip
    unzip file.zip
    #压缩
    tar -zcvf 压缩文件名.tar.gz 文件名
    ```

11. 远程复制

    ```shell
    scp -r 本地文件 用户名@ip:/远程路径
    ```

12. 查看文件大小

    ```shell
    du -h 文件名
    ```

13. 查看字符集

    ```shell
    #查看字符集
    echo #LANG
    #修改字符集
    export LANG=字符集
    ```

14. 查看空间存储情况

    ```shell
    df -ah
    ```

15. 查看进程

    ```shell
    ps -ef |grep 关键字
    ```

16. 防火墙

    ```shell
    #查看防火墙
    systemctl status firewalld
    #关闭防火墙（暂时，重启服务器时防火墙打开）
    systemctl stop firewalld
    #永久关闭
    systemctl disable firewalld
    #放开防火墙端口
    firewall-cmd --zone=public --add-port=8061/tcp --permanent
    firewall-cmd --reload
    ```

    

