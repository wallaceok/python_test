# -- coding: UTF-8
#coding=utf-8
from swampy.TurtleWorld import *;
import math

def  square(t):
    for i in range(4):
        fd(t ,100)
        lt(t)
def  polygon(t,n,length):
    angle = 360.0/n
    for i in range(n):
        fd(t,length)
        lt(t,angle)

def circle(t,r):
    circumference = 2*math.pi*r
    n = 50
    length = circumference/n
    polygon(t,n,length)

world = TurtleWorld()
bob = Turtle()
print bob
#square(bob)

#polygon(bob,7,70);

circle(bob,100)
user = wait_for_user()

