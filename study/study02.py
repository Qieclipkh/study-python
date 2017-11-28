# python6中内建序列  1.列表；2元组；3字符串；4Unicode字符串；5buffer对象；6xrange对象

# 列表和元组
# 列表和元组的区别：列表可以修改，元组则不能

# 列表 写在方括号中，使用，分隔
me = ['changleying', '1989']
you = ['xuhaiyan', '1992']
ta = ['changxu', '221819']

print(me)

# 通用================序列====================操作
# 索引  分片  加 乘 检查某个元素是否属于序列的成员（成员资格）
# 计算序列长度 找出最大元素 最小元素的内建函数

# 索引
greeting = 'hello world'
print(greeting[0])
# 负数索引会从右边开始
print(greeting[-1])
print('hello'[1])

# 分片
tag = 'http://www.baidu.com'
print(tag[11:-4])
print(tag[7:])
print(tag[-3:])
print(tag[:4])
# 复制序列
tag2 = tag[:]
print(tag2)

# 设置步长 步长可以为负数从右边开始取
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 下边2者等价
print(numbers[0:10])
print(numbers[0:10:1])

print(numbers[0:10:2])
# 将每4个元素中的第一个提取出来
print(numbers[::4])

# 序列相加(相同类型的序列才能进行连接操作)
print([1, 2, 3] + [4, 5, 6])

# 乘法
print([1, 2, 3] * 3)
# 空列表
print([])
print([None] * 10)

# 成员资格 in运算符

print('ch' in 'changleying')
print('xu' in 'changleying')

print(40 in [1, 2, 3])

# 长度 len 最小值 min 最大值 max
numbers = [1, 2, 3]
print(len(numbers))
print(min(numbers))
print(max(numbers))

# 列表
print(list('hello'))
# list函数适用于所有的序列

# 字符串组成的列表转成字符串
print(''.join(['h', 'e', 'l', 'l']))

# 列表可以使用所有适用于序列的标准操作

# 元素赋值
x = [1, 1, 1]
x[1] = 2
print(x)
# 删除操作
del x[1]
print(x)
del x[:]
print(x)

# 分片复制
name = list('changleying')
print(name)
name[:] = list('xu')
print(name)
# 分片复制不替换原有元素插入新的元素
numbers = [1, 5]
print(numbers)
numbers[1:1] = [2, 3, 4]
print(numbers)
# 分片删除元素
numbers[1:4] = []
print(numbers)

#列表方法
lst = [1,2,3]


#在列表末尾追加新的对象
lst.append(4)
print(lst)


#统计某个元素在列表中出现的次数
x=[[1,2],1,1,[2,1,[1,2]]]
print(x.count([1,2]))


#在列表的末尾一次性追加另一个序列的多个值
a=[1,2,3]
b=[3,4,5]
a.extend(b)
#也可以使用分片赋值
#a[len(a):]=b
print(a)
#extend操作修改被扩展序列，改变了被修改序列  +操作（连接操作）返回一个新的列表


#从列表中找出某个值第一个匹配项的索引位置
names = list('changleying')
print(names.index('g'))
#print(names.index('x')) #不存在引发异常


#将对象插入到列表中
numbers = [1,2,3,4,5,6,7]
numbers.insert(3,'four')
print(numbers)
#也可以使用负片来实现
numbers[3:3]='four'


#pop方法，移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
x = [1,2,3]
print(x.pop())

#remove方法，移除列表中某个之的第一个匹配项
names = list('changleying')
names.remove('g')
print(names)

#reverse方法，将列表中的元素反转
x = [1,2,3]
x.reverse()
print(x)

#sort方法，在原位置对列表排序（改变原来的值）
x=[4,5,1,3,8,3,45,2]
x.sort()
print(x)
#不改变原列表，可以使用sorted()函数
x=[4,5,1,3,8,3,45,2]
y=sorted(x)
print(x)
print(y)


#高级排序
numbers =[5,2,7,9]
numbers.sort(reverse=True)
print(numbers)
numbers =['32','234','d','qweq']
numbers.sort(key=max)
print(numbers)






#元组
#元组也是序列，不同的是不能修改
#使用，分隔就自动创建了元组
#活着使用大括号括起来
x=1,2,3
x=(1,2,3)
#实现一个值的元组
x=1, #等价于 x=(1,)
print(x)
print(3*(40+2))

#touple函数，和list函数相似，以一个序列作为参数并把他转为元组
names = list('changleying')
tuple(names)
print(names)
print(tuple(names))

#访问
x =1,2,3
print(x[1])
print(x[1:])

