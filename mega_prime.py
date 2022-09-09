def fun(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
s=len(str(n))
v=0
if fun(n)==0:
    print("Not Mega Prime")
else:
    while n>0:
        r=n%10
        n=n//10
        if fun(r)==0:
            print("Not Mega Prime")
            break
        else:
            v+=1
if v==s:
    print("Mega Prime")