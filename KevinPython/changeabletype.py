Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> print('First, variable a has value', a, 'and type', type(a))
First, variable a has value 10 and type <class 'int'>
>>> a =ABC
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a =ABC
NameError: name 'ABC' is not defined
>>> a = 'ABC'
>>> print('Now, variable a has value', a, 'and type', type(a))
Now, variable a has value ABC and type <class 'str'>
>>> 
