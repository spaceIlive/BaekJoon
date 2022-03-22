n=1
while (True):
    n=n+1
    if 3*n*(n-1)+1>1000000000:
        break


num=int(input())

for i in range(2,n+1):
    if 3*(i-1)*(i-2)+2<=num<=3*i*(i-1)+1:
        print(i)
    elif num==1:
        print(1)
        break