age1=int(input('enter the triangle 1st age value  '))
age2=int(input('enter the triangle 2nd age value  '))
age3=int(input('enter the triangle 3rd age value  '))
sum=(age1+age2+age3)
area=(sum*(sum-age1)*(sum-age2)*(sum-age3)) ** 0.5
print('the area of triangle',area)
