#条件、循环和其他语句
print('wo',42)#输出并不是元组

import math as foobar
x = foobar.floor(32.9)
print(x)
from math import ceil as foobar2
print(foobar2(32.3))
#序列解包或者递归解包
x,y,z=1,2,3
print(x,y,z)
phonebook = dict([('me','0359'),('you','0351'),('ta','010'),('bie','0498')])
key,value = phonebook.popitem()
print(key,value)
key,value=['2','3']
print(key,value)
*rest,a,b=[1,2,3,4]
print(*rest)

#链式赋值
x=y='ff'

#增量赋值
x=2
x+=2

#真值 布尔值 所有值都可以看作真值
#False None 所有类型的0（包括浮点型、长整数和其他类型）、空序列（字符串、列表、元组）、空字典 都为False
#True==1 False==0 这2个都返回的True
#True就是1 False就是0
print(True==1)
print(True+False+42)#返回值为43

if True ==1:
    print('asd')
elif True ==2:
    print(3)
else:
    print(1)


if 'you' in phonebook:
    print('在')
else:
    print('不在')
    
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)#注意这个返回False，值形同，但是对象不同
#is运算符是判断同一性而不是相等性
#x和y绑定在同一个列表上，而z是另一个具有相同数值和顺序的列表上

number = 4
if number>=1 and number<10:
    print('小鱼')
else:
    print('大大')
if  1<=number<10:
    print('小鱼')
#and or not
a='f'
b=''
c='c'
d = a if b else c
print(d)
#断言
age = -1
age = 9
assert age>0 and age<10,'the age must fff'

#while
x = 1
while x<10:
    print(x)
    x+=1

s = list('changleying')
for a in s:
    print(a.upper())
x=range(0,10)
for a in range(0,3):
    print(a)
dict = dict.fromkeys(('me','ta'))
print(dict)
dict['me']=12
for key in dict.values():
    print(key)
values = dict.values()
list(values).append('dd')
print(values)

for key,value in dict.items():
    print(key,value)
    
names =['me','ta','you']
ages =[12,13,14]
#zip函数将2个序列压缩在一起，返回一个元组的列表，可以处理不等长的列表(最短的序列用完为止)
y = zip(names,ages)
print(y)
for k,v in y:
    print(k,v)
for index,string in enumerate(['a','b','c']):
    print(string,index)
for index,string in enumerate(dict):
    print(string,index)

from math import sqrt

#else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
for x in range(99,0,-1):
    root = sqrt(x)
    if root == int(root):
        print(x)
        break
else:
    print('do not find it')
#列表推导式 轻量级循环
print([x*x for x in range(0,10) if x%3==0])

girls =['alice','bermce','clarice','boodasd']
boys =['chris','arnold','bob']
print('++++')
print([boy+'+'+girl for boy in boys for girl in girls if boy[0] == girl[0]])
print('++++')
letterGirls ={}
for girl in girls:
    #生成以girl首字母为key,girl为元素的列表
    #setdefault 存在给定的key,返回对应的值，不存在给定的key，则新增给定key-给定value
    letterGirls.setdefault(girl[0],[]).append(girl)
print(letterGirls)
#根据bory的首字母从组成的girl字典中获取对应的列表，然后拼接结果
print([boy+'+'+girl for boy in boys for girl in letterGirls[boy[0]]])
#如果例子中的首字母都是不同的
letterGirls2={}
boys =['chris','arnold','bob']
for girl in girls:
    letterGirls2.setdefault(girl[0],girl)
print('------')
print(letterGirls2)
print(letterGirls2['a'])
print('------')
print([boy+'+'+letterGirls2[boy[0]] for boy in boys])


#pass del exec
x=1
if x==1:
    print('===')
elif x==2:
    pass
else:
    pass

x=['hello','world']
y=x
y[1] ='python'
print(x)
print(y)
#同一个对象
print(x is y)
#输出值一样
del x
#删除x还能输出y,因为python中删除的是名称而不是值
print(y)
_locals = locals()
exec("print('hello,word')",globals(),_locals)
exec("ff=1",globals(),_locals)
print(_locals)
print(_locals['ff'])
_globals =globals()
print(eval('1+8000',_globals,_locals))