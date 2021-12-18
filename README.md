# 形式语言与自动机 正则表达式->极小DFA 评测程序
## 说明
本程序的检测方式为抽样检测：对于给定正则表达式，生成的极小DFA，输入句子，判断是否可以接收：

- 非完闭检查，给定多组测试数据（正则表达式可以接收句子），如果都可以接收，则判断该DFA是正确的。
- 因为极小DFA是唯一的，对于“极小”的检查，我们只检查状态的数量。
- 给定句子，判断是否可以接收，即是否符合该正则表达式。

**本程序需要安装python3.x，如何安装请自行搜索。**

## 如何使用
### 立即开始
下载该程序，文件名为auto_machine，在该文件夹下，包含文件：

- ans.txt：存放你缩写程序输出的自动机状态转移表
- sentences.txt：待检查的句子（测试数据），可以自己设置，用来检测自己程序的正确性，第一行为最小状态的数量。
- autograde.py

进入文件夹auto_machine，打开终端，执行下面的程序：

```shell
python autograde.py
```

*[True, True, True, True, False]*

上式内容，表示给定的5个句子中，前4个句子可被正则表达式接收，最后一个句子不能被接收。



```
python autograde.py --debug=True
```

*句子1100成功接收！*
*句子100011010000000成功接收！*
*句子000010000011010成功接收！*
*句子1110100010000100000100000000010成功接收！*
*不接收，字符串读完，未停止在终止状态，当前状态为:q2 所在句子为：101011111*
*[True, True, True, True, False]*

### 自定义参数

本程序有4个参数：ans_file，sentences_file，debug，eval，默认情况下参数的值为：

- ans_file="ans.txt"
- sentences_file="sentences.txt"
- debug=False
- eval=True

你可以更改文件名，方便你的使用。例如你的文件结构为

/auto_machine

​	—autograde.py

​	—output.txt

​	—test.txt

你可以使用如下命令进行测试：

```shell
python autograde.py --ans_file="output.txt" --sentences_file="test.txt"
```

当然也支持了简写的形式：

```shell
python autograde.py -a="output.txt" -s="test.txt"
```

### 数据

创建三个文件夹为：

- 正则表达式：re
- 极小自动机：ans
- 测试数据（句子）：sentences

文件夹内存放我们检查的数据，命名格式为：

re_1.txt，ans_1.txt, sentences_1.txt

