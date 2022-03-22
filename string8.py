a=input()
b=[[1,""],[2,"ABC"],[3,"DEF"],[4,"GHI"],[5,'JKL'],[6,'MNO'],[7,'PQRS'],[8,'TUV'],[9,'WXYZ']]
time=0
for i in a:
    for j in range(9):
        if i in b[j][1]:
            time= time+j+2
print(time)            