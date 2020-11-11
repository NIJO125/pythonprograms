a=[2,3,4,7,9]
a.append(10)
a.append(36)
print(a)


a=[2,3,4,7,9]
a.append(10)
a.append(36)

my_string="Hello world"
a.append(my_string)
print(a)


 extend()

a=[1,2,3]
b=[1,2,3]
a.extend(b)
print(a)
a.extend(range(9))
print(a) 

#index usage

a=[1,2,3]
b=[1,2,3]
b=a.index(3)
print(b)

#insert

a=[1,2,3]
a.insert(2,1)
print(a)

#pop
a.pop


#reverse


a=[1,2,3]
a.reverse()
print(a)


#sort

a=[1,2,3,9,3,2]
a.sort()
print(a)


#del

a=list(range(10))
print(a)
del a[::2]
print(a)




my_list=['hai','hai','hai']
for item in my_list:
  if(item=="hai"):
    print("hello world")
  

  page 144