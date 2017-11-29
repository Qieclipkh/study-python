#使用字符串
#所有标准的序列操作(索引,分片,乘法,成员资格,长度,最大值,最小值)对字符串适用
#但是由于字符串是不可变的,所以分片复制是不合法的

#字符串格式化
format = 'hello %s,%s enough for ya?'
#只有元组和字典能格式化一个以上的值,列表会解释成一个值
values = ('world',"hot")
print(format % values)
format = 'pi的值为 %.3f'#f 浮点数:一个句点在加上希望保留的小数位数
from  math import pi
print(format % pi)
#string模块提供另外一种格式化方法
from  string import Template
s = Template('$name is me')
print(s.safe_substitute(name='changle'))
#使用字典格式化
zidian={}
zidian['name'] = 'chang'
zidian['age'] = 200
s = Template('$name is me,age is $age')
print(s.substitute(zidian))
#safe_substitute() 不会因为缺少值或者不正确引用$出错
#字段宽度是5
print('age is:%5d' % 4)
#字段宽度是5,保留3位小数,使用.分隔
print('age is:%5.3f' % pi)
print('%.4s' % 'me is chang')
#*从元组中获取精度或者长度
print('%.*s' % (7,'me is chang'))
#字段宽度为10,精度为3,使用0补充(也可以是空格)
print('%010.3f' % pi)
#-用来左对齐,+用来不管是整数还是负数都标书出符号
print('%-10.3f' % pi)
print('%+10.3f' % -pi)

#字符串方法
import  string
#包含1-9的字符串
print(string.digits)
#包含所有小写和大写的字符串
print(string.ascii_letters)
#包含小写的字符串
print(string.ascii_lowercase)
#包含大写的字符串
print(string.ascii_uppercase)
#包含所有可打印字符的字符串
print(string.printable)
#包含所有标点的字符串

print(string.punctuation)
#find方法,在一个较长字符串查找子字符串,返回子串所在位置最左端的索引,没有找到返回-1
print('this is long string'.find('on'))
#还可以提供起始和结束点
print('this is long string'.find('on',10,16))

#split方法,将字符串分割成序列,不提供分隔符,将空格作为分割符(空格,制表,换行)
print('1+2+3+4+5'.split('+'))

#join方法,需要添加的元素必须是字符串
dirs = '','user','bin','env'
print(dirs)
print('/'.join(dirs))

#lower方法,返回字符串的小写字母版
print('Chang LE'.lower())

#replace方法,返回某字符串的所有匹配项均被替换之后的字符串
print('this is my python'.replace('is','eez'))

#strip方法,返回去除两侧(不包括内部)空格的字符串,也可以指定去除的字符
print('   this is ff   '.strip())

#translate方法,替换字符串中的某些部分,只处理单个字符; 第2个参数指定删除的字符
#穿件字符映射转换表,python2中是string.maketrans("cs",'kz')
table = str.maketrans("cs",'kz')
print('this is an inccddff'.translate(table))
