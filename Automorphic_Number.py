n=int(input())
t=n
m=n*n
s=0
c=0
x=0
while n!=0:
    s+=1
    n//=10
for i in range(s):
    r=m%10
    c=c*10+r
    m=m//10
while c!=0:
    r=c%10
    x=x*10+r
    c=c//10
if x==t:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

