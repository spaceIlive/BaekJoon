import math
import sys
a=[]
while True:
    x,y,z=map(int, sys.stdin.readline().split())
    if x==y==z==0:
        break
    else:
        if x**2==y**2+z**2:
            a.append('right')
        elif y**2==x**2+z**2:
            a.append('right')
        elif z**2==y**2+x**2:
            a.append('right')
        else:        
            a.append('wrong')
for i in range(len(a)):
    print(a[i])            