print("welcome")

print("Enter x and y")

print()

x=input("Enter x(entering done ends program):")

while x!='done':
    x = int(x)
    y=int(input("Enter y:"))
    sum=x+y
    print("Sum of ",x,"and",y," is:",sum)
    print()
    x = input("Enter x or 'done'")

print()
print("thanks")
