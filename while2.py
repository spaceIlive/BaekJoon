a=0
b=int(input())
stac=b
while True:
    a=a+1
    c=b%10
    d=(b//10)+(b%10)
    e=d%10
    b=c*10+e
    if b==stac:    
        print(a)
        break
    