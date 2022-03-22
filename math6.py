import sys
import math
def prime_list(n):
    sieve= [True]*n

    m=int(math.sqrt(n))
    for i in range(2,m+1):
        if sieve[i]== True:
            for j in range(i+i,n,i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True] #def쓰는게 런타임 훨씬 줄임

a= int(sys.stdin.readline())
b=[]
for i in range(a):
    f=int(sys.stdin.readline())
    b.append(f)
'''sieve=[True]*10000
for i in range(2,101):
    if sieve[i]== True:
        for j in range (2*i,10000,i):
            sieve[j]=False
c=[i for i in range(2,10000) if sieve[i]==True]'''

for i in b:
    d=[j for j in c if int(i/2)<=j<i]
    for j in d:
        if i-j in c:
            print('%d %d'%(i-j,j))
            break 

