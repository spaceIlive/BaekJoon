import sys

def hanoi_num(n):
    if n==1:
        result=1
        return result
    else:
        result=hanoi_num(n-1)*2+1
        return result
def hanoi_position(n,start,mid,end):
    if n==1:
        print('%d %d' %(start, end))
    else:
        hanoi_position(n-1,start,end,mid)
        print('%d %d' %(start, end))
        hanoi_position(n-1,mid,start,end)
        
                                                #제일 인상 깊었던 문제 가장 오래걸리고 생각도 많이 했던것 같다.

            
n=int(sys.stdin.readline())
print(hanoi_num(n))
hanoi_position(n,1,2,3)
