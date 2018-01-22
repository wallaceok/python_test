#coding=utf-8
letters = ['d','a','b','c']

#列表切片
print  letters[1:3]

#在列表尾部添加新的元素
letters.append('z')

#extemd 方法接收一个列表作为参数，并将其所有的元素附加到列表中
t1 = ['a','b','c']
t2 = ['d','e']
t1.extend(t2)
print t1

#列表人低到高排列
letters.sort()
print letters

#列表中删除元素
t=['a','b','c']
x = t.pop(1)
del t[1]

t.remove('a')


#字符串分隔成数组
s = 'pining for this fjords'
t = s.split()
print t

s='span-span-span'
t =s.split('-')
print t

#join 是split的逆操作
t= ['pining','for','the','fjords']
delimiter =' '
print  delimiter.join(t)

