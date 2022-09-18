### 1、Zuul组件

​	Zuul为Netflix团队开发，主要功能市将外部请求转发到具体的微服务实例上,是实现外部访问统一入口的基础而过滤器功能则负责对请求的处理过程进行干预,是实现请求校验、服务聚合等功能的基础.

### 2、gradle配置

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
    // https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-starter-netflix-eureka-client
    implementation group: 'org.springframework.cloud', name: 'spring-cloud-starter-netflix-eureka-client', version: '3.0.3'
    // https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-starter-netflix-zuul
    implementation group: 'org.springframework.cloud', name: 'spring-cloud-starter-netflix-zuul', version: '2.2.9.RELEASE'


}

test {
    useJUnitPlatform()
}

```

### 3、配置文件

``` yaml
server:
  port: 8071
spring:
  application:
    name: gateway
eureka:
  instance:
    prefer-ip-address: true
    lease-expiration-duration-in-seconds: 90
    lease-renewal-interval-in-seconds:  30
    hostname: localhost
  client:
    fetch-registry: true
    register-with-eureka: true #是否注册
    service-url:
      defaultZone: http://localhost:8061/eureka/,http://192.168.230.1:8062/eureka/,http://127.0.0.1:8063/eureka/
zuul:
  ignore-security-headers: true
  sensitive-headers: "*"
  host:
    socket-timeout-millis: 60000
    connect-timeout-millis: 60000
```

### 4、启动类注解

增加注解@EnableZuulServer

```java
package com.pizm.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulServer;

@EnableZuulServer
@SpringBootApplication
public class GatewayApplication {

    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }

}

```

