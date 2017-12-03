#集合、堆和双端队列
#1.集合（Set）位于sets模块中
s = set(range(10))
print(s)
#和字典一样，集合元素的顺序是随意的
#集合是可变的，所以不能用做字典中的键，本身只能包含不可变（可散列）值，所以就不能包含其他集合
#frozenset类型，用于代表不可变的集合，就可以将集合作为其他集合的成员还是字典的值
a = set()
b = set()
#a.add(b) #报错
a.add(frozenset(b))
print(a)


#2.堆  优先队列的一种。使用优先队列能够以任意顺序增加对象，并且能在任何时间找到最小的元素，也就是说比用于列表的min方法要有效率
#必须将列表作为堆对象本身

from heapq import *
from random import shuffle

data = list(range(0,10))
shuffle(data)
heap =[]
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)
#元素的顺序并不像看起来那么随意。虽然不是严格排序，但是也有规则：
#   位于i位置上的元素总比i/2位置处的元素大（反过来说就是i位置处的元素总比2*i以及2*i+1位置处的元素小）。这是底层堆算法的基础，而这个特性称为堆属性
#heappop函数弹出最小的元素，一般来说都是在索引0处的元素，并且会确保剩余元素中最小的那个占据这个位置（保持上边提到的堆属性）。
#   一般来说，尽管弹出列表的第一个元素并不是很有效率，但是在这里不是问题，因为heappop在“幕后”会做一些精巧的移位操作
print(heappop(heap))
print(heap)

heap = [5,8,3,0,6,7,9,1,4,2]
heapify(heap) #用任意列表作为参数，并且通过尽可能少的移位操作，将其转换为合法的堆
print(heap)

heapreplace(heap,0.5)  #弹出最小元素，并且将新元素 推入

print(heap)

#可迭代对象中第n大元素
b = nlargest(2,heap)
print(b)
print(heap)

#可迭代对象中第n小元素
b = nsmallest(2,heap)
print(b)
print(heap)


#3.双端队列 deque
#在需要按照元素增加的顺序来移除元素时非常有用
from collections import  deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)

print(q.pop())

print(q.popleft())

print(q)
#右移3位
q.rotate(3)
print(q)
#左移1位
q.rotate(-1)
print(q)

#4.time模块
import  time
#将时间元组转换为字符串
print(time.asctime())
#将秒数转换为日期元组，以本地时间为准
print(time.localtime())
#mktime 将时间元组转换为本地时间

#休眠
#time.sleep(10)
#将字符串解析为时间元组
#当前时间 新纪元开始后的秒数，以UTC为准
print(time.time())

#5.random 包含随机数的函数
#6.shelve 简单的存储方案
import shelve
s = shelve.open("test.dat")
s['x']=['a','b','c']
s['x'].append('d')
print(s['x'])#看不见d,原因；在shelf对象中查找元素的时候，这个对象都会根据已经存储的版本进行重新构建，当将元素赋给某个键的时候，它就被存储了
#所以s['x'].append('d')中的s['x']在一个新的副本中，d被添加到这个副本中了

tmp = s['x']
tmp.append('d')
s['x'] = tmp
print(s['x'])
s.close()

#还有第二种方案，将open函数的writeback参数设为True
s = shelve.open("test.dat",writeback=True)

#7.re模块包含对正则表达式的支持
