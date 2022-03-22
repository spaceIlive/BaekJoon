Test_case= int(input())
a=[0 for i in range(Test_case)]
c=list(map(int,input().split()))
for i in range (Test_case):
    a[i]=c[i]
b=[]    
for i in range(1,1001):
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
count=0
for i in a:
    if i in b:
        count+=1
    else:
        continue
print(count)  