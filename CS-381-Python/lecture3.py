##n=int(input("Enter a number:\n"))
####sum = 1
####for i in range(n+1):
####    if i % 2 != 0:
####        sum+=i
####print("Sum of numbers from 1 to n is: ",sum)
##
##counter = 0
##
##while counter < 2:
##    if n%2 == 0:
##        n = n//10
##        if n % 2 == 0 & n & 10 < 10:
##            print("Success")
##            break
##    else:
##        print("Try again")
##        counter = counter + 1
##        n=int(input("Enter a number:\n"))

##n = int(input("Enter a number non-divisible by 10\n"))
##m = 0
##if(n%10 != 0):
##    while n > 0:
##        m = m*10
##        m = m + (n % 10)
##        n = n//10
##    print("New number: ",m)
##else:
##    print("err stmnt")

##n = input("Enter a number: ")
##while n != 'done':
##    n = int(n)
##    for i in range(sqrt(n)):
##        if i > 1 and n % i == 0:
##            counter+=1
##    if counter > 0 and n > 0:
##        print(n, "IS NOT a prime number")
##    else:
##        print(n, "IS a prime number")
##    n = input("Enter a number: ")

##for i in range(2,12,2):
##    print(i)

##for i in range(10,0,-3):
##    print(i)


"""Sum of off integers"""
##n = int(input("Enter a number:\n"))
##sumOf = 0
####for i in range(1, n+1):
####    if i%2>0:
####        sum+=i
##for i in range(1,n+1,2):
##    sumOf+=i
##print("Sum of odd integers from 1 to",n," is: ",sumOf)


"""Print numbers such that sum of digits = 20"""
##for i in range(299, 1001):
##    sumOf = 0
##    temp = i
##    while temp > 0:
##        sumOf = sumOf + (temp%10)
##        temp = temp // 10
##    if sumOf == 20:
##        print(i)

"""Print primes"""
##for i in range(1, 1001):
##    temp = i
##    for j in range(2, temp):
##        if temp % j == 0:
##            print(i)
##            break

"""Use loops to print coordinates"""
##for i in range(1,5):
##    for j in range(1,5):
##        print("(",i,",",j,")", sep=" ", end=" ")
##    print()


"""Pyramid of numbers \9/"""
##n = int(input("Enter a number:"))
##for i in range (0,n+1):
##    for j in range(1,n*2):
##        temp = j
##        if(temp>n):
##            temp = n*2 - temp
##        if(temp>i):
##            print(temp, sep="", end="")
##        else:
##            print(" ", sep="", end="")
##    if i < n-1:
##        print()

"""Inf loop"""
##i=1
##j=1
##while i<5:
##    while j<5:
##        if (i+j)%2==0: # as soon as one even number is encountered, increment not executed
##            continue
##        print("(",i,",",j,")", end="")
##        j+=1
##    print()
##    i+=1

"""Inf loop"""
##i=1
##j=1
##while i<5:
##    while j<5:
##        if (i+j)%2==0:
##            break
##        print("(",i,",",j,")", end="")
##        j+=1
##    print()
##    i+=1
##

"""Arrow Pattern"""
while (n:=input("How many columns: "))!="done":
    n = int(n)
    for i in range((n*2)-1):
        for j in range(n):
    ##        if (i <=n and(i==j)) or i+j==2*(n-1) and i>n-1:
            if i==j<=n or i+j==2*n-2:
                print("*",end="")
            else:
                print(" ",end="")
        print()
        



