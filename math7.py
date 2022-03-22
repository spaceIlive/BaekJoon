N=int(input())
if N%5==0:
    print(N//5)
elif N%5==1:
    if N//5==0:
        print(-1)
    else:
        print((N//5)+1)
elif N%5==2:
    if N//5==0 or N//5==1:
        print(-1)
    else :
        print(N//5+2)
elif N%5==3:
    print(N//5+1)
else:
    if N//5==0:
        print(-1)
    else :
        print(N//5+2)                    