fix, pay, profit= map(int,input().split())

if profit-pay>0:
    print(fix//(profit-pay)+1)
else:
    print("-1")    