#check if a given num is prime

import math
n=int(input())
if(n<=1):
    print("NOT PRIME NUMBER")
else:
    flag=0
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            flag = 1
            break
    if(flag==0):
        print("PRIME NUMBER")
    else:
        print("NOT PRIME NUMBER")