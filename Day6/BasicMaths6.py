#Finding the factorial of a given number.

from math import factorial
n=int(input())
sum=1
while n!=0:
    sum=sum*n
    n=n-1
print(sum)

#with built-in function
n=int(input())
print(factorial(n))

#with user-defined fn
def FACT(x):
    fact=1
    while x!=0:
        fact=fact*x
        x=x-1
    return fact
n=int(input())
print(FACT(n))

#with recursion
def fac(x):
    if(x==0):
        return 1
    else:
        return x*fac(x-1)
n=int(input())
print(fac(n))