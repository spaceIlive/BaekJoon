a=int(input())
b=[]
c=[]
for i in range(a):
    d=input()
    e=len(d)
    for j in range(e):
        if j==0:
            if d[0]=='O':
                c.append(1)
            elif d[0]=='X':
                c.append(0)
        elif j!=0:
            if d[j]=='O':
                if d[j-1]=='O':
                    c.append(c[j-1]+1)
                elif d[j-1]=='X':
                    c.append(1)
            else :
                c.append(0)
    b.append(sum(c))
    c=[]
for i in range(a):
    print(b[i])
