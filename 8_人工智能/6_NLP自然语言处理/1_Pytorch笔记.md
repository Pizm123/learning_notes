[TOC]

## 1、Pytorch基本语法

### 1.1、什么是Pytorch

* Pytorch是一个基于Numpy的科学计算包

  * 作为Numpy的替代者，向用户提供使用GPU强大功能的能力
  * 作为一款深度学习的平台，向用户提供最大的灵活性和速度

* pytorch安装

  ```shell
  pip install torch torchvision torchaudio
  ```

### 1.2、Pytorch基本元素操作

#### 1.2.1、Tensors张量

* 张量的概念类似于Numpy中的ndarray数据结构，最大区别在于Tensor可以利用GPU的加速功能

#### 1.2.1、导入torch

* inport torch

#### 1.2.2、创建矩阵

* 无初始化数据

  ```python
  x = torch.empty(5, 3)
  # 结果
  tensor([[-4.6138e+20,  5.8574e-43,  0.0000e+00],
          [ 0.0000e+00, -4.6138e+20,  5.8574e-43],
          [-4.6138e+20,  5.8574e-43, -4.6138e+20],
          [ 5.8574e-43, -4.6138e+20,  5.8574e-43],
          [-4.6138e+20,  5.8574e-43, -4.6138e+20]])
  ```

* 有初始化数据

  ```python
  x1 = torch.rand(5, 3)
  # 结果
  tensor([[0.7834, 0.1161, 0.6895],
          [0.6038, 0.3004, 0.2812],
          [0.1132, 0.9600, 0.8586],
          [0.6652, 0.4563, 0.5422],
          [0.7631, 0.2071, 0.1515]])
  ```

* 对比有无初始化矩阵：

  * 当声明无初始化的矩阵时，它本身不包含任何确切的值，当创建一个未初始化的矩阵时，分配给矩阵的内存中有什么数值就赋值什么，本质上是毫无意义的数据

* 全零矩阵/全一矩阵

  ```python
  # 全零 类型long
  x2 = torch.zeros(5, 3, dtype=torch.long)
  # 全1 
  x = torch.ones(5, 3, dtype=torch.double)
  ```

* 通过数据创建

  ```python
  x = torch.tensor([2.5, 3.5])
  ```

* 通过已有张量创建

  ```python
  # 数据随机，形状与x相同
  y = torch.randn_like(x, dtype=torch.float32)
  # 查看形状
  y.size()
  ```

#### 1.2.3、基本运算

* 加法操作

  ```python
  x+y
  torch.add(x,y)
  torch.add(x,y,out=result)
  y.add_(x)

* 切片

  ```python
  print(x[:, 1])
  ```

* 改变张量形状

  ```python
  # 元素总量不可改变，-1自动匹配数量
  x = torch.randn(4, 4)
  y = x.view(16)
  z = x.view(-1, 8)
  print(x.size(), y.size(), z.size())
  ```

* item取出

  ```python
  # tensor 只有一个元素时，item()取出元素
  x = torch.randn(1)
  print(x)
  print(x.item())
  ```

* Tensor与ndarray转换

  ```python
  # tensor.numpy(): tensor转换成ndarray
  a = torch.ones(5)
  print(a.numpy())
  
  # from_numpy(): ndarray转换成tensor
  a = np.ones(5)
  b = torch.from_numpy(a)
  print(b)
  ```

  * 所有在CPU上的Tensors，除了CharTensor，都可以转换成numpy array

* Cuda Tensor

  * Tensors可以用.to()方法移动到任意设备上

    ```python
    device = torch.device("cuda")
    x.to(device)
    x.to("cpu")
    ```

### 1.3、Pytorch中的autograd

#### 1.3.1、autograd介绍

* 在整个Pytorch框架中，所有的神经网络本质上都是一个autopackage（自动求导工具包）
  * autograd package提供了一个对Tensors上所有的操作进行自动微分的功能

#### 1.3.2、关于torch.Tensor类

* torch.Tensor是整个package中的核心类，如果将属性.requires_grad设置为True，它将追踪在这个类上定义的所有操作，当代码要进行反向传播时，直接调用.backward()就可以自动计算所有的梯度，在这个Tensor上的所有梯度将被累加进属性.grad()中
* 如果想终止一个Tensor在计算图中的追踪回溯
  * 执行.detach()就可以将该Tensor从计算图中撤下
  * with torch.no_grad()代码块

```python
x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)

