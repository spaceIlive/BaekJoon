"""a=input()
b=[]
c="abcdefghijklmnopqrstuvwxyz"
d=[]
e=[]
Max=0
count_num=0
for i in c:
    d.append(i)
for i in a:
    b.append(i)
for i in range(len(b)):
    if b[i] in d:
        b[i]= chr(ord(b[i])-32) 
for i in range(len(b)):
    b[i]=ord(b[i])
for i in range(65,91):
    count=0
    for j in range(len(b)):
        if i==b[j]:
            count=count +1    
    e.append(count)

for i in e:  
    if i>Max:
        Max=i
for i in e:
    if Max==i:
        count_num=count_num+1
if count_num==1:
    for i in range(len(e)):
        if e[i]==Max:
            print(chr(ord(d[i])-32))
else:
    print("?")       """         #내가 짠 코드
word = input().upper()
word_list = list(set(word))

cnt=[]
for i in word_list:
    count = word.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
    
else:
    print(word_list[(cnt.index(max(cnt)))])  #백준에서 시간 짧은 코드