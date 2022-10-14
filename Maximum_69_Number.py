a=input()
l1=[]
for char in a:
    l1.append(int(char))
l1.sort(reverse=True)
if 6 in l1:
    i=l1.index(6)
    l1[i]=9
s=""
for item in l1:
    s+=str(item)
print(s)
    