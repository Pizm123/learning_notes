### 1、Eureka组件

​	Eureka是Netflix开发的服务发现框架，本身是一个基于REST的服务，主要用于定位运行在AWS域中的中间层服务，以达到负载均衡和中间层服务故障转移的目的。SpringCloud将它集成在其子项目spring-cloud-netflix中，以实现SpringCloud的服务发现功能。

### 2、高可用

 	当其中一台的服务发生故障时不影响整体服务状况，不能因为一台服务器的问题导致服务停止。而Zookeeper采用的是主从方式、Eureka则采用的是集群方式，当多台服务器相互注册就形成了高可用，这样当其中的一台停止提供服务时，剩余的则会继续提供服务

### 3、Eureka配置文件

``` yaml
server:
  port: 8061
eureka:
  instance:
    hostname: ${spring.cloud.client.ip-address} # 本机域名 localhost
    #    prefer-ip-address: true # 是否使用ip进行注册
    lease-expiration-duration-in-seconds: 90 # 检测心跳间隔时间
    lease-renewal-interval-in-seconds:  30   # 发送心跳间隔时间
  server:
    enable-self-preservation: false # 开启自我保护机制
    eviction-interval-timer-in-ms: 5000 # 清理节点间隔时间
  client:
    fetch-registry: false # 是否从Eureka Server获取注册信息
    register-with-eureka: false # 是否注册
    service-url:
      defaultZone: http://localhost:8061/eureka/
#      defaultZone: http://192.168.230.1:8062/eureka/,http://127.0.0.1:8063/eureka/
```

### 4、gradle引用

``` properties
plugins {
    id 'org.springframework.boot' version '2.5.3'
    id 'io.spring.dependency-management' version '1.0.11.RELEASE'
    id 'java'
}

group = 'com.pizm'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '1.8'

repositories {
    mavenLocal()
    maven { url "https://maven.aliyun.com/repository/public"}
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    // https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-starter-netflix-eureka-server
    implementation group: 'org.springframework.cloud', name: 'spring-cloud-starter-netflix-eureka-server', version: '3.0.3'

}

test {
    useJUnitPlatform()
}

```

### 5、配置

启动类增加注解 @EnableEurekaServer

``` java
package com.pizm.eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@EnableEurekaServer
@SpringBootApplication
public class EurekaApplication {

    public static void main(String[] args) {
        SpringApplication.run(EurekaApplication.class, args);
    }

}

```

