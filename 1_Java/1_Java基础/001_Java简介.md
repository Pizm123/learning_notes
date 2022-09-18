### 一、Java语言发展史

1. 1995年美国Sun公司推出，Java之父：詹姆斯·高斯林（James Gosling）

​    ![image-20211031163622451](.\image\image-20211031163622451.png)

### 二、Java跨平台原理

1. 在需要运行Java应用程序的操作系统上，安装一个与操作系统对应的Java虚拟机（JVM（Java Virtual Machine））即可。

### 三、JRE和JDK

1. JRE（Java Runtime Environment）是Java程序的运行时环境，包含JVM和运行时所需要的核心类库。

2. JDK(Java Development Kit)时Java程序的开发工具包，包含JRE和开发人员使用的工具。开发工具其中包括编译工具（javac.exe）和运行工具(java.exe)

3. JDK、JRE和JVM的关系

   

![image-20211031163253710](.\image\image-20211031163253710.png)

### 四、JDK的下载和安装

1. JDK的安装目录

   ![image-20211031164108960](.\image\image-20211031164108960.png)

### 五、Windows常用DOS命令

![image-20211031164353524](.\image\image-20211031164353524.png)

### 六、Path环境变量的配置

```
JAVA_HOME:jdk的安装目录
Path：%JAVA_HOME%\bin
```

### 七、Java程序开发运行流程

1. 编写程序

2. 编译程序

   ```
   javac HelloWorld.java
   ```

3. 运行程序

   ```
   java HelloWorld
   ```