print(x.grad_fn)
print(y.grad_fn)
```

#### 1.3.3、关于torch.Function类

* Function类是和Tensor同等重要的核心类，它和Tensor共同构建了一个完整的类，每个Tensor拥有一个.grad_fn属性，代表引用了哪个具体的Function创建了该Tensor
* 如果某个张量Tensor是用户自定义的，则其对应的grad_fn is None



#### 1.3.4、关于梯度Gradients

* 在Pytorch中，反向传播是依靠.backward()实现的

  ```python
  x = torch.ones(2, 2, requires_grad=True)
  y = x + 2
  z = y * y * 3
  out = z.mean()
  print(out)
  
  out.backward()
  print(x.grad)
  ```

## 2、Pytorch初步应用

### 2.1、使用Pytorch构建一个神经网络

#### 2.1.1、torch.nn

* 关于torch.nn
  * 使用Pytorch来构建神经网络，主要的工具都在torch包中
  * nn依赖autograd来定义模型，并对其自动求导

#### 2.1.2、构建神经网络的典型流程

1. 定义一个拥有可学习参数的神经网络
2. 遍历训练数据集
3. 处理输入数据使其流经神经网络
4. 计算损失值
5. 将网络参数的梯度进行反向传播
6. 以一定的规则更新网络的权重

#### 2.1.3、定义Pytorch实现的神经网络

```python
# 导入包
import torch
import torch.nn as nn
import torch.nn.functional as F


