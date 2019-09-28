a, b , c= 0,1,0
z =4000000
for i in range(1,z):
  if i < z and i%2 == 0:
    c=a+b
    a=b
    b+=c
print(b)
