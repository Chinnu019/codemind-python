n=int(input())
t1=n
t2=n
while True:
    t1+=1
    t1=str(t1)
    if t1==t1[::-1]:
        r1=t1
        break
    else:
        t1=int(t1)
while True:
    t2-=1
    t2=str(t2)
    if t2==t2[::-1]:
        r2=t2
        break
    else:
        t2=int(t2)
d1=int(r1)-n
d2=n-int(r2)
if d1==d2:
    print(r2,r1)
elif d1>d2:
    print(r2)
else:
    print(r1)