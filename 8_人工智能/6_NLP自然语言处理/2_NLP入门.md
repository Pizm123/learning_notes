[TOC]



## 一、NLP简介

### 1.1、什么是自然语言处理
- 自然语言处理（NLP）是计算机科学与语言学中关注计算机与人类语言间转换的领域

### 1.2、NLP发展简史

1. 1950年 图灵提出“机器可以思考么”
2. 1957~1970 自然语言处理领域开始形成两大阵营，基于规则、基于统计
3. 1994~1999 基于统计的方法逐渐取得胜利，概率计算开始引入到NLP领域的每个任务中
4. 2000~2008 机器学习开始兴起，迅速占据NLP主流市场
5. 2015~ 人工智能时代到来，深度学习技术深刻改变NLP

### 1.3、NLP应用场景

* 语音助手 
* 机器翻译
* 搜索引擎
* 智能问答



## 二、文本预处理

### 2.1、认识文本预处理

* 文本预处理及作用

  * 文本语料在输送给模型前一般需要一系列的预处理工作，才能符合模型输入的要求，如：将文本转化成模型需要的张量，规范张量的尺寸，而且科学的文本预处理环境还将有效指导模型超参数的选择，提升模型的评估指标

* 文本预处理中包含的主要环节

  * 文本处理的基本方法
    * 分词
    * 词性标注
    * 命名实体识别
  * 文本张量的表示方法
    * one-hot编码
    * Word2vec
    * Word Embedding
  * 文本语料的数据分析
    * 标签数量的分布
    * 句子长度分布
    * 词频统计与关键词词云
  * 文本特征处理
    * 添加n-gram特征
    * 文本长度规范
  * 文本数据增强方法
    * 回译数据增强法
  * 重要说明
    * 在实际生产应用中，我们最常使用的两种语言是中文和英文

### 2.2、文本处理的基本方法

#### 2.2.1、分词简介

* 什么是分词

  分词就是将连续的字序列按照一定的规范重新组合成词序列的过程。我们知道，在英文的行文中，单词之间是以空格作为自然分解符的，而中文只是字、句和段能通过明显的分界符来简单划界，而词没有一个形式上的分界符，分词过程就是找到这样分解符的过程

* 分词的作用

  词作为语言语义理解的最小单元，是人类理解文本语言的基础，因此也是AI解决NLP领域高阶任务，如自动问答，机器翻译，文本生成的重要基础环节

#### 2.2.2、流行中文分词工具-----jieba

* 愿景：“结巴”中文分词，做最好的Python中文分词组件

* 特性：

  * 支持多种分词模式
    * 精确模式
    * 全模式
    * 搜索引擎模式
  * 支持中文繁体分词
  * 支持用户自定义词典

* 安装

  ```
  pip install jieba
  ```

* jieba分词的使用

  * 精确模式分词

    * 试图将句子以最精确的切开，适合文本分析

    ```python
    import jieba
    
    content = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
    # 返回生成器对象
    # res = jieba.cut(content, cut_all=False)
    # lcut返回列表内容
    res = jieba.lcut(content, cut_all=False)
    print(res)
    ```

  * 全模式分词

    * 把句子中所有的可以成词的词语都扫描出来，速度非常快，但不能消除歧义

    ```python
    res = jieba.lcut(content, cut_all=True)
    print(res)
    ```

  * 搜索引擎模式

    * 在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词

    ```python
    res = jieba.lcut_for_search(content)
    print(res)
    ```

  * 中文繁体分词

    ```python
    # 繁体分词
    content1 = "煩惱即是菩提，我暫且不提"
    print(jieba.lcut(content1))
    ```

  * 使用用户自定义词典

    * 添加自定义词典后，jieba能够准确识别词典中出现的词汇，提升整体的识别准确率

    * 词典格式：每行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒

    * ```python
      云计算 5 n
      李小福 2 nr
      easy_install 3 eng
      好用 300
      韩玉赏鉴 3 nz
      八一双鹿 3 nz
      ```

      ```python
      jieba.load_userdict("./user_dict.txt")
      jieba.lcut("八一双鹿更名为八一南昌篮球队")
      ```

#### 2.2.3、流行中英文分词工具hanlp

