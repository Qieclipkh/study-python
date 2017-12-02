#更加抽象
#多态
#参数是支持加法的对象,都可以使用operater模块的add方法
import operator
print(operator.add(1,2))
print(operator.add('changle','le'))

#封装
#继承

#创建自己的类，参考study07_002

#特性、函数和方法
class Class:
    def method(self):
        print('I hava a self')
def function():
    print('I don\'t...')
instance =Class()
instance.method()
instance.method = function
instance.method()

instance.ff =function
instance.method()
#self参数并不依赖于调用方法的方式，前面使用的是instance.method(实例.方法)的形式，
#可以随意使用其他变量引用同一个方法

instance = Class()
instance2 = instance.method
instance2()
#instance2()看起来与函数调用十分相似，便是变量instance2引用绑定方法上，也就意味着还是对self参数进行访问

#私有化
class Secretice:
    def __inaccessible(self):
        print('Bet you can not see me...')
    def accessible(self):
        print("The secretice message is:")
        self.__inaccessible()
    def _accessible(self):
        print("The secretice message is:")
        self.__inaccessible()


s = Secretice()
#s.__inaccessible() 从外界是无法访问的，而在类内部还能使用
s.accessible()
#在方法和特性前边加上双下划线使其变为私有,外界是无法访问的，而在类内部还能使用
#在类的内部定义中，所有以双下划线开始的名字都被“翻译”成前面加上单下划线和类名的形式,可以使用这个方法名字使用该方法
s._Secretice__inaccessible()
#前面带有下划线的名字不会被带星号的import语句导入


#类的命名空间

#所有位于class语句中的代码都在特殊的命名空间中执行——类命名空间
class C:
    print("class C being defined...")


#指定超类
class Filter():
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if  x not in self.blocked]

class SPAMFilter(Filter): #SPAMFilter是Filter的子类
    def init(self): #重写超类中的init方法
        self.blocked=['SPAM']

f = Filter()
f.init()
result = f.filter([1,2,3])
print(result)



s = SPAMFilter()
s.init()
result = s.filter(['SPAM','SPAM','EGGS','BACON','SPAM'])
print(result)

#检查继承
#使用內建的issubclass函数，查看一个类是否另一个类的子类
print(issubclass(SPAMFilter,Filter))
#获取已知类的基类（们），使用它的特殊特性__bases__
print(SPAMFilter.__bases__)
#isinstance方法检查一个对象是否是一个类的实例
s = SPAMFilter()
print(isinstance(s,SPAMFilter))
#__class__ 知道一个对象属于哪一个类
print(s.__class__)

#多个超类 多重继承
class Calualator:
    def calualate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print("hi,My values is ",self.value)

class TalkingCalualator(Calualator,Talker):
    pass
#
tc = TalkingCalualator()
tc.calualate('1+2*3')
tc.talk()
#注意超类的顺序，先继承的类中的方法会重写后继承类中同名方法

#接口和内省
#检查对象tc是否有叫做talk的特性（包含一个方法）
print(hasattr(tc,'talk'))
print(hasattr(tc,'fnord'))
#检查talk特性是否可调用
print(callable(getattr(tc,'talk',None)))
print(tc.__dict__)