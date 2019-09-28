a = [[1,2],[3,4]]
b = [[4,3],[2,1]]
c=[]
for i in range (len(a)):
  d= []
  for j in range (len(a)):
    d.append(a[i][j]+b[i][j])
  c.append(d)
print(c)
#comp
a = [[1,2,8,7],[3,4,9,12],[8,7,3,1]]
b =[[9,11,12,3],[8,7,9,3],[29,8,4,3]]
e =[[8,9,4,3],[7,8,11,8],[2,1,2,3]]
c= []
for i in range(len(a)):
  d=[]
  for j in range(len(a[i])):
    d.append (a[i][j]+b[i][j]-e[i][j])
  c.append(d)
print(c)

