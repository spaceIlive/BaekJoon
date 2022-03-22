'''import sys
N=int(sys.stdin.readline())
Factorial=1
if N==0:
    print(1)
else:
    for i in range(1,N+1):
        Factorial=Factorial*i
    print(Factorial) '''            #for문이고 밑에는 재귀함수 이용
def Fac(n):
    result=1
    if n>1:
        result= n*Fac(n-1)
        return result
    else:
        return result
N=int(input())
print(Fac(N))        

