total = 0
stop = True
for i in range(2000000):
  batas = round(i ** 0.5)
  if i == 2:
    total += i
  for j in range(2,batas + 1):
    if i % j == 0:
      break
    if j == batas:
      total += i
print('jumlah bilangan prima dengan nilai di bawah 2000000 adalah',total)

