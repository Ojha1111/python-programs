try:
    a=int(input("enter the number: "));
    b=int(input("enter the number: "));
    c=a/b;
except ZeroDivisionError as c:
    print(c)
except TypeError as c:
    print(c)
except ValueError as c:
    print(c)
else:
    print(c);
    
    
    
