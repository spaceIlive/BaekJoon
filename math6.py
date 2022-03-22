Test_case= int(input())
a=[]
b=[]
for i in range(15):
    inner=[]
    if i == 0:
        for j in range(14):
            inner.append(j+1)
        a.append(inner)
          
    else :
        for j in range(0,14):
            if j ==0:
                inner.append(1)
            else:    
                inner.append(inner[j-1]+a[i-1][j])
        a.append(inner)
for i in range(Test_case):
    inner2=[]
    for j in range(2):
        inner2.append(int(input()))
    b.append(inner2)    
for i in range(Test_case):
    print(a[(b[i][0])][(b[i][1])-1])

# 나는 한번에 아래꺼랑 왼쪽거 더하려 했는데 차라리 밑에꺼를 복사한 이우에 왼쪽꺼를 더하는것도 나쁘지는 않은듯