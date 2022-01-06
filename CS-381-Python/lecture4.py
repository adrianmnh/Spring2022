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

"""Print primes"""
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
####def my_bin(x):
####

"""My Sum"""
def my_sum(*a):
    print(a)
    return sum(a)
print(my_sum(3))
print(my_sum())
print(my_sum(5,6,8))