* 中英文NLP处理工具包，基于tensorflow2.0，使用在学术界和行业中推广最先进的深度学习技术

* hanlp安装

  ```
  pip install hanlp 
  ```

* 分词

  * hanlp中文分词

  ```python
  # hanlp分词功能
  import hanlp
  
  # 中文分词
  tokenizer = hanlp.load('CTB6_CONVSEG')
  print(tokenizer("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"))
  ```

  * 英文分词

* 命名实体识别

  * 命名实体：通常我们将人名、地名、机构名等转悠名词统称命名实体

  * 命名实体识别（Named Entity Recognition，简称NER）就是识别出一段文本中可能存在的命名实体

  * 命名实体识别的作用

    * 同词汇一样，命名实体也是人类理解文本的基础单元，因此也是AI解决NLP领域高阶任务的重要基础环节

  * 实例

    * 使用hanlp进行中文命名实体识别

      ```python
      # 中文命名实体识别
      # 加载中文命名实体识别的预训练模型MSRA_NER_BERT_BASE_ZH
      recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)
      content = list("上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。")
      print(recognizer(content))
      ```

    * 使用hanlp进行英文命名实体识别

      ```python
      # 英文命名实体识别
      recognizer = hanlp.load(hanlp.pretrained.ner.CONLL03_NER_BERT_BASE_CASED_EN)
      print(recognizer(['President', 'Obama', 'is', 'speaking', 'at', 'the', 'White', 'House']))
      ```

* 词性标注

  * 词性：语言中对词的一种分类方法，以语法特征为主要依据、兼顾词汇意义对词进行划分的结果，常见的词性有14种，如名词、动词、形容词等

  * 词性标注（POS）：就是标注出一段文本中每个词汇的词性

  * ```python
    我爱自然语言处理
    我 /rr ,爱 /v, 自然语言 /n, 处理 /vn
    rr：人称代词
    v:  动词
    n:  名词
    vn: 动名词
    ```

  * 词性标注的作用

    * 词性标注以分词为基础，是对文本语言的另一个角度的理解，因此也常常成为AI解决NLP领域高阶任务的重要基础环节

  * 使用jieba进行中文词性标注

    ```python
    import jieba.posseg as pseg
    print(pseg.lcut("我爱北京天安门"))
    # 返回pair元组
    ```

  * 使用hanlp进行中文词性标注

    ```python
    tagger = hanlp.load(hanlp.pretrained.pos.CTB5_POS_RNN_FASTTEXT_ZH)
    print(tagger(['我', '的', '希望', '是', '希望', '和平']))
    ```

  * 使用hanlp进行英文词性标注

    ```python
    tagger = hanlp.load(hanlp.pretrained.pos.PTB_POS_RNN_FASTTEXT_EN)
    print(tagger(['I', 'banked', '2', 'dollars', 'in', 'a', 'bank', '.']))
    ```



### 2.3、文本张量表示方法

#### 2.3.1、了解文本张量表示

* 什么是文本张量表示
  * 将一段文本使用张量进行表示，其中一般将词汇表示成向量，称作词向量，再由各个词向量按顺序组成矩阵形成文本表示

* 例子

  ```python
  ['人生','该','如何','起头']
  # 每个词对应矩阵中的一个向量
  [[
      
  ]]
  ```

* 文本张量表示的作用
  * 将文本表示成张量（矩阵）形式，能够使语言文本可以作为计算机处理程序的输入，进行接下来一系列的解析工作
* 文本张量表示的方法
  * one-hot编码
  * Word2vec
  * Word Embedding

#### 2.3.2、one-hot词向量表示

* 又称独热编码，将每个词表示成具有n个元素的向量，这个词向量中只有一个元素是1，其他元素都是0，不同词汇元素的位置不同，其中n的大小是整个语料中不同词汇的总数

* 例子

  ```python
  ['改变'，'要','如何','起手']
  [[1,0,0,0],
   [0,1,0,0],
   [0,0,1,0],
   [0,0,0,1]]
  ```

