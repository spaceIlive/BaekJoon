A,B,V= map(int, input().split())
#day=1
'''while True:
    if V<=(A+(A-B)*(day-1)):
        print(day)
        break
    else:
        day+=1     '''          #이렇게 하면 숫자 커지면 너무 오래걸림
if (1+((V-A)/(A-B)))-(1+((V-A)//(A-B)))!=0 :
    print (2+((V-A)//(A-B)))
else:
    print(int(1+((V-A)/(A-B))))            