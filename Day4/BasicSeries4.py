n,a = int(input()), int(input())
s=1; j=2; sign=1
for i in range(2,n+1):
    s=s+sign*a**j
    sign = sign*-1
    j=j+2
print(s)