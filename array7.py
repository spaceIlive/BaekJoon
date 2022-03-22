a=int(input())
b=[]
c=[]
for i in range(a):
    b=list(map(int,input().split()))
    sum=0
    aver=0
    count=0
    for j in b[1:]:
        sum += j
    aver=sum/b[0]
    for k in b[1:]:
        if k>aver:
            count += 1
    c.append(count/b[0]*100)    
for i in range(a):
    print("{:.3f}%".format(c[i])) #format함수에 소숫점표현    