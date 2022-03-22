"""a=[]
for i in range(9):
    b=int(input())
    a.append(b)
max=a[0]   
for i in range(9):
    if max<a[i]:
        max=a[i]

print(max)
print(a.index(max)+1)""" #배열이용해서 한건데 왜 틀린건지 모르겠음

#좋은 풀이같은거
'''
max_num=0
max_index=0
for i in range(9):
    a=int(input())
    if a>max_num:
        max_num=a
        max_index=i
print(max_num)
print(max_index+1)  '''     

#메서드를 알때(솔직히 나는 이렇게 연습하는거 별로라 생각)
a=[]
for i in range(9):
    b=int(input())
    a.append(b)
print(max(a))
print(a.index(max(a))+1)    



