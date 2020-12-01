def fact(n):
  return 1 if (n==1 or n==0) else n*fact(n-1)
a=int(input("Enter your no"))
print(fact(a))