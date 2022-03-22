"""a= input()
list=[]
for i in a:
    list.append(i)
count=0    
for i in range(len(list)):
    if list[i]=='=':
        continue
    elif list[i]=='-':
        continue
    elif list[i]=='j':
        if i>0 :
            if list[i-1]=='n' or list[i-1]=='l':
                continue
            else:
                count=count+1
                continue
        else:
            count=count+1
            continue
    elif list[i]=='z':
        if i>0:
            if list[i-1]=='d' and list[i+1]=='=':
                continue
            else:
                count=count+1
                continue
        else:
            count=count+1  
            continue
    else:
        count=count+1
        continue

print(count)                """ #런타임 에러 뜸 왜 뜨는지는 모르겠는데 시바 짜증남
# replace 함수 써야하는듯 시발
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
a= input()
for i in croatia:
    a=a.replace(i,'a')
print(len(a))    