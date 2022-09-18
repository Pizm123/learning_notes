### 1、gitbook常用命令

``` shell
# 列出本地安装版本
gitbook ls
# 列出当前使用版本
gitbook current
# 列出远程可使用版本
gitbook ls-remote
# 安装2.6.9版本
gitbook fetch 2.6.9
# 卸载指定版本
gitbook uninstall 2.6.9
# 更新到指定版本，没有指定版本则到最新
gitbook update 2.6.9
# 安装当前项目所需插件，book.json
gitbook install
# 构建成Html文件，默认在_book目录下
gitbook build 
# 启动服务
gitbook serve
# 输出pdf电子书
gitbook pdf
# 输出epub电子书
gitbook epub
# 输出mobi电子书
gitbook mobi
```