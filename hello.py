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
#练习题:以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y = 1, *nums):
    for i in nums:
        y *= i
    return x*y
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
#递归函数：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n): #计算n的阶乘
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))#-->120
'''
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
#递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
#每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。如：fact(1000)
'''
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
'''
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
'''
#练习题：汉诺塔实现，请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。
def move(n, a='A', b='B', c='C'):
    if n == 1:
        print(a, '-->', c)
    else:
        move((n-1),a,c,b)
        print(a, '-->', c)
        move((n-1),b,a,c)
move(3)
#A --> C
#A --> B
#C --> B
#A --> C
#B --> A
#B --> C
#A --> C
##切片：取一个list或tuple的部分元素是非常常见的操作[:::]
List1 = list(range(100))
print(List1)#输出List1
print(List1[:10])#输出前十个元素
print(List1[-10:])#后十个
print(List1[10:20])#前11-20个数
print(List1[:10:2])#前10个数，每两个取一个
print(List1[::5])#所有数，每5个取一个
print(List1[:])#原样复制一个list
print((0, 1, 2, 3, 4, 5)[:3])#tuple一样-->(0, 1, 2)
print("ABCDEFGHIJKLMN"[2:8:2])#字符串也可以-->CEG
#练习题：实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while s[-1:] ==' ':#循环判断结尾是否为空格
    	s=s[:-1]	   #舍去空格，重新赋值给s
    	#continue	   #继续，也可以替换成trim(s)或者直接省略
    while s[:1] ==' ': #循环判断开头是否为空格
    	s=s[1:]		   #舍去空格，重新赋值给s
    	#continue	   #继续，也可以替换成trim(s)或者直接省略
    return s
 #测试   
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
##迭代：如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#python中list,tuple,str，dict都是可迭代的，用for……in……完成：
for c in 'ABCDEF':
	print(c)
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)#-->a\n  b\n  c\n
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
#通过collections模块的Iterable类型可判断一个对象是否可迭代：
from collections import Iterable
print(isinstance('abc', Iterable))#-->True
print(isinstance([1,2,3], Iterable))#-->True
print(isinstance(123,Iterable))#-->False
#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A','B','C']):
	print(i, value)#-->输出类似dict的索引值对
#练习题：请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
	if L == []:
		return(None,None)
	x = y = L[0]
	for i in L:
		if i < x:
			x = i
		if i > y:
			y = i
	return (x,y)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
##列表生成式：列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print(list(range(1,11)))#-->要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print([x * x for x in range(1, 11)])#-->[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]#生成[1x1, 2x2, 3x3, ..., 10x10]
print([m + n for m in 'ABC' for n in 'ABC'])#-->['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']#还可以使用两层循环，可以生成全排列.
#生成字典
import string	
a = list(range(0,10))
A = []
for xin in a:
	A.append(str(xin))
b = list(string.ascii_lowercase)
c = list(string.ascii_uppercase)
#d = list(string.ascii_letters)#大写加小写
#print([m + n + k for m in A for n in b for k in c])#生成3个字符组成的全排列列表。
#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value,因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
List2 = [k + '=' + v for k, v in d.items()]
print(List2)#-->['y=B', 'x=A', 'z=C']
print([s.lower() for s in List2])#-->['x=a', 'y=b', 'z=c']
L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = []
# for s in L1:
# 	if isinstance(s,str) == True:
# 		s=s.lower()
# 		L2.append(s)
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')



