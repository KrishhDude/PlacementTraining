'''
Write code for finding the sum of series given below.
S = 1 - 4 + 9 - 16 + .....to 'N' terms

'''
N=int(input())
s=1
sum=0
for i in range(N):
    sum=sum+((-1)**i)*(s*s)
    i+=1
    s+=1
print(sum)