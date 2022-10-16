n=input()
c=1
s=0
for i in n:
    s+=int(i)**c
    c+=1
if s==int(n):
    print(True)
else:
    print(False)