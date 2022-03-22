"""a=int(input())
e=[]
for i in range(a):
    b=list(map(str,input().split()))
    b[0]=int(b[0])
    c=[]
    d=""
    
    for j in range(b[0]):
        c=list(b[1])
        
    for k in range(len(c)):
        d+=str(c[k])*b[0]
    e.append(d)
for i in range(a):
    print(e[i])   """       #내풀이
        
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ""
    for i in s :
        text += int(num) *i
    print(text)                 #다른사람 짧은 풀이인데
                                #여기서 안 사실: split해서 받은 문자열은 for문에서 문자 하나씩 선언 가능하다
