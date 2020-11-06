assignment operation
a=b=c=1
print(a,b,c)


x=y=[2,3,4]
print(x,y)


def myfunc():
  a=b=c=10
  return a,b,c
print(myfunc())



def myfun(a,b):
  if a>b:
    print("A is Greater ")
  else:
    print("B is Greater ")
print(myfun(2,3))


set 
 
a={1,2,3}
print(a)

a = {1: 'one',2: 'two'}
print(a)


i = 7
if isinstance(i, int):
 i += 1
elif isinstance(i, str):
 i = int(i)
 i += 1
print(i)


a = 'hello'
print(list(a)) 
print(set(a)) 
print(tuple(a))


names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) 
print(names[2])


names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.append("Sia")
print(names)

names=['manu']
names.insert(1, "Nikki")
print(names)


a=[1,1,1,222,2,3,3]
print(a.count(1))

a=[1,2,3,4,5]

print(a[::-1])
print(str(a.reverse))


a=[1,2,3,4,5]
b=4
if b in a:
  print("Number is there")



import datetime
today=datetime.datetime.now()
print(str(today))
print(repr(today))



a='hello world'
print(a[::-1])
print(a)

def func():
 """This is a function that does nothing at all"""
 return

print(func.__doc__)



set operation

# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6} # {3, 4, 5}
# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6} # {1, 2, 3, 4, 5, 6}
# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
{1, 2, 3, 4} - {2, 3, 5} # {1, 4}
# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}
# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
{1, 2} >= {1, 2, 3} # False




page 89










