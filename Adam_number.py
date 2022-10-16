n1=int(input())
s1=n1**2
n2=str(n1)
n2=n2[::-1]
n2=int(n2)
s2=n2**2
s1=str(s1)
s2=str(s2)
if s1==s2[::-1]:
    print(True)
else:
    print(False)