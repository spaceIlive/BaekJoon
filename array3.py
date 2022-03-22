a=int(1)
for i in range(3):          
    b=int(input())          
    a=a*b                   #3개 수 곱
c=str(a)                    #문자형으로 변환
d=[]                        #리스트화 과정(문자형 변환)
for char in c:              #문자형으로 말고 숫자로는 안될까?
    d.append(char)
'''count_0=0                #'0'카운트 과정
                            #이건 코드가 너무 길어지고 일일이 노가다 하는 느낌
for i in range(len(d)):
    if d[i] == '0':
        count_0=count_0 + 1

print(count_0) ''' 
e=["0","1","2","3","4","5","6","7","8","9"]
f=[]
for i in range (10):
    count=0
    for j in range(len(d)):
        if e[i]==d[j]:
            count=count+1
    f.append(count)
for i in range(10):
    print(f[i])    
