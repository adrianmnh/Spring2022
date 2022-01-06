Most programming languages reference the address of the object

Python references the address of the object itself
Cpy on write, make a copy for the changed object

b and a pointing to the same object
a gets assigned a new value
a gets a new copy, b remains the same

in python objects are immutable

to get a substring in python, you dont change the original string and concat it, a copy of the substring gets created as a new object

print function keywords

value sept end file flush

python interpreter ignotes comments

multi row quote marks for comments

Reference counting
some object [5]
a=5 , then a is pointing to the object
the 5 is an actual object with a lot more information that just the 5
there's a counter of pointers referencing this object

import sys

sys.getrefcount(z)

ref counter is important for garbage collection:

in c++:
int a = 5 -> stack memory(automatic variable)
int *p = new int[5] -> allocating heap memory(automatic variable)
to delete the memory allocation of "new int[5]" we have to explicitly deallocate memory space

In Python:

del(object) is the explicit deallocation technique

in c++
a=5;
cout << (a=a+1); -> This is an expression(it has a side effect)
Whats changing in the environment? The value being referenced by a is changing

Whats the "value" of the expression?

cout<< (a=5) -> prints out a reference of "a" not 5


Python
print(a:=a+1) prints the object reference

Problem rounding a number

round(x[,n])

add .5 to the float, and then cast to integer

To find if a number is odd or even

print(n, (n%2==0)*'EVEN' + (n%2!=0)*'ODD')

How to swap a and b
temp = a
a = b
b = temp
a,b = x,y

To swap in python:
a,b = b,a


Format function
3 ways to format

format(123123.14, '20.2f')  -> a field of 20, and floating precision 2
'20,.2f' , number with commas







