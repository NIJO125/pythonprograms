def simp(p,t,r):
  s=(p*t*r)/100
  print("Simple interest is:",s)
  return s
p=int(input("Enter p :"))
t=int(input("Enter t:"))
r=int(input("Enter r :"))
print(simp(p,t,r))