* one-hot编码实现

  ```python
  # 导入用于对象保存和加载的包
  import joblib
  # 导入keras的词汇映射器Tokenizer
  from keras.preprocessing.text import Tokenizer
  
  # 初始化一个词汇表
  vocab = {'周杰伦', '陈奕迅', '李宗盛'}
  
  # 实例化一个词汇映射器
  t = Tokenizer(num_words=None, char_level=False)
  
  # 在映射器上拟合现有的词汇表
  t.fit_on_texts(vocab)
  
  # 遍历词汇表，将每一个单词映射为one-hot张量表示
  for token in vocab:
      # 初始化一个全零向量
      zero_list = [0] * len(vocab)
      # 使用映射器转化文本数据
      token_index = t.texts_to_sequences([token])[0][0] - 1
      # 将对应的位置赋值1
      zero_list[token_index] = 1
      print(token, "的one-hot编码为：", zero_list)
  
  # 将拟合好的映射器保存起来
  tokenizer_path = './Tokenizer'
  joblib.dump(t, tokenizer_path)
  ```

* one-hot编码器使用

  ```python
  # 加载映射器
  t = joblib.load('./Tokenizer')
  token = '李宗盛'
  # 从词汇映射器中得到index
  token_index = t.texts_to_sequences([token])[0][0] - 1
  # 初始化一个全零向量
  zero_list = [0] * 3
  zero_list[token_index] = 1
  print(token, '的one-hot编码为', zero_list)
  ```

* one-hot编码的优劣势

  * 优势：操作简单，容易理解
  * 劣势：完全割裂了词与词之间的联系，而且在大语料集下，每个向量的长度过大，占据大量内存
  * 因为one-hot编码明显的劣势，这种编码方式被应用的地方越来越少，取而代之的是稠密向量的表示方法word2vec和word embedding



#### 2.3.3、word2vec

* 什么是word2vec
  * 是一种流行的将词汇表示成向量的无监督训练方法，该过程将构建神经网络模型，将网络参数作为词汇的向量表示，它包含CBOW和skipgram两种训练模式
  
* CBOW（Continuous bag of words）模式
  * 给定一段用于训练的文本语料，再选定某段长度（窗口）作为研究对象，**使用上下文词汇预测目标词汇**
  
* skipgram模式
  * 给定一段用于训练的文本语料，再选定某段长度（窗口）作为研究对象，**使用目标词汇预测上下文词汇**

* 使用fasttext工具实现word2vec的训练和使用
  1. 获取训练数据
  
     ```python
     # 数据集
     http://mattmahoney.net/dc/enwik9.zip
     # 解压
     unzip enwik9.zip
     # 使用perl脚本提取网页中的文本数据
     perl wikifil.pl data/enwik9 > data/fil9
     ```
  
  2. 训练词向量
  
     ```python
     import fasttext
     
     # 使用fasttext的train_unsupervised(无监督训练方法)进行词向量的训练
     model = fasttext.train_unsupervised('data/fil9')
     
     # 通过get_word_vector方法来获得指定词汇的词向量
     model.get_word_vector('the')
     ```
  
  3. 模型超参数设定
  
     * fasttext.train_unsupervised(path, "skipgram", dim=300, epoch=1, lr=0.05, thread=12)
       * path：词汇文件路径
       * 无监督训练模式：skipgram/cbow
       * dim：词键入维度，默认100，随着语料库的增大，词嵌入的维度往往也要更大
       * epoch：数据循环次数，默认5
       * thread：线程数，默认12个线程
  
  4. 模型效果检测
  
     * model.get_nearest_neighbors('单词') ：查找临近单词
  
  5. 模型的保存与重加载
  
     ```python
     # 使用save_model保存模型
     model.save_model('fil9.bin')
     
     # 使用fasttext.load_model加载模型
     model = fasttext.load_model('fil9.bin')
     ```



#### 2.3.4、word embedding

* 什么是word embedding（词嵌入）
  * 通过一定的方式将词汇映射到指定维度（一般是更高维度）的空间
  * 广义的word embedding 包括所有的密集词汇向量的表示方法，如word2vec，即可认为是word embedding的一种
  * 狭义的word embedding 是指在神经网络中加入的embedding层，对整个网络进行训练的同时产生的embedding矩阵，这个矩阵就是训练过程中所有输入词汇的向量表示组成的矩阵
  
