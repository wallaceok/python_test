#coding=utf-8
#元组是不可变的
t = ('a','b','c','d','e')
print t[0]
print t[1:3]

#('b', 'c')
#如果尝试修改元组中的一个元素，会报错误
#t[0] ='A'    是错误的
#不能修改元组的元素，但是可以将一个元组替换为另一个
t= ('A',) +t[1:]
print t
#元组赋值
a,b = 1,2

#作为返回值的元组
#内置函数divmod 接收两个参数，并返回两个值 的元组，即商和余数。可以将结果存为一个元组
t = divmod(7,3)
print t

quot,rem = divmod(7,3)
print quot
print rem

#max  min都是内置函数，分别返回一个序列的最大值和最小值。min_aax 计算这个两个值将它们作为一个元组返回
def min_max(t):
    return  min(t),max(t)

#可变长的参数元组
#函数可以接收不定个数的参数。以*开头的参数名会收集（gather)所有的参数到一个元组上。
def  printall(*args):
    print args

printall(1,2.0,'3')
#分散（scatter)如果有一个序列的值而想将它们作为可变长参数传入到函数中，可以使用*操作符。例如，divmod正好接收两个参数，它们不接收元组
t = (7,3)
#divmod(t)  #这样会抛出异常
divmod(*t)  #分散后就不抛出异常了

####列表和元组 zip是一个内置函数，接收两个或多个序列，并将它们“拉”到一起，成为一个元组列表。每个元组包含各个序列中的一个元素。
#将字符串和一个列表“拉”到一起
s = 'abc'
t = [0,1,2]
zz = zip(s,t)
print zz
#[('a', 0), ('b', 1), ('c', 2)]     每个元组包含的一个字符和列表中对应的元素。如果序列之间的长度不同，则结果的长度是所有序列中最短的那个。
zz =zip('Anne','elk')
print zz    #[('A', 'e'), ('n', 'l'), ('n', 'k')]

#可以在for循环中使用元组赋值来访问元组的列表
t = [('a',0),('b',1),('c',2)]
for letter,number in t:
    print number,letter




