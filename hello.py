#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#examle
print("hello world")
print("2的10次方为%d" % (2**10))
print("{0:*^10}".format(10))
print('my name is {1} ,age {0} {1}'.format(20,'Xjoon'))
##一、python基础
#数据类型
	#整  数：分为正整数和负整数，例如：10进制--1,100,-8080,0等等。十六进制--0xff00,0x123456789abcdef。
	#浮点数：不解释，例如：1.23，-9.01，1.23e8=12.3e7,0.000012=1.2e-5=12.e-6。
	#字符串：单引号或双引号括起来的任意文本。"I'm OK"，"I'm \"OK\"",r"I'm "OK"，转义符\:\t \\ \n。'''可换行的字符串内容'''。
	#布尔值：True，False，注意区分大小写。and or not 运算符。
	#空  值：用None表示，注意与0区分，0是有意义的。
	#变  量：变量名称必须是大小写英文、数字和_的组合，并且不能用数字开通，避开关键字。
'''		   执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
		   执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC'：
		   执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：
		   所以，最后打印变量b的结果自然是'ABC'了。
'''
	#常  量：所谓常量就是不能变的变量。在Python中，通常用全部大写的变量名表示常量：如：PI=3.14159265359。
	#解释一下整数的除法为什么是精确的：10/3=3.33333333333335，10//3=3，10%3=1。（//地板除，商永远是直接取整数）
#字符编码：ASCII,Unicode,UTF-8
'''    字符      ASCII 				Unicode	               UTF-8
	    A        01000001           00000000 01000001      01000001
	   中        x                  01001110 00101101      11100100 10111000 10101101
	python3中的字符串是以Unicode编码的，也就是说，Python的字符串支持多语言。'\u4e2d\u6587'==='中文'。
	Python对bytes类型的数据用带b前缀的单引号或双引号表示：x = b'ABC'。
'''
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))
#b'ABC'
print('中文'.encode('utf-8'))
#b'\xe4\xb8\xad\xe6\x96\x87'
#pirnt('中文'.encode('ascii'))会报错
#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))#-->'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))#-->'中文'
#如果bytes中包含无法解码的字节，decode()方法会报错：如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))#-->'中'
#len()函数计算的是字符串的字符数。
print(len(b'ABC'))#-->3
print(len('中文'))#-->2
print(len('中文'.encode('utf-8')))#-->6
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))#-->6
print(u'中文测试正常')
#格式化：%d->整数，%f->浮点数，%s->字符串，%x->十六进制整数。
print('Hi, %s, you have $%d.' % ('Michael', 1000000))#-->"Hi, Michael, you have $1000000."
print('%2d-%02d' % (3, 1))#-->" 3-01"
print('%.2f' % 3.1415926)#-->"3.14"
#%s永远起作用，它会把任何数据类型转换为字符串：%%转义%.
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125))#-->'Hello, 小明, 成绩提升了 17.12%'
s1 = 72
s2 = 85
s3=(s2-s1)/s1*100
print('小明的成绩提升了%.1f%%' % s3)
#list可变的有序列表，[]表示;在末尾追加：l1.append('A')；指定位置：l1.insert(2,'B');删除末尾：l1.pop(),删除指定元素：l1.pop(2);l1.sort():升序排列。
l1=[1,2,'a',[1,2]]
l2=[]
l3=[1]
print(l1[3][1])#-->2
print(len(l2))#-->0
print(l1[-1],l1[-2])#-->[1,2] a
print(type(l3))#--><class 'list'>
#tuple不可变的有序列表叫元组，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用t1[0]，t2[-1],
#但不能赋值成另外的元素。当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。
t1=()#空的tuple
t2=(1,)#单元素tuple
t3=('a', 'b', ['A', 'B'])#多元素tuple
t3[2][0]='X'
t3[2][1]='Y'
print(t3)#-->('a', 'b', ['X', 'Y'])
#注意：tuple不可变，指的是“指向不变”，即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#条件判断：if x:只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
h=1.75
w=80.5
#h=input('请输入身高：(单位m)')
#w=input('请输入体重：(单位kg)')
H=float(h)
W=float(w)
BIM=W/H**2
print('您的BIM指数是：',BIM)
if BIM<18.5:
    print('您的体重过轻！')
elif 18.5<=BIM<25:
    print('您的体重正常，请保持！')
elif 25<=BIM<28:
    print('您的体重过重，有点微胖哦！')
elif 28<=BIM<32:
    print('您的体重超重了，名副其实的小胖子！')
else :
    print('emmm....大胖子，说的就是你！')
#循环1：利用for...in...循环求1+2+……100的和：
sum = 0
for x in range(101):#list()函数可以将range()结果变成list，tuple()同理。
	sum = sum+x
print(sum)
print(range(4))#-->range(0,4),代表0-3的序列
print(type(range(4)))#--><class 'range'>
print(tuple(range(4)))#-->(0，1，2，3)
#循环2：使用while循环求range(101)中，前11个数中偶数的和：
n = 0
sum1 = 0
t = tuple(range(101))
while n <= len(t):
	n = n + 1
	if n > 10:
		break
	if t[n] % 2 != 0:
		continue
	sum1 =sum1 + t[n]
print(sum1)
#字典dict，无序键值对:全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'A':1,'B':2,'C':3}
print(d['A'])#-->1（print(d['D']),会报错。）
d['C']=4
if 'C' in d:
	print(d['C'])#-->4
