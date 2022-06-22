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