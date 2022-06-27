n = int(input())
sum=0; j=2; k=7; sign=1
for i in range(1,n+1):
    sum=sum+sign*(j/k)
    j=j+3
    k=k+4
    sign=sign*-1
print("{0:.6f}".format(sum))