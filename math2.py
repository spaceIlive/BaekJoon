'''M=int(input())
N=int(input())
a=[]
for i in range(M,N+1):
    a.append(i)
b=[]    
for i in range(1,10001):
    if  i==2:
        b.append(i)
    elif i ==1 :
        continue    
    else:
        for j in range(2,i):
            if i%j==0:
                break
            else:
                if j==i-1:
                    b.append(i)
                else:
                    continue
c=[]                    
for i in a:
    if i in b:
        c.append(i)
    else:
         continue 
if len(c)==0:
    print(-1)
else:

    print(sum(c))
    print(min(c))           '''               
n1=int(input())
n2=int(input())
if n1==1:
    n1=2
sum=0
min=10001
for e in range(n1,n2+1):
    prime=True
    for i in range(2,e):
        if e%i==0:
            prime=False
            break
    if prime:
        if min>e:
            min=e
        sum+=e
if sum!=0:
    print(sum)
if min==10001:
    print(-1)
else:
    print(min)  # 이거 좋은 코딩인거 같아서 긁어옴     