* ```python
  # 导入torch和tensorboard
  import fileinput
  import torch
  from torch.utils.tensorboard import SummaryWriter
  
  # 实例化一个写入对象
  writer = SummaryWriter()
  
  # 随机初始化一个100 * 50 的矩阵
  embedded = torch.randn(100, 50)
  
  # 导入中文词汇文件
  meta = list(map(lambda x: x.strip(), fileinput.FileInput("./vocab100.csv")))
  writer.add_embedding(embedded, metadata=meta)
  writer.close()
  
  ```



### 2.4、文本数据分析

#### 2.4.1、文本数据分析简介

* 文本数据分析的作用

  * 文本数据分析能够有效帮助我们理解数据语料，快速检查出语料可能存在的问题，并指导之后模型训练过程中一些超参数的选择
* 常用几种文本数据分析方法

  * 标签数量分布

  * 句子长度分布

  * 词频统计与关键词词云
  

#### 2.4.2、标签数量分布

* 在深度学习模型评估中，我们一般使用ACC作为评估指标，若想将ACC的基线定义在50%左右，则需要我们的正负样本比例维持在1：1左右，否则就要进行必要的数据增强或者数据删减

* ```python
    #%%
    # 文本数据分析之文本标签分布
    #%%
    # 导入包
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt
    #%%
    # 设置显示风格
    plt.style.use('fivethirtyeight')
    #%%
    # 使用pandas读取数据
    train_data = pd.read_csv('./cn_data/train.tsv', sep="\t")
    #%%
    train_data
    #%%
    # 获取训练数据标签数量分布
    sns.countplot(x='label', data=train_data)
    plt.title('train_data')
    plt.show()
    #%%
    ```

#### 2.4.3、句子长度分布

* 通过绘制句子长度分布图，可以得知我们的语料中大部分句子长度的分布范围，因为模型的输入要求为固定尺寸的张量，合理的长度范围对之后进行句子截断补齐(规范长度)起到关键的指导作用，上图中大部分句子长度的范围大致为20~250之间

* ```python
  #%%
  # 文本数据分析之句子长度分布
  #%%
  train_data['sentence_length'] = list(map(lambda x: len(x), train_data['sentence']))
  #%%
  train_data
  #%%
  # 绘制句子长度列的数量分布图
  #%%
  sns.countplot(x="sentence_length", data=train_data)
  plt.xticks([])
  plt.show()
  #%%
  # 绘制dist长度分布图
  sns.displot(train_data['sentence_length'])
  plt.xticks([])
  plt.show()
  #%%
  ```

* 通过查看正负样本长度散点图，可以有效定位异常点的出现位置，帮助我们更准确的进行人工语料审查

  ```python
  # 句子长度正负样本散点图分布绘制
  sns.stripplot(y="sentence_length", x='label', data=train_data)
  plt.show()
  ```

#### 2.4.4、词频统计与关键词词云

* 词汇总数统计

  ```python
  #%%
  # 文本数据分析之词汇总数统计
  # 导入jieba分词
  import jieba
  # 导入chain方法用于扁平化列表
  from itertools import chain
  #%%
  # 对训练集句子进行分词
  train_vocab = set(chain(*map(lambda x: jieba.lcut(x), train_data['sentence'])))
  #%%
  train_vocab
  #%%
  print("词汇总数为：", len(train_vocab))
  ```

* 根据高频形容词词云显示，我们可以对当前语料质量进行简单评估，同时对违反语料标签含义的词汇进行人工审查和修正，来保证绝大多数语料符合训练标准

  ```python
  #%%
  # 文本数据分析之正负样本高频形容词词云绘制
  #%%
  # 导入jieba分词的词性标注
  import jieba.posseg as pseg
  #%%
  # 获取形容词列表方法
  def get_a_list(text):
      """
      获取形容词列表
      :param text:
      :return:
      """
      r = []
      for g in pseg.lcut(text):
          if g.flag == 'a':
              r.append(g.word)
      return r
  #%%
  # 导入绘制词云的工具包
  from wordcloud import WordCloud
  #%%
  def get_word_cloud(keywords_list):
      """
      绘制词云
      :param keywords_list:
      :return:
      """
      wordcloud = WordCloud(font_path='./NotoSansCJK-Bold.ttc', max_words=100, background_color='white')
      keywords_string = " ".join(keywords_list)
      # 生成词云
      wordcloud.generate(keywords_string)
  
      # 绘制图像
      plt.figure()
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis('off')
      plt.show()
  
  #%%
  # 获取正样本
  p_train_data = train_data[train_data['label'] == 1]['sentence']
  #%%
  p_train_data
  #%%
  # 获取正样本形容词
  train_p_a_vocab = chain(*map(lambda x:get_a_list(x), p_train_data))
  # 绘制词云
  get_word_cloud(train_p_a_vocab)
  ```



