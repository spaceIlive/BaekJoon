number = []
#count = 0
for i in range (10):
    a=(int(input()))%42
    number.append(a)            #여기서 메소드를 안다면 1.중복되는 리스트 원소를 제거하는 메소드 사용 후 2.아래 식 이용
'''for i in range(len(number)):    
    for j in range(42):
        if number[i] == j
            count=count+1'''
b=[]
for i in range (42):
    b.append(i)
c=[]                                #이게 set함수 쓰는 과정인듯
for i in range(42):
    count=0
    for j in range(len(number)):
        if b[i]==number[j]:
            c.append(b[i])
            break
print(len(c))