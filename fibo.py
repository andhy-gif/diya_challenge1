def fibonacci(n):
  a,b = 0,1
  while a<n:
    a,b=b,a+b
    if a % 2 == 0:
      print(a, end=' ')
      a += a
      print(a)
fibonacci(4000000)
