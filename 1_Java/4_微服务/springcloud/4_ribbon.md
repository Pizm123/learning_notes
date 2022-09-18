### 1、ribbon

Spring Cloud Ribbon是一个基于HTTP和TCP的客户端负载均衡工具，它基于Netflix Ribbon实现。通过Spring Cloud的封装，可以让我们轻松地将面向服务的REST模版请求自动转换成客户端负载均衡的服务调用。



### 2、服务端配置

```yaml
server:
  port: 8081
spring:
  application:
    name: maindataservice
  devtools:
    restart:
      enabled: true  #设置开启热部署
  freemarker:
    cache: false    #页面不加载缓存，修改即时生效
eureka:
  instance:
    hostname: ${spring.cloud.client.ip-address} # 本机域名 localhost
    #    prefer-ip-address: true # 是否使用ip进行注册
    lease-expiration-duration-in-seconds: 90 # 检测心跳间隔时间
    lease-renewal-interval-in-seconds:  30   # 发送心跳间隔时间
    instance-id: ${spring.cloud.client.ip-address}:${server.port}
  client:
    fetch-registry: true # 是否从Eureka Server获取注册信息
    register-with-eureka: true # 是否注册
    service-url:
      defaultZone: http://localhost:8061/eureka/
#      ,http://192.168.230.1:8062/eureka/,http://127.0.0.1:8063/eureka/

#  devtools
#debug: true
```



```properties
implementation group: 'org.springframework.cloud', name: 'spring-cloud-starter-netflix-eureka-client', version: '3.0.3'
```

最新版springcloud不需要引入ribbon的jar包，引入会报错找不到服务

### 3、客户端配置

```yaml
server:
  port: 8082
spring:
  application:
    name: userservice
  devtools:
    restart:
      enabled: true  #设置开启热部署
  freemarker:
    cache: false    #页面不加载缓存，修改即时生效
eureka:
  instance:
    hostname: ${spring.cloud.client.ip-address} # 本机域名 localhost
    #    prefer-ip-address: true # 是否使用ip进行注册
    lease-expiration-duration-in-seconds: 90 # 检测心跳间隔时间
    lease-renewal-interval-in-seconds:  30   # 发送心跳间隔时间
    instance-id: ${spring.cloud.client.ip-address}:${server.port}
  client:
    fetch-registry: true # 是否从Eureka Server获取注册信息
    register-with-eureka: true # 是否注册
    service-url:
      defaultZone: http://localhost:8061/eureka/
#      ,http://192.168.230.1:8062/eureka/,http://127.0.0.1:8063/eureka/

#  devtools
#debug: true
```

### 4、客户端启动类

配置bean，使用@LoadBalanced注解

```java
package com.pizm.userservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.cloud.netflix.hystrix.EnableHystrix;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestOperations;
import org.springframework.web.client.RestTemplate;

@EnableHystrix
@SpringBootApplication
public class UserserviceApplication {

    public static void main(String[] args) {
        SpringApplication.run(UserserviceApplication.class, args);
    }

    @Bean
    @LoadBalanced
    public RestTemplate initRestTemplate() {
        return new RestTemplate();
    }
}
```



### 5、调用过程

* 注入依赖

  ```java
  @Autowired
  public RestTemplate restTemplate;
  ```

* 调用服务

```java
@GetMapping("/test2")
public String test2(){
    //调用远程服务 http请求
    String url = "http://MAINDATASERVICE/getTest";
    Map map = restTemplate.getForObject(url, Map.class);
    System.out.println(map);
    return "success";
}
```

