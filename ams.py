import math
def digits(num):
    n=0
    while(num>0):
        n=n+1
        num=num//10
    return(n)
def power(x,y):
    return(math.pow(x,y));
def armstrong(num,p):
    s=0
    while(num>0):
        rem=num%10
        pr=power(rem,p)
        s=s+pr
        num=num//10
    return s
n=int(input('enter the number: '))
y=digits(n)
arm=armstrong(n,y)
if arm==n:
    print('the number is armstrong')
else:
    print('the number not armstrong')
