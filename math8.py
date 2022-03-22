import sys
x=[]
y=[]
c=[]
for i in range(3):
    a,b=map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)
for i in range(3):
    count=0
    for j in range(3):
        if x[i]==x[j]:
            count+=1
    if count==1:
        c.append(x[i])
    else: continue
for i in range(3):
    count=0
    for j in range(3):
        if y[i]==y[j]:
            count+=1
    if count==1:
        c.append(y[i])
    else: continue
print('%d %d'%(c[0],c[1]))