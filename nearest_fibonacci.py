n=int(input())
l=[0,1]
a=0
b=1
c=0
for i in range(n):
    c=a+b
    l.append(c)
    a=b
    b=c
l1=[]
l2=[]
for i in l:
    if i>n:
        l2.append(i)
    else:
        l1.append(i)
t1=l1[-1]
t2=l2[0]
r1=n-t1
r2=t2-n
if r1==r2:
    print(t1,t2)
elif r1>r2:
    print(t2)
else:
    print(t1)
