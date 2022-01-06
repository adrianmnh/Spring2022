##len("abcde")

"""Square Root"""
##import math
##math.sqrt(9.1)


"""Is even"""
##def isEven(x):
##    if x%2:
##        return False
##    return True
##print(isEven(4))

"""LeapYear"""
##def isLeapYear(x):
##    if x%400==0:
##        return True
##    elif x%4==0 and x%100!=0:
##        return True
##    return False
##print(isLeapYear(777))
##print(isLeapYear(2000))
##print(isLeapYear(1000))
##print(isLeapYear(400))
##print(isLeapYear(100))
##print(isLeapYear(4))

"""Print primes, must rework"""
##from math import sqrt
##x=int(input("Enter 2 numbers:\n")) 
##y=int(input())
##print("The primes between x and y:")
##for i in range(x,y+1):
##    temp = i
##    for j in range(2,int(sqrt(i))):
##        if temp % j != 0:
##            print(i, sep=", ", end=" ")
##            break

"""COnvert integer iunto binary"""
##def my_bin(x):
####    return bin(x)[2:len(bin(x))]
##    s=""
##    while(x>0):
##        s=str((x%2))+s
##        x=x//2
##        print(s)
##my_bin(6)

"""My Sum"""
##def my_sum(*a):
##    print(a)
##    return sum(a)
##print(my_sum(3))
##print(my_sum())
##print(my_sum(5,6,8))

"""Sums"""
##def newSum(*a, neg):
##    if neg==False:
##        return sum(a)
##    return -sum(a)

"""Adding to list"""
##a=[]
##for i in range(1,11):
##    a.append(i)
##print(a)
##print(sum(a))
##a.append("Hello")
##print(a)
##print(sum(a))

"""Adding even positions numbers 1-10"""
##a=[]
##for i in range(1,11):
##    if i%2==1:
##        print(i)
##        a.append(i)
##print(sum(a))

"""Random Integers from 1-10"""
##from random import randint
##a=[]
##temp=0
##for i in range(10):
##    r = randint(1,10)
##    if r not in a:
##        a.append(r)
####    if a.count(r) == 0:
####        a.append(r)
######    if a[i]>temp:
######        temp=a[i]
##print(a)
####print(temp)

"""Random list from 1-25, find max in 2 ways"""
"""1. using a temp variable to keep track of max"""
##from random import randint
##a=[]
##temp=0
##for i in range(10):
##    a.append(randint(1,25))
##    if a[i]>temp:
##        temp=a[i]
##print(a)
##print(temp)
"""2. using max function of lists"""
##from random import randint
##a=[]
##temp=0
##for i in range(10):
##    a.append(randint(1,25))
##    temp=max(a)
##print(a)
##print(temp)
##
##for i in a:
##    print(i)
