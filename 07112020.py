i=0
while i<7:
  print(i)
  if i==4:
    print("Breaking from loop")
    break
  i += 1

for i in(0,1,2,3,4):
  print(i)
  if i==2:
    break



for x in ['one','two','three']:
  print(x)



for index,item in enumerate(['one','two','three']):
  print(index,'::',item)


