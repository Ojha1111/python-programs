Python 3.0 (r30:67507, Dec  3 2008, 19:44:23) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 3.0      
>>> a=hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=hello
NameError: name 'hello' is not defined
>>> a="hello"
>>> a[0]
'h'
>>> a[3]
'l'
>>> a[1:3]
'el'
>>> a=a[0]+'i'+a[2:5]
>>> a
'hillo'
>>> a.index('il')
1
>>> a.index('l')
2
>>> a.index('l',3)
3
>>> a.index('l',4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.index('l',4)
ValueError: substring not found
>>> a.count('l')
2
>>> x="lovely"
>>> x.count('l')
2
>>> pos=x.index('l')
>>> pos
0
>>> x.index('l',pos+1)
4
>>> x.index
<built-in method index of str object at 0x00000000030B68A0>
>>> x.index('v')
2
>>> x.count('v')
1
>>> len(a)
5
>>> a[-1]
'o'
>>> index=0
>>> 
>>> print(string.ascii_lowercase)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(string.ascii_lowercase)
NameError: name 'string' is not defined
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
>>> print(string.ascii_uppercase)
ABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> 
