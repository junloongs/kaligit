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





