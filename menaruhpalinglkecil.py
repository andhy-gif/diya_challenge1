a =[1,2,3,4,12,34,-1,46,76,87,89]
b = 0
akhir=len(a)
for i in range(akhir):
  for j in range(i):
    if a[j] < a[i]:
      b = a[i]
      a[i] = a[j]
      a[j] = b   
print(a) 

