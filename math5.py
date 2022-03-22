'''import math
def find_prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i)==0:
                return False    
Test_case=[]
while True:
    a=int(input())
    if a!=0:    
        Test_case.append(a)
    else:
        break
for i in Test_case:
    n=0
    for j in range(i,2*i+1):
        if find_prime(j)!=False:
            n=n+1
        else: pass
    print(n)'''                     #이거 시간초과뜸
'''import math

while True:
    a=int(input())
    if a==0: 
        break
    n=0
    for i in range(a,2*a+1):
        if i==1:
            continue
        elif i==2:
            n+=1    
        else:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    break    
                else:
                    n=n+1
    print(n)                    '''    #이것도 시간초과
'''import math
def find_prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i)==0:
                return False 
a=[]
b=[]        
for i in range(1,2*123456+1):
    if find_prime(i)!=False:
        a.append(i)

while True:
    n=int(input())
    if n==0:
        break
    else:
        b.append(n)

for i in a:
    

    for j in range(i,2*i+1):
        if j in a:
            n=n+1
            
        else:
            continue
    print(n) '''               #리스트에 싹다 저장하고 풀었는데 이것도 시간초과, 그래서 에라토스테네스의 체 이용
import sys
import math
def prime_list(n):
    sieve= [True]*n

    m=int(math.sqrt(n))
    for i in range(2,m+1):
        if sieve[i]== True:
            for j in range(i+i,n,i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]

a=[]
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    else:
        a.append(n)
       
for i in a:
    if i==1:
        print(1)
    else:
        answer=[num for num in prime_list(2*i) if num>i]
        print(len(answer))