import sys
a=int(input())
b=list(map(int,sys.stdin.readline().split()))
minimum=b[0]
maximum=b[0]
for i in range(a):
    if b[i]<minimum:
        minimum=b[i]    

for i in range(a):
    if b[i]>maximum:
        maximum=b[i]

print("{} {}".format(minimum,maximum))                     
