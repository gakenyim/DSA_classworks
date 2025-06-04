def fibonacci(n):
    if n==0:
      return 0
    elif n ==1:
      return 1
    else:
      return fibonacci(n-1)+fibonacci(n-2)

    

#  n_terms = int(input("Enter the number of terms required by the user: "))
# ##first two terms
#  n_1=0
#  n_2=1
#  count=0
#  if n_terms<=0:
#   print("Please enter a positive integer")
#  elif n_terms==1:
#   print("Fibonacci sequence upto",n_terms,":")
#   print(n_1)
#  else:
#   print("Fibonacci sequence:")
#  while count<n_terms:
#   print(n_1)
#   nth=n_1+n_2
#   n_1=n_2
#   n_2=nth
#   count+=1