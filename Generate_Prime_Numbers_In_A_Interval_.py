import math
def fun(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if fun(i):
        print(i)