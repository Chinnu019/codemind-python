n=input()
ec=0
oc=0
for i in n:
    if int(i)%2==0:
        ec+=1
    else:
        oc+=1
if ec==len(n):
    print("Even")
elif oc==len(n):
    print("Odd")
else:
    print("Mixed")