def hello():
    print("hello world")

#测试

#hello()

#在study10_03.py中将当前.py作为模块导入

#作为普通执行运行，能够正常运行，但是作为模块导入，在其他程序调用hello函数，测试代码就会执行
#为了避免这种情况的关键在于：“告知”模块本身是作为程序运行还是导入到其他程序，需要用到__name__变量

#print(__name__)
#在程序运行时，__name__的值时'__main__'，而在导入的模块中，这个值就被设定为模块的名字

#为了让模块的测试代码更加好用，可以将其放置在if语句中

#定义测试方法 ,将上边的测试方法注释掉
def test():
    hello()

#如果作为程序运行，hello函数被执行

#单独定义测试方法运行
if __name__ =='__main__':
    test()
#在if语句中，进行测试
if __name__ =='__main__':
    hello()

#让模块可用
#第一种：site-packages   将本程序复制到环境变量的site-packages目录中，重命名后，可以在其他程序中直接导入
#第二种：
#   原因：1.不希望将自己的模块填满python解释器的目录；2.没有python解释器目录中存储文件的权限；3.想讲模块放在其他地方

#告诉解释器去哪里找 1.编辑sys.path,这不是通用的方法，标准的方法是在PYTHONPATH环境变量中包含模块的目录

#包
#包基本上就是另外一类模块，它能包含其他模块
#当模块存储在文件中时，包就是模块所在的目录。
#为了让Python将其作为包对待，它必须包含一个命名为__init__.py的文件（模块）

#学习模块中有什么
import copy
#1.使用dir,可以将对象的所有特性（以及模块的所有函数、类、变量等）列出
import sys
print(dir(copy))
print(dir(sys))
#__all__变量 告诉解释器从模块导入所有名字代表的含义
#使用如下导入，可以使用__all__变量中的4个函数，其他的函数，就得显式地实现，或者导入copy，使用copy.
#没有设定__all__，import *默认会导入模块中的所有不以下划线开头的全局名称
from copy import *

import copy
#help获取帮助
print(help(copy.copy))
#文档字符串
print(copy.copy.__doc__)
#查看源码所在文件
print(copy.copy.__code__)

#sys模块
#sys.argv 获取命令行参数（通过命令行调用python脚本时，在后面加上一些参数——这就是命令行参数），第1个参数是脚本名字
print(sys.argv)

import os

print(os.environ)
print(os.linesep)
print(os.sep)
print(os.urandom(5))
#注意需要将目录名称放入引号中，不然(路径中有空格)DOS就会在空格处停止下来
#打开火狐浏览器，打开百度主页
#os.system(r'E:\"application"\"Mozilla Firefox"\firefox.exe www.baidu.com')
#更好的方案，windows特有的函数
#os.startfile(r'C:\Users\Qieclipkh\AppData\Local\Google\Chrome\Application\chrome.exe')
#更好的方案 webbrowser模块的open函数
#import webbrowser
#webbrowser.open('www.baidu.com')

import fileinput #能够轻松的便利本文件的所有行
#inplace 参数，原地处理
for line in fileinput.input(inplace=False):
    print(1111111111111111111)
    line = line.rstrip()
    num = fileinput.lineno()
    print('%-40s # %2i' % line,num)


