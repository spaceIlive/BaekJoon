a=list(map(str,input().split()))
num=""
for i in range(2):
    for j in a[i]:
        num = j + num
    a[i]=num       
    num=""
print (max(a))
#문자열 역순 읽기 [A:B:C] index A부터 index B까지 C간격