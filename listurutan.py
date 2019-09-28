a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = 0
d,e = len(a),len(b)
for i in range(d):
  for j in range(e):
    if a[i] == a[j]:
      c += a[i]
      a[j] = a[i]
      a[i] = c
print(c)

