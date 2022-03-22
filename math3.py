import math
def find_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i)==0:
            return False  
    return True                 # n = 2 일때 range가 말이 안돼서 for 문이 안돌아가 true가 나오나 >> 그런듯
N=int(input())
prime_list=[]
for i in range(2,N):
    if find_prime(i)==True:
        prime_list.append(i)
    else: pass

'''for i in range(len(prime_list)):
    n=1
    if N%(prime_list[i])==0:
        while (N%(pow(prime_list[i],n))) == 0:
            print(prime_list[i])
            n=n+1    
    else: pass  '''                         #이부분만 좀 바꿈
for i in range (len(prime_list)):
    if N%prime_list[i]==0:
        while N%prime_list[i]==0:
            print(prime_list[i])
            N=int(N/prime_list[i])    

'''import math
n=int(input())   
if n==1:
    print('')
elif n==2:
    print(2)    
else :
    for i in range(2,n):
        if n%i==0:
            while n%i==0:
                print(i)
                n=int(n/i)     '''