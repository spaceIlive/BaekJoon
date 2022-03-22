def solve(n) :
    a=[]
    for i in range(1,n+1):
        if i<100:
            a.append(i)
        elif i<=1000:
            if ((i//100)-((i//10)%10))!=(((i//10)%10)-i%10):
                pass
            else :
                a.append(i)

    return(len(a))
n= int(input())               
print(solve(n))