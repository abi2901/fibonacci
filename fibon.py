# Program to display the Fibonacci sequence up to n-th term
n= int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# if there is only one term, return n1
if n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
