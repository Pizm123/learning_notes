### 1、断路器Hystrix

​	当对某个服务的调用在一定的时间内（默认10s，由metrics.rollingStats.timeInMilliseconds配置），有超过一定次数（默认20次，由circuitBreaker.requestVolumeThreshold参数配置）并且失败率超过一定值（默认50%，由circuitBreaker.errorThresholdPercentage配置），该服务的断路器会打开。返回一个由开发者设定的fallback

### 2、断路器使用

* 启动类增加注解

```java
@EnableHystrix
```

* controller类增加注解

```java
@HystrixCommand(fallbackMethod = "hystrixMethod")
```

* 方法使用注解

```
@HystrixCommand(fallbackMethod = "hystrixMethod")
```

* 增加方法

```java
public String hystrixMethod(){
    return "调用失败，调用hystrix回调方法";
}
```