### 2.5、文本特征处理

#### 2.5.1、文本特征处理简介

* 文本特征处理的作用
  * 文本特征处理包括为语料添加具有普适性的文本特征，如n-gram特征，以及对加入特征之后的文本语料进行必要的处理，如长度规范，这些特征处理工作能够有效的将重要的文本特征加入模型训练中，增强模型评估指标
* 常见的文本特征处理方法
  * 添加n-gram特征
  * 文本长度规范

#### 2.5.2、n-gram特征

* 什么是n-gram特征
  * 给定一段文本序列，其中n个词或字的相邻共现特征即n-gram特征，常用的n-gram特征是bi-gram和tri-gram特征，n对应2,3

* 提取方法

  ```python
  #%%
  # 文本特征处理之n-gram特征提取
  #%%
  def create_ngram_set(input_list, ngram_range):
      """
      从数值列表中提取n-gram特征
      :param input_list: 数值列表
      :param ngram_range: n
      :return:
      """
      return set(zip(*[input_list[i:] for i in range(ngram_range)]))
  #%%
  # 测试
  input_list = [1, 3, 2, 1, 5, 3]
  res = create_ngram_set(input_list, 2)
  print(res)
  ```



#### 2.5.3、文本长度规范

* 文本长度规范及其作用
  * 一般模型的输入需要等尺寸大小的矩阵，因此在进入模型前需要对每条文本数值映射后的长度进行规范，此时将根据句子长度分布分析出覆盖绝大多数文本的合理长度，对超长文本进行截断，对不足文本进行补齐（一般使用数字0），这个过程就是文本长度规范
* 文本长度规范的实现

```python
from keras.preprocessing import sequence
def padding(x_train, cutlen):
    """
    对输入文本张量进行长度规范
    :param x_train:
    :param cutlen:
    :return:
    """
    return sequence.pad_sequences(x_train, cutlen)
x_train = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5]]
res = padding(x_train, 10)
print(res)
```

```python
# 文本特征处理之文本长度规范
def padding(x_train, cutlen):
    datas = []
    for i in x_train:
        data = i
        if len(data) > cutlen:
            data = data[len(data) - cutlen:]
        elif len(data) < cutlen:
            data = [0 for i in range(cutlen - len(data))] + data
        datas.append(data)
    return data
```



### 2.6、文本数据增强

#### 2.6.1、文本数据增强的作用

* 常见的文本数据增强方法
  * 回译数据增强法

#### 2.6.2、回译数据增强

* 什么是回译数据增强法

  * 回译数据增强目前是文本数据增强方面效果较好的增强方法，一般基于google翻译接口，将文本数据翻译成另外一种语言（一般选择小语种），之后再翻译回原语言，即可认为得到与原语料同标签的新语料，新语料加入到原数据集中即可认为是对原数据集数据增强

* 回译数据增强优势

  * 操作简便，获得新语料质量高

* 回译数据增强存在的问题

  * 在短文本回译过程中，新语料与原语料可能存在很高的重复率，并不能有效增大样本的特征空间

* 高重复率解决办法

  * 进行连续的多语言翻译，如 中文->韩文->日文->中文，根据经验，最多只采用3次连续翻译，更多的翻译次数将产生效率低下，语义失真等问题

