#coding=utf-8
#搜索字符串
def  find(word,letter):
    count = 0
    while count < len(word):
        if  word[count] == letter:
            return count
        count=count+1
    return -1



s = 'Monty Python'
print  s[0:5]
print  s[6:12]

#字符串方法
#upper()  字符转换成大写
word ='banana'
new_word =word.upper()
print  new_word

#查找字符所在位置
index = word.find('a')
print index

#它可以接受两个参数，表示从哪一个下标开始查找，第三个实参表示查找到那个下标就结束
#http:docs.python.org/lib/string-methods.html   阅读字符串方法的文档
word.find('na',3)
word.find('na',1,2)

#操作符in    它是一个布尔操作符，操作于两个字符串上，如果第一个是第二个的子串，则返回True，否则返回false

'a' in 'banana'

#打印出word1中出现且出现在word2中的所有字符
def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print  letter


in_both('apples','oranges')

#字符串比较 关系操作字符也可以用在字符串上。检查两个字符串是否相等

if word == 'banana':
    print 'All right,bananas.'




