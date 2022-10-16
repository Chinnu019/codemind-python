import math as m
def fun(n):
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
n1=str(n)
n1=int(n1[::-1])
if fun(n) and fun(n1):
    print("circular prime")
elif fun(n) or fun(n1):
    print("prime but not a circular prime")
else:
    print("not prime")
        