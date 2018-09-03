count=0
pwd='cse'

while True:
    password=str(input('enter your password: '))

    count += 1
    
    if(password == pwd):
        print('login successfull')
        break;
    elif (password != pwd) :
        if(count >= 3):
           print ('you have been denied access')
           break
    
