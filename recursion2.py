def Fibonacci(n):
    result=0
    if n==0:
        result=0
        return result
    elif n==1:
        result=1
        return result
    else:
        result=Fibonacci(n-1)+Fibonacci(n-2)
        return result
a=int(input())
print(Fibonacci(a))            