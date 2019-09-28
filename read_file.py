import sys
f=open(sys.argv[1],'r')
line =f.readline()
l=0
while line:
    l+=1
    print(l)
    print(line)
    line=f.readline()

