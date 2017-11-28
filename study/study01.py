#基础知识
# 普通除法
print(1 / 2)
# 执行整除
print(1 // 2)
# 乘方运算  比取反（一元运算符）优先级高
print(-3 ** 2)  # 相当于-(3**2)

#变量 变量名可以包括字母 数字和下划线,不能以数字开头
x =3

print(x)
# input("you age is ")
#
# x = input("x:")

#函数
#幂运算函数
x = pow(2,3)
print(x)
# 绝对值
x= abs(-10)
print(x)
#四舍五入运算 取最接近的整数值
print(round(3/2))

import  math
print(math.floor(32.9))


from math import sqrt
#计算平方根
print(sqrt(4))
#print(sqrt(-1)) #ValueError: math domain error
#导入cmath模块 可以执行负数的平方根为虚数
import  cmath
print(cmath.sqrt(-1)) #输出1j

#字符串
#双引号和单引号 没有区别
print('hello world')
print("hello world")
print("let's go")
print('let\'s go')
#字符串拼接

print("let's say" '" hello world!"')

x="hello"
y='world'
print(x+' '+y)

#字符串表示 将值转为字符串 str repx ``(反引号 python3不支持)
print(str("hello world"))
print(repr(10000))

#长字符串 原始字符串和Unicode
#最后一个字符\将换行符转义了
print('''this is a very \
very long string''')
#原始字符串可以放入任何字符，基本正确  原始字符最后一个字符不能为\
print(r'e:\application')
print(r'let\'s go')
#Unicode 以u开头
print(u'hello world')