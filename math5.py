T= int(input())
'''a=[]
for i in range(T):
    H,W,N=map(int,input().split())
    n=1
    for j in range(100):
        if n*H < N <= H*(n+1):
            a.append([N-H*n,n+1])
            break
        else:
            n=n+1    
for i in range(T):
    print('%d0%d' %(a[i][0],a[i][1]))'''
a=[]
for i in range(T):
    H,W,N=map(int,input().split())
    if (N/H-N//H)==0:
        n=int(N//H-1)
        a.append([N-H*n,n+1])
    else:
        n=int(N//H)
        a.append([N-H*n,n+1])
for i in range(T):
    print('%d0%d' %(a[i][0],a[i][1]))   #아 시바 백준 ㅂㅅ같은 프로그램이 이 좋은 코딩을 못알아 쳐먹음

#여기서부터다른코드
T=int(input())

for i in range(T):
    h,w,n=map(int, input().split())

    floor=n%h
    room_line=(n//h)+1
    if floor ==0:
        floor = h
        room_line-=1

    print(floor*100+room_line)    
