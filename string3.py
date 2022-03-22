a=input()
b='abcdefghijklmnopqrstuvwxyz'
c=[]
for i in range(len(b)):
    c.append(b[i])
for i in range(len(c)):
    for j in range(len(a)):
        if c[i]==a[j]:
            c[i]=j
            break
        elif j==len(a)-1:
            if c[i]==a[j]:
                c[i]=j
            else :
                c[i]=(-1)
for i in c:
    print(i,end=' ')      #줄바꿈없이 출력     