print(d.get('C'))#-->4(如果'C'不在字典中，返回Nome或指定值：d.get('D',-1)
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('B')
print(d)#-->{'A': 1, 'C': 4}
'''
和list比较，dict有以下几个特点：
	查找和插入的速度极快，不会随着key的增加而变慢；
	需要占用大量的内存，内存浪费多。
而list相反：
	查找和插入的时间随着元素的增加而增加；
	占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''
#集合set：与dict类似，也是一组key的集合，但不存储value。key不重复。创建set需要一个list作为输入集合:s1=set([1,2]);s1=set((1,2));s1=set({1,2});s1=set{1,2};"s1=set{(1,2)}"。
s1 = set([1,2,3,3])#重复的元素自动被过滤掉
print(s1)#-->{1,2,3}
print(type(s1))#--><class 'set'>
s1.add(5)
s1.add(5)#重复执行，无意义。
print(s1)#-->{1, 2, 3, 5}
s1.remove(3)
print(s1)#-->{1, 2, 5}
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s2 = set([2, 3, 4])
print(s1 | s2)#-->{1, 2, 3, 4, 5}
print(s1 & s2)#-->{2}
dict1 = {(1,2,3)}
print(dict1)#-->{(1,2,3)}
print(len(dict1))#-->1
print(type(dict1))#--><class 'set'>
# dict2 = {(1,[2,3])}#-->TypeError: unhashable type: 'list'
# print(dict2)
# dict3 = dict1 = {(1,2,3),{1,2}}
# print(dict3)#-->#-->TypeError: unhashable type: 'set'
# dict4 = {{1,2,3}}
# print(dict4)#-->TypeError: unhashable type: 'set'
set1 = set((1,2,3))
print(set1)#-->{1,2,3}
# set2 = set((1,[2,3]))#-->TypeError: unhashable type: 'list'
# print(set2)
set3 = set({1,2,3})
print(set3)#-->{1,2,3}
set4 = {1,2,3,4}
print(set4)#-->{1,2,3,4}
'''
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
'''
#str是不变对象，而list是可变对象。a='abc',a.replace('a','A')='Abc',注意：replace函数是在'abc'字符串的基础上新生成一个'Abc'，而不改变原来的值。
##二、函数
#调用函数：python内置了很多函数（https://docs.python.org/3/library/functions.html），如：abs()求绝对值，交互模式下help()函数可以查看帮助，
#传入函数的参数数量不一直或类型不一致，会报错：TypeError的错误。常用函数：取最大值max；print;input;list;tuple;dict;set;range;format;ord;chr;ascii等
#类型转换函数：int();float();str();bool();还可以给函数“起别名”，把函数名赋值给变量，就可以用变量名了，如下：
a=print
a('我用变量a输出了！')
#定义函数：定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，
#在缩进块中编写函数体，函数的返回值用return语句返回。遇到return就结束，如果没有return就返回None。交互模式下，两个回车退出函数定义。定义空函数用pass。
def my_abs(x1):
	if not isinstance(x1,(int,float)):#参数核查，参数只能是整型和浮点型。
		raise TypeError('bad operand type')#抛出异常TypeError异常。
	if x1 >= 0:
		return x1
	else:
		return -x1
print(my_abs(-929))#-->992
#函数返回多个值：
import math
def move(x,y,step,angle=0):#坐标、位移和角度，角度是默认参数，不填写自动置0. 特别注意：“定义默认参数要牢记一点：默认参数必须指向不变对象！” 
	radian = math.pi/180*angle#30度对应的[弧度]的定义是，当角所对的弧长等于半径时，角的大小为1弧度。角所对的弧长是半径的几倍，那么角的大小就是几弧度：角（弧度）＝弧长/半径 ；180度＝π弧度 ；
										#1度＝π/180 弧度；弧度＝度×π/180，反过来，π弧度＝180°；1弧度＝180°/π （≈57.3°）；度＝弧度×180°/π 。
	nx = x+step*math.cos(radian)#余弦×斜边=邻边;计算参考：https://blog.csdn.net/lyd1212/article/details/47359611
	ny = y+step*math.sin(radian)#正弦×斜边=对边
	return nx,ny
x ,y =move(100,100,60,30)
print(x,y)#-->151.96152422706632 130.0
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
print(math.sqrt(2))#-->1.4142135623730951#平方根计算。
#定义可变参数函数：要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,5,6]))#-->66
def calc2(*numbers):#加*号以后，在函数内部，参数numbers接收到的是一个tuple。
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
num1=[1,2,5,6]
print(calc2(*num1))#-->66#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去。
#关键字参数:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict.
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('Michael',30)#-->name: Michael age: 30 other: {}
person('Bob',35,gender='M',job='PythonEngineer',city='Beijing')#-->name: Bob age: 35 other: {'gender': 'M', 'job': 'PythonEngineer', 'city': 'Beijing'}
extra_dict={'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra_dict)#-->name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
#命名关键字参数：对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#但是调用者仍可以传入不受限制的关键字参数。如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')#-->Jack 24 Beijing Engineer

def person(name, age, *args, city, job):#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了.
    print(name, age, args, city, job)
#注意：命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#person('Jack', 24, 'Beijing', 'Engineer')#-->TypeError: person() takes 2 positional arguments but 4 were given,由于调用时缺少参数名city和job，
#Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
def person(name, age, *, city='Beijing', job):#命名关键字参数可以有缺省值，从而简化调用,
    print(name, age, city, job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack', 24, job='Engineer')#-->Jack 24 Beijing Engineer
#注意：使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
#参数组合：在Python中定义函数，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数，这5种参数都可以组合使用。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)#-->a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)#-->a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')#-->a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)#-->a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)#-->a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)#-->a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)#-->a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
#!! 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。




