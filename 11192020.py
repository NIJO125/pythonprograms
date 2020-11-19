s={1,2,3}
for a in s:
  print(a)
l1=list(s)
print(l1)
l2=[a*2 for a in s if a > 2]
print(l2)


print(''.join(reversed('hello')))


p="Hello ".isalpha()
print(bool(p))


p="foo" in " for for"
print(bool(p))



a=" ".join(["Once","upon","time"])
print(a)


s = "She sells seashells by the seashore."
print(s.count("e"))


import random 
print(random.randint(1,10))

import random
print(random.randrange(1,100))

from collections import deque
d = deque('ghi') 
for elem in d:
  print(elem.upper())


import json
d = {
 'foo': 'bar',
 'alice': 1,
 'wonderland': [1, 2, 3]
}
with open("ext,txt", 'w') as f:
 json.dump(d, f)



import json
with open("ext.txt", 'r') as f:
 d = json.load(f)
 print(d)


 sqlite3


 import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks
 (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()




