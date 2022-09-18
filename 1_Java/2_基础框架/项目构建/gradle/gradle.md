## gradle配置

### 1、gradle的环境变量配置

GRADLE_HOME：D:\workTools\gradle-6.7-all\gradle-6.7  gradle的解压目录

GRADLE_USER_HOME: 自定义文件夹

Path:%GRADLE_HOME%\bin

### 2、gradle国内仓库

```
mavenLocal()
maven { url "http://maven.aliyun.com/nexus/content/groups/public/"}
mavenCentral()
```
