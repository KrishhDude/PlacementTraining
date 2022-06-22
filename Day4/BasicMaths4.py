m,n = int(input()),int(input())
min_num = min(m,n)
for i in range(min_num, 0, -1):
    if(m%i == 0 and n%i == 0):
        gcd = i; break
print("HCF={} LCM={}".format(gcd,m*n//gcd))