* 代码实现

  ```python
  #%%
  # 文本数据增强之回译数据增强法
  #%%
  datas = ['酒店设施非常不错','这家价格很便宜','拖鞋都发霉了，太差了','电视不好用，没有看到足球']
  #%%
  # 导入google翻译接口
  from googletrans import Translator
  #%%
  # 实例化翻译对象
  proxies = {'http': '127.0.0.1:10809'}
  translator = Translator()
  #%%
  # 进行翻译，目标韩语
  translations = translator.translate(datas,dest='ko')
  #%%
  # 获取翻译后的结果
  ko_res = list(map(lambda  x: x.text, translations))
  print("中间翻译结果：", ko_res)
  #%%
  # 翻译回中文
  translations = translator.translate(ko_res, dest='zh-cn')
  cn_res = list(map(lambda x:x.text, translations))
  print("回译结果：", cn_res)
  ```
  

#### 2.7、案例：新闻主题分类任务

* 获取新闻数据集合

* 实现步骤

  * 构建带有Embedding层的文本分类模型

    ```python
    class TextSentiment(nn.Module):
        """
        文本分类模型
        """
    
        def __init__(self, vocab_size, embed_dim, num_class):
            """
            初始化
            :param vocab_size: 语料包含的不同词汇总数
            :param embed_dim: 指定词嵌入的维度
            :param num_class: 文本分类的类别总数
            """
            super().__init__()
            # 实例化embedding层
            self.embedding = nn.Embedding(vocab_size, embed_dim, sparse=True)
            # 线性层
            self.fc = nn.Linear(embed_dim, num_class)
            # 初始化权重
            self.init_weights()
    
        def init_weights(self):
            """初始化权重函数"""
            # 初始权重取值范围
            initrange = 0.5
            self.embedding.weight.data.uniform_(-initrange, initrange)
            self.fc.weight.data.uniform_(-initrange, initrange)
            # 偏置
            self.fc.bias.data.zero_()
    
        def forward(self, text):
            """
            构建网络
            :param text: 文本数值映射后的结果
            :return:
            """
            embedded = self.embedding(text)
            # 计算数据包含几组数据c
            c = embedded.size(0) // BATCH_SIZE
            # 去除不够c的数据
            embedded = embedded[:BATCH_SIZE * c]
            # 转置，增加维度
            embedded = embedded.transpose(1, 0).unsqueeze(0)
            # 平均池化
            embedded = F.avg_pool1d(embedded, kernel_size=c)
            # 返回全连接
            return self.fc(embedded[0].transpose(1, 0))
    ```
    
  * 对数据进行batch处理
  
    ```python
    def generate_batch(batch):
        """
        数据批量处理
        :param batch:
        :return:
        """
        # 从batch中获取标签张量
        label = torch.tensor([i[1] for i in batch])
        # 获取样本张量
        text = [i[0] for i in batch]
        text = torch.cat(text)
        return text, label
    ```
    
    
    
  * 构建训练与验证函数
  
    ```python
    def train(train_data_set):
        """
        模型训练方法
        :param train_data_set: 训练集数据
        :return:
        """
        # 初始化损失值和准确率
        train_loss = 0
        train_acc = 0
    
        # 生成批次数据
        data = DataLoader(train_data_set, batch_size=BATCH_SIZE, shuffle=True, collate_fn=generate_batch)
    
        # 遍历批次训练数据
        for i, (text, cls) in enumerate(data):
            # 梯度归零
            optimizer.zero_grad()
            # 获取模型输出
            output = model(text)
            # 计算损失
            loss = criterion(output, cls)
            # 累计损失
            train_loss += loss.item()
            # 反向传播
            loss.backward()
            # 参数更新
            optimizer.step()
            # 累计准确率
            train_acc += (output.argmax(1) == cls).sum().item()
    
        # 调整优化器学习率
        scheduler.step()
    
        return train_loss / len(train_data), train_acc / len(train_data)
    
    
    def valid(valid_data):
        """
        模型验证方法
        :param valid_data: 验证集数据
        :return:
        """
        test_loss = 0
        test_acc = 0
    
        data = DataLoader(valid_data, batch_size=BATCH_SIZE, collate_fn=generate_batch)
    
        for text, cls in data:
            # 验证阶段不求解梯度
            with torch.no_grad():
                # 模型输出
                output = model(text)
                # 计算损失
                loss = criterion(output, cls)
                # 累计损失
                test_loss += loss.item()
                test_acc += (output.argmax(1) == cls).sum().item()
        return test_loss / len(valid_data), test_acc / len(valid_data)
    
    ```
  
    
  
  * 进行模型训练和验证
  
    ```python
    
    def run():
        """
        开始训练
        :return:
        """
        # 训练轮次
        N_EPOCHS = 10
    
        # 训练集数据进行转换成数值张量
        train_data_value = [(torch.tensor(text_pipeline(i['text'])), label_pipline(i['label'])) for i in train_data.iloc]
    
        # 划分训练集和验证集数据
        train_len = int(len(train_data) * 0.95)
        sub_train_, sub_valid_ = random_split(train_data_value, [train_len, len(train_data) - train_len])
    
        # 开始训练
        for epoch in range(N_EPOCHS):
            # 开始时间
            start_time = time.time()
            # 训练
            train_loss, train_acc = train(sub_train_)
            valid_loss, valid_acc = valid(sub_valid_)
    
            # 计算耗时
            secs = int(time.time() - start_time)
            mins = secs / 60
            secs = secs % 60
    
            print('EPoch: %d' % (epoch + 1), " | time in %d minutes, %d seconds" % (mins, secs))
            print(f'\tLoss: {train_loss:.4f}(train)\t|\tAcc:{train_acc * 100:.1f}%(train)')
            print(f'\tLoss: {valid_loss:.4f}(valid)\t|\tAcc:{valid_acc * 100:.1f}%(valid)')
    
    
    ```
  
    
  
  * 查看embedding层嵌入的词向量
  
    ```python
    print(model.state_dict()['embedding.weight'])
    ```
  
  * 完整代码
  
    ```python
    # 导入工具包
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    # 分词器
    from torchtext.data.utils import get_tokenizer
    # 词汇表构建方法
    from torchtext.vocab import build_vocab_from_iterator
    from torch.utils.data import DataLoader
    import time
    from torch.utils.data.dataset import random_split
    import pandas as pd
    
    # 执行设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    
    def load_data():
        """
        加载数据
        :return:
        """
        train_data_frame = pd.read_csv('/home/pizm/project/py_pro/news_classify/data/train.csv',
                                       names=['label', 'title', 'content'])
        # 合并标题和内容
        train_data_frame['text'] = train_data_frame['title'] + " " + train_data_frame['content']
        train_data_frame = train_data_frame[['label', 'text']]
        return train_data_frame
    
    
    # 训练集数据
    train_data = load_data()
    
    # 数据数值化
    text_pipeline = lambda x: vocab(tokenizer(x))
    label_pipline = lambda x: int(x) - 1
    
    # 使用英文分词器
    tokenizer = get_tokenizer('basic_english')
    
    
    def yield_tokens(data_iter):
        """分词生成器"""
        for text in data_iter:
            yield tokenizer(text)
    
    
    # 词汇表
    vocab = build_vocab_from_iterator(yield_tokens(train_data['text']), specials=['<unk>'])
    vocab.set_default_index(vocab["<unk>"])
    
    
    class TextSentiment(nn.Module):
        """
        文本分类模型
        """
    
        def __init__(self, vocab_size, embed_dim, num_class):
            """
            初始化
            :param vocab_size: 语料包含的不同词汇总数
            :param embed_dim: 指定词嵌入的维度
            :param num_class: 文本分类的类别总数
            """
            super().__init__()
            # 实例化embedding层
            self.embedding = nn.Embedding(vocab_size, embed_dim, sparse=True)
            # 线性层
            self.fc = nn.Linear(embed_dim, num_class)
            # 初始化权重
            self.init_weights()
    
        def init_weights(self):
            """初始化权重函数"""
            # 初始权重取值范围
            initrange = 0.5
            self.embedding.weight.data.uniform_(-initrange, initrange)
            self.fc.weight.data.uniform_(-initrange, initrange)
            # 偏置
            self.fc.bias.data.zero_()
    
        def forward(self, text):
            """
            构建网络
            :param text: 文本数值映射后的结果
            :return:
            """
            embedded = self.embedding(text)
            # 计算数据包含几组数据c
            c = embedded.size(0) // BATCH_SIZE
            # 去除不够c的数据
            embedded = embedded[:BATCH_SIZE * c]
            # 转置，增加维度
            embedded = embedded.transpose(1, 0).unsqueeze(0)
            # 平均池化
            embedded = F.avg_pool1d(embedded, kernel_size=c)
            # 返回全连接
            return self.fc(embedded[0].transpose(1, 0))
    
    
    def get_a_model():
        """
        实例化模型
        :return:
        """
        # 获得语料词汇总数
        VOCAB_SIZE = len(vocab)
        # 词嵌入维度
        EMBED_DIM = 32
        # 获得类别总数
        NUN_CLASS = len(set(train_data['label']))
        # 实例化模型
        return TextSentiment(VOCAB_SIZE, EMBED_DIM, NUN_CLASS).to(device)
    
    
    # 模型实例化
    model = get_a_model()
    
    # 指定BATCH_SIZE的大小
    BATCH_SIZE = 16
    # 损失函数
    criterion = torch.nn.CrossEntropyLoss().to(device)
    # 优化器
    optimizer = torch.optim.SGD(model.parameters(), lr=4.0)
    # 优化器步长调节器
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 1, gamma=0.9)
    
    
    def generate_batch(batch):
        """
        数据批量处理
        :param batch:
        :return:
        """
        # 从batch中获取标签张量
        label = torch.tensor([i[1] for i in batch])
        # 获取样本张量
        text = [i[0] for i in batch]
        text = torch.cat(text)
        return text, label
    
    
    def train(train_data_set):
        """
        模型训练方法
        :param train_data_set: 训练集数据
        :return:
        """
        # 初始化损失值和准确率
        train_loss = 0
        train_acc = 0
    
        # 生成批次数据
        data = DataLoader(train_data_set, batch_size=BATCH_SIZE, shuffle=True, collate_fn=generate_batch)
    
        # 遍历批次训练数据
        for i, (text, cls) in enumerate(data):
            # 梯度归零
            optimizer.zero_grad()
            # 获取模型输出
            output = model(text)
            # 计算损失
            loss = criterion(output, cls)
            # 累计损失
            train_loss += loss.item()
            # 反向传播
            loss.backward()
            # 参数更新
            optimizer.step()
            # 累计准确率
            train_acc += (output.argmax(1) == cls).sum().item()
    
        # 调整优化器学习率
        scheduler.step()
    
        return train_loss / len(train_data), train_acc / len(train_data)
    
    
    def valid(valid_data):
        """
        模型验证方法
        :param valid_data: 验证集数据
        :return:
        """
        test_loss = 0
        test_acc = 0
    
        data = DataLoader(valid_data, batch_size=BATCH_SIZE, collate_fn=generate_batch)
    
        for text, cls in data:
            # 验证阶段不求解梯度
            with torch.no_grad():
                # 模型输出
                output = model(text)
                # 计算损失
                loss = criterion(output, cls)
                # 累计损失
                test_loss += loss.item()
                test_acc += (output.argmax(1) == cls).sum().item()
        return test_loss / len(valid_data), test_acc / len(valid_data)
    
    
    def run():
        """
        开始训练
        :return:
        """
        # 训练轮次
        N_EPOCHS = 10
    
        # 训练集数据进行转换成数值张量
        train_data_value = [(torch.tensor(text_pipeline(i['text'])), label_pipline(i['label'])) for i in train_data.iloc]
    
        # 划分训练集和验证集数据
        train_len = int(len(train_data) * 0.95)
        sub_train_, sub_valid_ = random_split(train_data_value, [train_len, len(train_data) - train_len])
    
        # 开始训练
        for epoch in range(N_EPOCHS):
            # 开始时间
            start_time = time.time()
            # 训练
            train_loss, train_acc = train(sub_train_)
            valid_loss, valid_acc = valid(sub_valid_)
    
            # 计算耗时
            secs = int(time.time() - start_time)
            mins = secs / 60
            secs = secs % 60
    
            print('EPoch: %d' % (epoch + 1), " | time in %d minutes, %d seconds" % (mins, secs))
            print(f'\tLoss: {train_loss:.4f}(train)\t|\tAcc:{train_acc * 100:.1f}%(train)')
            print(f'\tLoss: {valid_loss:.4f}(valid)\t|\tAcc:{valid_acc * 100:.1f}%(valid)')
    
    
    if __name__ == '__main__':
        run()
        print(model.state_dict()['embedding.weight'])
    ```
  
    



