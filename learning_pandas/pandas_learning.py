#!/usr/bin/env python
# _*_coding:utf-8 _*_
import pandas as pd
import datetime
import numpy as np
from pandas import DataFrame,Series
import chardet
df= pd.read_csv('E:\\nbiot.csv', encoding='gbk',header=5)#索引第5行为表头。
df["地市"]=df.网元名称.apply(lambda x:x[:2])#以网元名称列为基准，创建新的列“地市”。
print(df.head(5))#输出前5行。
df.rename(columns={'用户数':'用户'},inplace = True)#修改列名称，inplace布尔值，默认为False。
# 指定是否返回新的DataFrame。如果为True，则在原df上修改，返回值为None
n_df=df.rename(columns={'用户':'用'},inplace=False)#此处inplace为True，则n_df为None.
#n_df.to_csv("E:\\3.csv",encoding='utf_8_sig')
print(df.head(5))
tb = pd.pivot_table(df, values=['请求','成功','用户'], index=['地市'],columns=['覆盖等级'], aggfunc=[np.mean,len],fill_value=0,margins=True)
#fill_value的意思是以什么来替代NaN,margins为True表示添加汇总列。
print(tb)
#print(tb.fillna(0))
tb.to_csv("E:\\2.csv",encoding='utf_8_sig')

#pandas.merge和实例方法join实现的是图2列之间的连接，以DataFrame数据结构为例讲解，DataFrame1和DataFrame2
# 必须要在至少一列上内容有重叠，index也好，columns也好，只要是有内容重叠的列即可，指定其中一列或几列作为
# 连接的键，然后按照键，索引DataFrame2其他列上的的数据，添加DataFrame1中。例，以columns内容作为连接键：
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df2 = DataFrame({ 'key': ['a', 'b', 'd'],'data2': range(3),'data3':range(3,6)})
df3=pd.merge(df1, df2)#以df1的key为标准，把df2中的数据按V过来。并忽略df1中没有匹配到的key行。
print("pandas.merge的用法")
print(df1,"\n","*"*30)
print(df2,"\n","*"*30)
print(df3,"\n","*"*50)
#通过设置merge参数'on'，'left_on'，'right_on'可以指定用来连接的列（即关键的重复内容列），也可以将index作为连接键，
# 只要传入left_index=True或right_index=True（或两个都传）来说明索引被用作连接键，例：
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
lr1=pd.merge(left1, right1, left_on='key', right_index=True)#
print("pandas.merge方法的参数")
print(left1,"\n","*"*30)
print(right1,"\n","*"*30)
print(lr1,"\n","*"*50)
#而实例方法join默认通过index来进行连接，例：
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
lr2=left2.join(right2, how='outer')#how='inner'为默认连接方式：交集，outer为并集。相同索引连接，不同则留空。
print("DataFrame.join的用法")
print(left2,"\n","*"*30)
print(right2,"\n","*"*30)
print(lr2,"\n","*"*50)
#上面介绍的函数实现的均是列之间的连接，要实现行之间的连接，要使用pd.concat方法，例:
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
ss=pd.concat([s1, s2, s3],axis=0)#axis默认为0，即纵向合并
st=pd.concat([s1,s2,s3],axis=1)#axis设置为1，则横向合并。
print("pandas.concat的用法")
print(s1,"\n","*"*30)
print(s2,"\n","*"*30)
print(s3,"\n","*"*30)
print(ss,"\n","*"*30)
print(st,"\n","*"*50)
#combine_first:它实现既不是行之间的连接，也不是列之间的连接，它在为数据“打补丁”：用参数对象中的数据为调用者对象的缺失数据“补空”
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],'b': [np.nan, 2., np.nan, 6.],'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],'b': [np.nan, 3., 4., 6., 8.],'d':[1,2,3,4,5]})
df3=df1.combine_first(df2)
print("DataFrame.combine_first的用法")
print(df1,"\n","*"*30)
print(df2,"\n","*"*30)
print(df3)

df=pd.read_csv('E:\\csv_result.csv')
print(df.head(0))#输出表头
print(df['小区'][:5])#输出[小区]列的前5个数据。
print(df.小区.str[9:30][:5])#截取字符串


