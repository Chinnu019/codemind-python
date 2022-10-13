n=input()
t="0123456789"
s=0
for i in n:
    if i in t:
        s+=int(i)
print(s)