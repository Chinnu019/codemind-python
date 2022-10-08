n=int(input())
for i in range(n):
    a=int(input())
    t=a
    b=int(a**0.5)
    if b*b==t:
        print("True")
    else:
        print("False")