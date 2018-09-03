n=int(input('enter the number'))
factorial = 1
if(n<0):
    print('this number is not factorial');
elif(n == 0):
    print('this number factorial is 1');
else:
    for i in range(1,n + 1):
        factorial = factorial*i
        print('the factorial number is',num,'is',factorial)
