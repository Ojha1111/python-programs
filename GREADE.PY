a=int(input('enter the number'));
b=int(input('enter the number'));
c=int(input('enter the number'));
d=int(input('enter the number'));
e=int(input('enter the number'));

total_num = [((a+b+c+d+e)/5)*100%]

if(total_num >= 75%):
    print('your marks grade A ');
elif (60% <= total_num <= 74.99%):
    print('your marks grede B');
elif (50% <= total_num <=59.99 ):
    print('your marks grede C');
else:
    print('your marks grade D');
