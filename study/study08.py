#异常

#print(1/0)如果异常对象并未被处理或捕捉，程序就会用所谓的回溯（Traceback，一种错误信息）终止执行

#异常可以在某些东西出错时自动引发。为了引发异常有两种方式：
#1.使用一个类，应该是Excepion的子类（使用类时，程序会自动创建类的一个实例）raise  Exception('我的错误')
#2.实例参数调用raise语句。 raise  Exception

#內建异常都可以在exceptions模块(py3没有这个模块)（和內建的命名空间中）找到

import math
#使用dir函数列出模块中的内容
print(dir(math))

#自定义异常类，确保从Exception继承
class MyError(Exception):
    pass

#捕捉异常
try:
    print(1/0)
except ZeroDivisionError:
    print("被除数不能为0")
    #raise
    
#使用不带参数的raise将异常抛出（传递异常，不进行处理）
#except 可以使用多个处理不同的异常，也可以用一个快捕捉多个异常
#
except(ZeroDivisionError,NameError,TypeError):
    print('多个异常')

#捕捉对象
#except子句中访问异常对象本身
try:
    1/0
except(ZeroDivisionError,TypeError) as e:#py2写作 except(Exception),e
    print('+++')
    print(e)

#捕捉所有的异常
try:
    1/0
except:
    print('可以做任何事情了')
#exception中忽略所有异常
#这样危险，会隐藏所有的错误，同样会捕捉用户终止的Ctrl+c命令以及用Sys.exit函数终止程序的企图
try:
    1/0
except Exception as e:
    print(1)

#没有异常时候执行一段代码使用else
try:
    1/1
except Exception as e:
    print(e)
else:
    print('没有发生异常')

#finally （py2 finally需要单独使用）
try:
    1/0
except ZeroDivisionError as e:
    print(e)
else:
    print('正确运行了')
finally:
    print('无论何时都执行')


def describePerson(person):
    print("Description of",person['name'])
    print("Age:",person['age'])
    if 'occupation' in person:
        print("Occupation:",person['occupation'])

person = {'name':'常乐盈','age':30}
describePerson(person)
person['occupation']='java'
describePerson(person)
#代码非常直观但是效率不高，程序2次查询'occupation'键，一次检查，一次取值
#解决方案
def describePerson(person):
    print("Description of",person['name'])
    print("Age:",person['age'])
    try:
        print("Occupation: "+person['occupation'])
    except KeyError:
        pass
#注意：打印职业的时候使用加号而不是逗号。否则字符串"Occupation:"在异常引发之前就会被输出
person = {'name':'常乐盈','age':30}
describePerson(person)

#在很多情况下使用try/except语句比if/else会更自然一些，应该养成尽可能使用try/except的习惯
#“请求宽恕易于请求许可”