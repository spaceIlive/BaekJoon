examnum = int(input())
scorelist = list(map(int,input().split()))
maxscore = scorelist[0]
for i in range(examnum):
    if maxscore<scorelist[i]:
        maxscore=scorelist[i]
for i in range(examnum):
    scorelist[i]=scorelist[i]/maxscore*100
sum=0    
for i in range(examnum):
    sum = sum + scorelist[i]
average = sum / examnum
print(average)