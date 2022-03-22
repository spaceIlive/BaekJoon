def solve():
    a=[]
    b=[]
    c=[]
    for i in range(1,10000):
        a.append(i)
    for i in range(10000):
        if (1<= i <10):
            b.append(2*i)
        elif (10<= i < 100):
            b.append((i//10)+(i%10)+i)
        elif (100<= i <1000):
            b.append((i//100)+((i//10)%10)+(i%10)+i)
        else :
            b.append((i//1000)+((i//100)%10)+((i//10)%10)+i%10+i)
    for i in a:
        if i not in b:
            c.append(i)
    for i in c:
        print(i)
solve()    