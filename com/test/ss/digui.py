#coding=utf-8
#递归简单例子
def countdown(n):
    if n<=0:
        print 'Blastoff'
    else:
        print n
        countdown(n-1)

countdown(10)


def  factorial(n):
    if n==0:
        return 1
    else:
        recurse= factorial(n-1)
        result=n*recurse
        return result

