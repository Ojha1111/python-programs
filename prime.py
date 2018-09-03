n=int(input("enter the number"))

if n > 1:
    for i in range(2,num):
        if(n % 2) == 0:
            print('the number is not prime')
            break
        else:
            print('the number is prime')
else:
    print('the number is not prime')
