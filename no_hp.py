def no_hp(no):
  k = ' -'
  a = ''
  b = ''
  for i in no:
    if i not in k:
      a += i
  if len(a) % 3 == 0 or len(a) % 3 == 2:
    for j in range(len(a)):
      if j == 0:
        b += a[j]
      elif j % 3 != 0:
        b += a[j]
      elif j % 3 == 0:
        b += '-'
        b += a[j]
  elif len(a) % 3 == 1:
    for j in range(len(a)):
      if j == 0:
        b += a[j]
      elif j % 3 != 0:
        b += a[j]
      elif j % 3 == 0:
        b += '-'
        b += a[j]
      if j >= len(a)-3:
        break
    for j in range(2):
      if j % 2 == 0:
        b += '-'
        b += a[j+len(a)-2]
      else:
        b += a[j+len(a)-2]
  else:
    return a
  return b
print(no_hp('00-44 48 5555 8361'))
print(no_hp('0 - 22 1985--324'))
print(no_hp('555372654'))
print(no_hp('5553'))
print(no_hp('55'))
print(no_hp('55-5'))
