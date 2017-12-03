#魔法方法、属性和迭代器

#构造方法
class Foobar:
    #将init方法修改为魔法版本__init__既是构造方法
    def __init__(self):
        self.somevar =43
f = Foobar()
print(f.somevar)

#如果一个类的构造方法被重写，那么就需要调用超类（你所继承的类）的构造方法，否则对象可能不会正确地初始化
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaaah...')
            self.hungry = False
        else:
            print('No, thanks')
class SongBird(Bird):
    def __init__(self):
        self.sount = "Squawk"
    def sing(self):
        print(self.sount)

sb = SongBird()
sb.sing()

#因为SongBird是Bird的一个子类，它继承了eat方法，它调用eat方法，就会产生问题，不存在hungry属性
#原因是：在SongBird中，构造方法被重写，但新的构造方法没有任何关于初始化hungry特性的代码
#       为了达到预期效果，SongBird的构造方法必须调用其超类Bird的构造方法以完成hungry的初始化（2种办法）
#第一种：调用未绑定的超类构造方法
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)  #这就是
        self.sount = "Squawk"
    def sing(self):
        print(self.sount)
sb = SongBird()
sb.eat()
sb.eat()
#说明：调用一个实例的方法是，该方法的self参数会被自动绑定到实例上（这称为绑定方法），
#     但如果直接调用类的方法（比如Bird.__init__(self)），那么久没有实例会被绑定。这样就可以自由的提供所需要的self参数，这样的方法被称为未绑定方法

#第二种:super函数
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaaah...')
            self.hungry = False
        else:
            print('No, thanks')
    def ff(self):
        print('ff')
class SongBird(Bird):
    def __init__(self):
        print(super(SongBird,self).ff())
        super(SongBird,self).__init__() #这就是
        self.sount = "Squawk"
    def sing(self):
        print(self.sount)
print('------')
sb = SongBird()
sb.eat()
sb.eat()
#super函数：（可以假装他返回的是所需的超类）实际上它返回了一个super对象，这个对象负责进行方法解析。当对其特性进行访问时，
#       它会查找所有的超类（以及超类的超类），直到找到所需的特性为止（或者引发一个AttributedError异常）

#成员访问

#创建自己的算式序列
def checkIndex(key):
    """
    键是个整数，否则抛出TypeError，键如果是负数，则抛出IndexError
    因为键是无限长的，所以不判断上限
    :param key:
    :return:
    """
    #if not isinstance(key,(int,其他类型)):raise TypeError
    if not isinstance(key,int):raise TypeError
    if key<0:  raise IndexError

class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        """
        初始化算术序列
        :param start: 序列中的第一个值
        :param step: 2个相邻值之间的差别
        """
        self.start = start
        self.step = step
        self.changed={}
    def __getitem__(self, key):
        """
        获取对应下标的值
        :param item:
        :return:
        """
        try:
            return self.changed[key]
        except KeyError:
            #没有对应，则计算值
            return self.start+key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value
    def __delitem__(self, key):
        checkIndex(key)
        try:
            del self.changed[key]
        except:
            pass
        
s =ArithmeticSequence(1,2)
print(s[4])
s[4] = 2
s[5] = 30
print(s.changed)
print('1121212')
del s[5]
print(s.changed)

#更简单的定义自己的序列
#继承。子类化列表，字段和字符串

class   CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter = 0;
    def __getitem__(self, index):
        self.counter +=1
        return super(CounterList,self).__getitem__(index)
cl = CounterList(range(10))
#可以调用list的很多方法
print(cl)
cl.reverse()
print(cl)


#属性

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def getSize(self):
        return self.width,self.height
    def setSize(self,size):
        self.width,self.height = size
        
r = Rectangle()
r.width=10
r.height=5
print(r.getSize())
r.setSize((20,10))
print(r.getSize())

#更简单的
#property函数
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def getSize(self):
        print(111,self.__dict__)
        return self.width,self.height
    def setSize(self,size):
        self.width,self.height = size
    size = property(getSize,setSize)
#property函数创建了一个属性，其中访问器函数被用作参数（先是取值，再试赋值）
r = Rectangle()
r.width =100
r.height=50
print(r.size)
r.size=(200,100)
print(r.size)
#size特性仍然取决于getSize、setSize的计算，但是看起来就像普通的属性一样
#roperty函数可以传递0、1、3或者4个参数来调用，如果没有参数，产生的属性既不是可读，也不是可写，
#   如果一个参数调用（一个取值方法）产生的属性是只读的
#   第3个参数（可选）是一个用于删除特性的方法（它不要参数）
#   第4个参数（可选）是一个文档字符串
# 4个参数分别叫fget、fset、fdel、doc  可以使用关键字参数的方式来实现

#静态方法和类成员方法
class MyClass:
    def smeth():
        print('this is a static method')
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print('this is a Class method'),cls
    cmeth = classmethod(cmeth)
    
MyClass.smeth()
MyClass.cmeth()
#没有实例化直接调用
class MyClass:
    @staticmethod
    def smeth():
        print('this is a static method')
    @classmethod
    def cmeth(cls):
        print('this is a Class method'), cls
#或者使用@操作符 （装饰器语法）

#__getattr__  __setattr__   错误还的研究下
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def __getattr__(self, name):
#         print('__getattr__')
#         if name == 'size':
#             return self.width,self.height
#         else:
#             return self.__dict__[name]
#     def __setattr__(self, name, size):
#         print('__setattr__')
#         if name == 'size':
#             self.width,self.height = size
#         else:
#             raise AttributeError
#     def getSize(self):
#         print(111,self.__dict__)
#         return self.width,self.height
#     def setSize(self,size):
#         self.width,self.height = size
#
#     size = property(getSize,setSize)
# r = Rectangle()
# r.size = 300,150
# print(r.size)


#迭代器
#只要对象实行了__iter__方法，就能对其进行迭代。__iter__方法会返回一个迭代器（iterator）,所谓的迭代器就是具有next方法
#在py3中，迭代对象应该实行__next__方法，而內建函数next可以访问这个方法
class Fids:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
#正式的说法是，一个实现了__iter__方法的对象是可迭代的，一个实现了__next__方法的对象则是迭代器
fids = Fids()
#去查找在菲波那切数列中比1000大的数中最小的数
for f in fids:
    if f>1000:
        print(f)
        break
#內建函数iter可以从迭代对象中获得迭代器
it = iter([1,2,3])
print(next(it))
print('迭代Fids实例')
fids = Fids()
it = iter(fids)
print(next(it))

#使用list构造器显式地将迭代器转换为列表
class TestIterator:
    value = 0
    def __next__(self):
        self.value +=1
        if self.value>10:raise  StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))


#生成器 这个下来的认真在看一次 yield
