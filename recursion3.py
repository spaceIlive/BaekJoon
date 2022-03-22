'''import sys 
sys.setrecursionlimit(10**6) 
def append_star(LEN): 
    if LEN == 1: 
        return ['*'] 
    Stars = append_star(LEN//3) 
    L = [] 
    
    for S in Stars: L.append(S*3) 
    for S in Stars: L.append(S+' '*(LEN//3)+S) 
    for S in Stars: L.append(S*3) 
    
    return L 
    
n = int(sys.stdin.readline().strip()) 
print(append_star(n))
print('\n'.join(append_star(n)))'''

def Star(n):
    if n==1: 
        result=['*']
        return result
    else:
        result=[]
        for i in Star(n//3):
            result.append(i*3)
        for i in Star(n//3):
            result.append(i+' '*(n//3)+i)
        for i in Star(n//3):
            result.append(i*3)
        return result
N=int(input())
print("\n".join(Star(N)))                         


