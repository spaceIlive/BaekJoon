num= int(input())
count=int(0)


for i in range(num):
    err=int(0)
    voca= input()
    alpha=[]
    for j in range(len(voca)):
        if j>=1:
            if voca[j]!=voca[j-1]:
                alpha.append(voca[j])
            else:
                continue
        else:
            alpha.append(voca[j])       #alpha라는 연속된 문자열을 없애고 남은 array 만드는코드

    for i in range(len(alpha)):
        for j in range(i+1,len(alpha)):
            if alpha[i]==alpha[j]:
                err=err+1
                break
            else :
                continue
        if err!=0:
            break                       #alpha에서 같은 문자가 있을시에 err숫자 올라가는 구조

    if err==0:
        count=count+1
    else:
        continue                              
print(count)

