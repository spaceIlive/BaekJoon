import math
import sys
ans=[]
Test_case=int(sys.stdin.readline())
for i in range(Test_case):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    if abs(x2-x1)+abs(y2-y1)==0:
        if r1==r2:
            ans.append(-1)
        else:
            ans.append(0)    
    else:
        if math.sqrt((x1-x2)**2+(y1-y2)**2)==(r2+r1):
            ans.append(1)
        elif math.sqrt((x1-x2)**2+(y1-y2)**2)>(r2+r1):
            ans.append(0)
        elif abs(r2-r1)<math.sqrt((x1-x2)**2+(y1-y2)**2)<r2+r1:
            ans.append(2)
        else:
            ans.append(0)
for i in range(len(ans)):
    print(ans[i])                    