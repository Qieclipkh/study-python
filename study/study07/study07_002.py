_metaclass_ = type



class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return  self.name
    def greet(self):
        print('Hello, world!I\'m %s' % self.name)

foo = Person()
bar = Person()

foo.setName("chang")
bar.setName("xu")

foo.greet()
bar.greet()

#self的作用，将自己作为第一个参数传入函数中
#foo是Person的实例，foo.great()可以看作是Person.greet(foo)方便的简写


