# 抽象

# 斐波那契数列（任一个数都是前2个数之和）
fids = [0, 1]
for i in range(0, 8):
    # fids.append(fids[i]+fids[i+1])
    fids.append(fids[-2] + fids[-1])
print(fids)


# 创建函数
def hello(name):
    print('hello ' + name)


hello('world')


def fids(num):
    '''
    当前函数的注释
    '''
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result



def init(labls):
    '''
    初始化语句
    '''
    #data = dict([('first',{}),('middle',{}),('last',{})])
    storge = dict.fromkeys(labls)
    for key in storge:
        storge[key] = {}
    return  storge
labls = 'first','middle','last'
storge=init(labls)
print('------')

def store(storge,full_name,labls):
    names = full_name.split()
    if(len(names)==2):
        names.insert(1,'')
    #zip返回一个元组 组成的 列表
    for label,name in zip(labls,names):
        storge[label].setdefault(name,[]).append(full_name)


store(storge,'Magnus lie Hetland',labls)
store(storge,'Robin Locksly',labls)
store(storge,'Robin hot',labls)
print(storge)
#获取中间名称为空字符串的人
print(storge[labls[1]][''])
def lookup(storge,label,name):
    return storge[label][name]
print(lookup(storge,labls[1],''))

#前边定义的函数，传递的参数都叫做位置参数，位置很重要


def hello_1(greeting,name):
    print('%s, %s!' % (greeting,name))
hello_1('hello','world')
#关键字参数,还可以在函数中给参数提供默认值
hello_1(name='world',greeting='hello')

def hello_2(greeting='hello',name='world'):
    print('%s, %s!' % (greeting,name))
hello_2(name='ffff')
#位置参数和 关键字参数 联合使用时候，将位置参数放在前边
def hello_3(name,greeting='hello',punctuation='!'):
    print('%s, %s %s' % (greeting,name,punctuation))
hello_3('chang',punctuation='!'*3)

#提供任意多的参数,参数拼装成对应多参数长度的元组
#*的意思就是‘收集剩余位置的参数’
#如果不提供参数，就是一个空元组
def print_params(*params):
    print(params)
print_params(1,'3','asd')
#关键字参数收集 使用2个*，参数为字典
def print_params_2(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
print_params_2(1,2,3,5,6,7,foo=1,boo=4)

print((5,)*2)


#作用域121
#变量和对应的值用的是个“不可见”字典，內建的var函数可以返回这个字典
# 一般来说vars返回的字典是不能修改的，官方文档说，结果是未定义的，可能得不到想要的结果
x=9000
scope = vars()
print(scope)
scope['x']
print(scope['x'])
scope['x']+=1000
print(x)

#函数内的变量被称为局部变量，与全局变量想法的概念
#如果局部变量名和全局变量名相同，全局变量会被局部变量屏蔽，如果要获取全局变量使用globals函数
x=1000000
def xx(x):
    print(x)
    print(globals()['x'])
xx(1)
print('+++++')
#重绑定全局变量（使变量引用新值）
def change_global():
    global x
    x = x+1
change_global()

print(x)
#闭包，函数里边放一个函数
def foo(x):
    def doo(y):
        #nonlocal关键字和global关键字类似，可以让内层函数对外层函数的变量进行复赋值
        nonlocal x
        x=x+4
        print(x*y)
    return doo
#将内层函数作为外层函数的返回值，但是没有被调用
x = foo(3)
print(x)
x(5)
foo(3)(5)

#递归


