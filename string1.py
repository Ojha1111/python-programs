Python 3.0 (r30:67507, Dec  3 2008, 19:44:23) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 3.0      ==== No Subprocess ====
>>> a=[1,2,"abc",25.5];
>>> b=a;
>>> b[0]=50;
>>> print(a);
[50, 2, 'abc', 25.5]
>>> a=[20,10,3.5];
>>> type(a)
<class 'list'>
>>> a[2]
3.5
>>> a[2]=568
>>> print(a)
[20, 10, 568]
>>> a[-1]
568
>>> b=a[::-1]
>>> b
[568, 10, 20]
>>> a[1:3]
[10, 568]
>>> a[:2]
[20, 10]
>>> a[2:]
[568]
>>> c=a
>>> a
[20, 10, 568]
>>> c
[20, 10, 568]
>>> c[0]=100
>>> c
[100, 10, 568]
>>> a
[100, 10, 568]
>>> c
[100, 10, 568]
>>> c[1:1]=[70,80]
>>> c
[100, 70, 80, 10, 568]
>>> c[3]=[]
>>> c
[100, 70, 80, [], 568]
>>> del d[3]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    del d[3]
NameError: name 'd' is not defined
>>> del c[3]
>>> c
[100, 70, 80, 568]
>>> d=[20,39,49]
>>> c+d
[100, 70, 80, 568, 20, 39, 49]
>>> a[0]*5
500
>>> c=[]
>>> c=[0]*5
>>> c
[0, 0, 0, 0, 0]
>>> c=[1,2,3]
>>> c=[1,2,3]*3
>>> c
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
