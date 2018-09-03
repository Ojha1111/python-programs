def facto(num):
    result=1
    for i in range(1,num+1):
        result=result*i
        return(result);
    
def check(num1):
    s=0
    while(num1>0):
        rem=num1%10
        fact=facto(rem)
        s=s+fact
        num1=num1//10
    return(s)
n=int(input('enter the number: '))
chk1=check(n)
if chk1==n:
    print('it is perfect number')
else:
    print('it is no perfect number')
    