# 定义神经网络类
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 定义卷积层1 ,输入维度1，输出维度6，卷积核大小 3*3
        self.conv1 = nn.Conv2d(1, 6, 3)
        # 卷积层2，输入维度6，输出维度16，卷积核大小 3*3
        self.conv2 = nn.Conv2d(6, 16, 3)
        # 全连接层
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 卷积、激活、池化
        x = F.max_pool2d(F.relu(self.conv1(x)), (2 * 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2 * 2))
        # 调整张量形状
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)
```

* net.parameters()获取网络参数

  ```python
  params = list(net.parameters())
  print(len(params))
  print(params[0].size())
  ```

* 注意torch.nn构建的神经网络只支持mini-batches的输入，不支持单一样本输入

  * nn.Conv2d需要一个4DTensor，如果单一样本输入，需要通过input.unsqueeze(0),扩张成4D

* 假设图像尺寸32*32

  ```python
  input1 = torch.randn(1, 1, 32, 32)
  out = net(input1)
  print(out)
  print(out.size())
  ```

#### 2.1.4、损失函数

* 损失函数的输入是一个输入的pair(output，target)，然后计算出一个数值来评估output和target之间的差距大小

* 在torch.nn中有若干不同的损失函数可供使用，比如nn.MSELoss就是通过计算均方误差来评估输入和目标值之间的差距

* 应用nn.MSELoss计算损失

  ```python
  target = torch.randn(1, 10)
  criterion = nn.MSELoss()
  loss = criterion(out, target)
  print(loss)
  ```

```
print(loss.grad_fn)
print(loss.grad_fn.next_functions[0][0])
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])
```

#### 2.1.5、反向传播

* 在Pytorch中执行反向传播非常简便，全部的操作就是loss.backward()

* 在执行反向传播之前，要将梯度清零，否则梯度会在不同的批次数据之间被累加

  ```python
  # 梯度清零
  net.zero_grad()
  print(net.conv1.bias.grad)
  # 反向传播，自动求导
  loss.backward()
  print(net.conv1.bias.grad)
  ```

#### 2.1.6、更新网络参数

* 最简单的算法SGD（随机梯度下降）

  * SGD公式 weight = weight - learning_rate * gradient

* Pytorch优化器

  ```python
  import torch.optim as optim
  
  # 构建优化器
  optimizer = optim.SGD(net.parameters(), lr=0.01)
  # 优化器梯度清零
  optimizer.zero_grad()
  # 执行网络计算
  input1 = torch.randn(1, 1, 32, 32)
  output = net(input1)
  # 计算损失
  target = torch.randn(1, 10)
  criterion = nn.MSELoss()
  loss = criterion(output, target)
  # 反向传播
  loss.backward()
  # 更新参数
  optimizer.step()
  ```

  

### 2.2、使用Pytorch构建一个分类器

#### 2.2.1、分类器任务和数据介绍

* 构造一个将不同图像进行分类的神经网络分类器，对输入的图片进行判别并完成分类
* 数据集采用CIFAR10

#### 2.2.2、训练分类器步骤

* 1. 使用torchvision下载CIFAR10数据集
  
     ```python
     import torch
     import torchvision
     import torchvision.transforms as tf
     import torch.nn as nn
     import torch.nn.functional as F
     
     
     def down_datasets():
         transform = tf.Compose([tf.ToTensor(), tf.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
         train_set = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
         train_loader = torch.utils.data.DataLoader(train_set, batch_size=4, shuffle=True, num_workers=2)
     
         test_set = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
         test_loader = torch.utils.data.DataLoader(test_set, batch_size=4, shuffle=False, num_workers=2)
     
         classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
     ```
  
  2. 定义卷积神经网络
  
     ```python
     class Net(nn.Module):
         def __init__(self):
             super(Net, self).__init__()
             # 定义两个卷积层
             self.conv1 = nn.Conv2d(3, 6, 5)
             self.conv2 = nn.Conv2d(6, 16, 5)
             # 定义池化层
             self.pool = nn.MaxPool2d(2, 2)
             # 定义全连接层
             self.fc1 = nn.Linear(16 * 5 * 5, 120)
             self.fc2 = nn.Linear(120, 84)
             self.fc3 = nn.Linear(84, 10)
     
         def forward(self, x):
             x = self.pool(F.relu(self.conv1(x)))
             x = self.pool(F.relu(self.conv2(x)))
             # 变换x的形状
             x = x.view(-1, 16 * 5 * 5)
             x = F.relu(self.fc1(x))
             x = F.relu(self.fc2(x))
             x = self.fc3(x)
             return x
     ```
  
  3. 定义损失函数
  
     * 采用交叉熵损失函数和随机梯度下降优化器
  
     ```python
     net = Net()
         # 定义损失函数，选用交叉熵损失函数
         criterion = nn.CrossEntropyLoss()
         # 定义优化器
         optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
     ```
  
     
  
  4. 在训练集上训练模型
  
     * 训练
  
     ```python
     def train(net, train_loader, criterion, optimizer):
         """
         训练模型
         :return:
         """
         print("开始训练")
         for epoch in range(2):
             running_loss = 0.0
             # 按批次迭代训练模型
             for i, data in enumerate(train_loader, 0):
                 # 从data中取出含有输入图像的张量inputs，标签张量labels
                 inputs, labels = data
                 # 梯度清零
                 optimizer.zero_grad()
                 # 输入网络，得到输出张量
                 outputs = net(inputs)
                 labels = F.one_hot(labels, num_classes=10).float()
                 # 计算损失值
                 loss = criterion(outputs, labels)
     
                 # 反向传播，梯度更新
                 loss.backward()
                 optimizer.step()
     
                 # 打印训练信息
                 # print(loss.item())
                 running_loss += loss.item()
                 if (i + 1) % 200 == 0:
                     print('[%d, %5d] loss %.3f' % (epoch + 1, i + 1, running_loss / 200))
                     running_loss = 0.0
         print("训练结束")
     
     
     def save_model(net):
         """
         保存模型
         :param net:
         :return:
         """
         PATH = './cifar_net.pth'
         torch.save(net.state_dict(), PATH)
     
     
     def run():
         net = Net()
         # 定义损失函数，选用交叉熵损失函数
         criterion = nn.CrossEntropyLoss()
         # 定义优化器
         optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
         # 开始训练
         train(net, train_loader, criterion, optimizer)
         # 保存模型
         save_model(net)
     ```
  
     
  
     * 保存模型
  
     ```python
     torch.save(net.state_dict(),"./cifar_net.pth")
     ```
  
     
  
  5. 在测试集上测试模型
  
     ```python
     def test_model():
         """
         测试模型
         :return:
         """
         dataiter = iter(test_loader)
         images, labels = dataiter.next()
         print(''.join('%5s ' % classes[labels[j]] for j in range(4)))
     
         # 实例化模型对象
         net = Net()
         # 加载模型状态字典
         net.load_state_dict(torch.load("./cifar_net.pth"))
         # 预测
         outputs = net(images)
         # 选取概率最大的类别
         _, predicted = torch.max(outputs, 1)
         # 打印预测标签
         print(''.join('%5s ' % classes[predicted[j]] for j in range(4)))
     ```
  
     * 在全部测试集上的准确率
  
     ```python
     def batch_test_model():
         """
         在整个测试集上测试模型准确率
         :return:
         """
         correct = 0
         total = 0
         # 实例化模型对象
         net = Net()
         # 加载模型状态字典
         net.load_state_dict(torch.load("./cifar_net.pth"))
     
         with torch.no_grad():
             for data in test_loader:
                 images, labels = data
                 # 预测
                 outputs = net(images)
                 # 选取概率最大的类别
                 _, predicted = torch.max(outputs.data, 1)
                 total += labels.size(0)
                 correct += (predicted == labels).sum().item()
         print("准确率：%d %%" % (100 * correct / total))
     ```
  
     * 在10个类别哪些表现更好
  
       ```python
       def batch_class_test_model():
           """
           在整个测试集上测试模型每个类别的准确率
           :return:
           """
           # 实例化模型对象
           net = Net()
           # 加载模型状态字典
           net.load_state_dict(torch.load("./cifar_net.pth"))
       
           class_correct = list(0. for i in range(10))
           class_total = list(0. for i in range(10))
       
           with torch.no_grad():
               for data in test_loader:
                   images, labels = data
                   # 预测
                   outputs = net(images)
                   # 选取概率最大的类别
                   _, predicted = torch.max(outputs.data, 1)
                   c = (predicted == labels).squeeze()
                   for i in range(4):
                       label = labels[i]
                       class_correct[label] += c[i].item()
                       class_total[label] += 1
           for i in range(10):
               print("%5s准确率：%d %%" % (classes[i], 100 * class_correct[i] / class_total[i]))
       ```

#### 2.2.3、GPU上训练

```python
device = torch.device("cuda:0" if torch.cuda.is_availabe() else "cpu")

# 模型转移到GPU
net.to(device)
# 数据转移
inputs, labels = data[0].to(device), data[1].to(device)
```

