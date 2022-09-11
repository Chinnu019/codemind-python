A,B,C=map(int,input().split())
t=(A+B+C)/2
s=(t*(t-A)*(t-B)*(t-C))**0.5
print("%0.2F"%s)