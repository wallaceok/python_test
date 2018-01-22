#coding=utf-8

# 字典是集合和值集合之间的映射
#{} 代表一个字典
eng2sp = dict()
print  eng2sp
#字典添加新项
eng2sp['one']='uno'
print  eng2sp

print  eng2sp['one']

#多个值一起赋
eng2sp = {'one':'uno','two':'dos','three':'tres'}
print eng2sp
#字典的键值对的数量
len(eng2sp)

#in 一个值是不是字典 中的值  true   false
print  'one' in eng2sp

#values  以列表形式返回字典所有的值并可以有in操作符
vals = eng2sp.values()
print vals
print 'un1o' in vals

dicts = dict()
fin = open('words.txt')
for line in fin:
    word = line
    dicts[word] = word
    #print word

print dicts.viewkeys()

#直方图 统计学术语表示一个计数器的集合  每个字母出现过几次
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] =1
        else:
            d[c]+=1
    return d

# h = histogram('brontosaurus')
# print  h

#循环和字典
def  print_hist(h):
    for c in h:
        print  c,h[c]

h = histogram('parrot')
print_hist(h)

#反向查找
def revrse_lookup(d,v):
    for k in d:
        if d[k] ==v:
            return  k
    raise ValueError

h = histogram('parrot')
k = revrse_lookup(h,2)
print k


#字典和列表 列表可以在字典中以值的形式出现。下面是 反转字典的函数
def  invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val  not in inverse:
            inverse[val] =[key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print hist
inverse = invert_dict(hist)
print inverse


#备忘 数一下fibonacci(0) 和fibonacci(1) 被调用了多少次  记录已经计算过的值
#know 是一个用来记录我们已知的Fibonacci数的字典。开始时它有两项：0映射到0，以及1映射到1
#每当fibonacci被调用时，它会先检查know。如果 结果已经存在，则可以立即返回。如果不存在，它需要计算这个新值，将其添加进字典，并返回
know = {0:0,1:1}
def fibonacci(n):
    if n in know:
        return know[n]
    res = fibonacci(n-1) +fibonacci(n-2)
    know[n]= res
    return res





