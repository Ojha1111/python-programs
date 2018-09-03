def fibo(end):
    x=-1;
    y=1;
    z=1;
    for i in range(0,end):
        z=x+y;
        print(z,end=' ');
        x=y;
        y=z;
num=int(input('enter the number : '));
fibo(num);
        
