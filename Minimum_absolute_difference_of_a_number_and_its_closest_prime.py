import math as m
def p(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def mp(n):
    t=n
    for i in range(n,0,-1):
        if p(i):
            t1=i
            break
    while True:
        if p(t):
            t2=t
            break
        else:
            t+=1
    d1=n-t1
    d2=t2-n
    return min(d1,d2)
num=int(input())
print(mp(num))
