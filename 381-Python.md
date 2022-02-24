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


## Difference between runtime stack and heap in python:
Everything on the heap in python

In c/c++
int a : automatic variable

In memory, there's a part for functions(code segment), and another for variables. A portion of memory is allocated for static variables. Another portion allocated for runtime stack(activation records) which includes variables within some scope. The memory allocated for dynamic memory is called the heap.

In the heap, memoery is used without previous knowledge of the amount of memory that may be used. A memory manager distributes available space to the heap as needed

When a program runs on heap memory, it generally takes a lot more time to execute because the heap requires different memory allocation algorithms working on the background.

Python functions that are written in c/c++ are generally much faster than native python functions


What's an object?
Things can be done to an object, use functions on it and such

Python is a first class object language

## Difference between class and object

Class creates class objects

Dunder methods??
Double under methods
* Special methods of certain classes

When using iterables:
* next(q) &rarr; q.__next__



add methods of the integer class

```c
q=7
q.__add__(5)
```

In c/c++

if Z is a rational number, and we want to perform addition between 2 objects of class "rational", then we can overload the + operator

```c
Rat operator+(Rat r){...}
z=x.operator+(r) // this is the equivalent of a dunder methods in Python
```

## Lists, tuples, dictionaries

You can store different type objects in a list

c/c++, lists are homogenous

In Python, a list is an array of pointers, the types don't adhere to the variables(names) but to the objects pointing to

## Why is python considered a scripting language?

* Scripted languages are interpreted
* 

Scripting languages are used for coordinating multiple programs by checking status codes, executes dynamically. Written in operating system language

c/c++ main function returns int

In large systems, there are chains of programs running

If a program is successful, 


## Function overloading:

Getting one function to do multiple things

In python, function names can be overloaded by overriding the previous function definition


For loops call **next()** on eveyr iteration of the loop

For loops are generators


### Python 

does nto concern with closing files or memory leakage. Context manager

## RAII
Resources Acquising initialization


# Command Compilation:

`python -m module_name` - run library module as a script

`python -m pydoc package_name` - documentation

`cat/nano PATH/module_name.py` - view documentation without executing commands

`python -m venv virtualenv_name` - create venv

`venvPATH\Scripts\activate.bat` - activate venv

`pip install package` - install package in venv


# Python Django Server

`python -m django version`

`django-admin startproject ProjectName` - creates project and populates django organizational unit. Contains settings and database configuration for single or multiple apps/website

`python ProjectName/manage.py startapp AppName` - creates single app/website within django project

`python manage.py migrate` - database migration: internal management tool that ensures django **database used** is consistent with **database definition**

`python manage.py runserver`

* `urls.py` - stores urls  must be in both the application and enclosing django project. This file must have the urls 