##根据起始时间和网元名称进行分组后对TA区间0的次数列进行sum求和计算
print(df.columns[0])#输出列名-->起始时间
gp=df.groupby(["起始时间","网元名称"])["用户随机接入时TA值在区间0范围的接入次数 (无)"].sum()
print(gp[:5])
#gs=df.起始时间.str[:10][:5],df.网元名称,df["用户随机接入时TA值在区间0范围的接入次数 (无)"]
#pv=df.pivot_table(df['起始时间'].str[:10],index="网元名称",columns="用户随机接入时TA值在区间0范围的接入次数 (无)",margins=True,aggfunc=np.sum,fill_value=0)
#数据透视图,对起始时间列进行汇总计算,index为行,columns为列,margins=True增加一个全部行汇总,aggfunc=np.sum透视图中对起始时间值进行sum计算,这里np是开头import的numpy as np,fill_value=0对空值进行0替换,否则没有数据会显示NaN
#print(gs[:5])
#print(df["用户随机接入时TA值在区间0范围的接入次数 (无)"] > 500000)#采样点大于5000,返回False 或者True
print(df.网元名称.str.startswith('HZS')[:5])#字符串匹配
#print(df.iloc(3))
df=df.set_index(["网元名称"])#设置索引
print(df.head(5))
print(df.loc['VIP_HZFL0181杭州浙大玉泉校区'])#按照索引返回series,也可以用df.ix['VIP_HZFL0181杭州浙大玉泉校区']
print(df.sort_index(ascending=False).head(5))#对索引排序，ascending=False表示降序。
#当你为一列数据设置了一个索引时，它们将不再是数据本身了。如果你想把索引设置为原始数据的形式，你可以使用和set_index相反的操作——reset_index。
df = df.reset_index()#释放索引
print(type(df.小区))#返回object
#DataFrame.apply,Series.map,DataFrame.applymap用法的比较：
print(df.apply(lambda x:isinstance(x,object))) #输出每一列对应一个值
print(df["用户随机接入时TA值在区间0范围的接入次数 (无)"].map(lambda x:"%.2f" %x)) #对series中的每个元素进行函数操作
apm=df.applymap(lambda x:x==None)[:5]#对dataframe中的每一个元素进行函数操作
#apm.to_csv("E:\\1.csv",encoding='utf_8_sig')
print(apm)
def MyDate(time):
    MyDate=time[:10]
    #MyDate=pd.to_datetime(MyDate).date
    return MyDate
df["日期"]=df.起始时间.apply(MyDate)
print(df.head(5))
#df.to_csv("E:\\1.csv",encoding='utf_8_sig',index=False)
grp=df.groupby([df.日期,df.网元名称])[['QPSK调制方式的上行达到最大重传次数之后的仍然传输失败的TB数 (无)','16QAM调制方式的上行达到最大重传次数之后的仍然传输失败的TB数 (无)']].sum()
#grp.to_csv("E:\\1.csv",encoding='utf_8_sig')
print(grp)
#数据差集计算
MyFile=(r"D:\kaligit\learning_pandas\test1.csv")
with open(MyFile, 'rb') as f:
    MyFileCode = chardet.detect(f.read())['encoding']
df= pd.read_csv(MyFile, encoding=MyFileCode,header=0,dtype={"本端基站ID":str,"对端基站ID":str})#索引第1行为表头。
#print(df.head(5))
df.fillna(value="-",inplace=True)
new_df1=df["本端基站ID"]+";"+df["对端基站ID"]
new_df2=df["对端基站ID"]+";"+df["本端基站ID"]
c=new_df1.append(new_df2)
c.drop_duplicates(keep=False,inplace=True)
#这里想要说明的是，drop_duplicates当中的参数keep=False，意为重复项全部删除，它还有keep="first"与keep="last"，
# 分别对应在有多项重复时，保留第一项（或最后一项）。
c.reset_index(drop=True)
#不想保留原来的index，直接使用重置后的索引，那么可以使用参数drop=True，默认值是False
c.name="单向对"
#对DataFrame列的重命名d.columns=['a','b','C'];或者d.rename({'a':'A', 'b':'B'},inplace=True)。Series用s.name="newname";或者s.rename("newname1",inplace=True)。
c.to_csv("E:\\2.csv",encoding='utf_8_sig',index=False,header=True)



