print([x+2 for x in range(10)])



for i in [x**2 for x in range(20)]:
  print(i)


print({x for x in range(5)})

[x + y for x, y in [(1, 2), (3, 4), (5, 6)]]
# Out: [3, 7, 11]
[x + y for x, y in zip([1, 3, 5], [2, 4, 6])]
# Out: [3, 7, 11]



matrix=[[1,2,3],[4,5,6],[7,8,9]]
print([[row[i] for row in matrix] for i in range(len(matrix))])


with open('shoppinglist.txt','r') as fileobj:
  content=fileobj.read()
  lines=content.split('\n')
print(lines)



s=lambda: "Hello"
print(s())


s=lambda s: s.strip().upper()
print(s("Hello"))
    

    