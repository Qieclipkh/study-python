#字典  键唯一,值并不唯一
#字典的创建
phonebook = {"me":"0359","you":"0351","ta":"010","bie":"0499"}
print(phonebook)
#dict函数创建字典
phonebook = dict([('me','0359'),('you','0351'),('ta','010'),('bie','0498')])
print(phonebook)
print(dict(name='chang',age=42))

#基本字典操作
print(len(phonebook))
print(phonebook['ta'])
phonebook['ta']=399
print(phonebook)
del phonebook['you']
print(phonebook)
print('bie' in phonebook)

#字典格式化字符串
print("me's phone numbe is %(me)s" % phonebook)









#字典方法
#1.clear 清楚字典中所有的项
#2.copy 返回一个具有相同键-值对的新字典(实现的是浅复制,而不是副本)
#替换时候原始字典不受影响,但是修改了值(原地修改,而不是替换),原始字典也会改变,因为同样的值也存在原字典中
#3.deepcopy 深层复制
from copy import deepcopy
#4.fromkeys 使用给定的键建立新的字典,每个键对应的值为None
print({}.fromkeys(['join','ff']))
print(dict.fromkeys(['miss','mir']))
#5.get 访问字典不存在的键会返回None,或者设置个默认值
#6.has_key(python3没有这个函数) 检查字典中是否含有给定的键 相当于 k in d
#7.items 将字典中所有的项已列表形式返回,列表的每个项都来自于(键,值)(元组),但没有特定的顺序
print(phonebook.items())
#8.keys 将字典中的键以列表形式返回
print(phonebook.keys())
#9pop 用来获得对应于给定键的值,然后将这个键从字典中移除
#10.popitem 弹出随机项
phonebook.popitem()
#11.setdefault 获得给定键的值,如果没有,则设定相应的值
phonebook.setdefault('chang')
print(phonebook)
#12.update 利用一个字典更新另一个字典
#提供的字典中的项会添加的旧的字典,存在则覆盖
#13.values 以列表的形式返回字典中的值
print(phonebook.values())