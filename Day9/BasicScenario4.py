'''
Constraints

1 <= P <= 107

Output Format

Output all the divisors of P separated by a space in the increasing order.

Sample Input 0

10

Sample Output 0

1 2 5 10

Sample Input 1

-10

Sample Output 1

Wrong Input
'''
n=int(input())
if n<1 or n>10**7:
    print("Wrong Input")
else:
    for i in range(1,n+1):
        if(n%i==0):
            print(i, end=' ')