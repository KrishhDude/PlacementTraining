'''
Write code for finding the sum of the series given below after accepting the value of 'N' as input.
S = 1 + (1+2) + (1+2+3) + (1+2+3+4) + .......+ (1+2+3+.......N)

Input Format

Get the value of 'N' as input in line 1.

Constraints

1 <= N <= 100

Output Format

Display the final value of 'S' as output.

Sample Input 0

3

Sample Output 0

10


'''

n=int(input())
sum=0
for i in range(1,n+1):
    for j in range(i+1):
        sum=sum+j
print(sum)

#the series is summation of (sum of n numbers) n times
#the original code is O(n^2) complexity
#rewritingin O(n) complexity

n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+(i*(i+1))//2
print(sum)

#rewriting in O(1) complexity
n=int(input())
sum=(n*(n+1)*(n+2))//6
print(sum)