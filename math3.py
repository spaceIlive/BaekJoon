num= int(input())
n=1
while True:
    if n*(n+1)/2>=num:
        break
    else:
        n=n+1
      
if n>1:    
    if (n%2)==1:
       b= num-((n)*(n-1)/2)
       print('%d/%d' %((n-b+1),(b)))
    else:
        b= num-((n)*(n-1)/2)
        print('%d/%d' %((b),(n-b+1)))
else:
     print('%d/%d' %(1,1))