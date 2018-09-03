
n1 = 0
n2 = 1
count = 0
for i in range(0,50):

  if i <= 0:
   print("Please enter a positive integer")
  elif i == 1:
   print("Fibonacci sequence upto",i,":")
   print(n1)
  else:
   print("Fibonacci sequence upto",i,":")
   while count < i:
       print(n1,end=' , ')
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1
