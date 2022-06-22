'''
Write code for finding sum of the series given below after accepting the value of 'n' and 'a' as input.
S = 1 + a2 - a4 + a6 - a8 + .... to 'n' terms

Input Format

Get the value of 'n' as input in line 1.
Get the value of 'a' as input in line 2.

Constraints

1 <= n <= 10
2 <= a <= 5

Output Format

Display the final value of 'S' as output.

Sample Input 0

3
2

Sample Output 0

-11

'''

n,a = int(input()), int(input())
s=1; j=2; sign=1
for i in range(2,n+1):
    s=s+sign*a**j
    sign = sign*-1
    j=j+2
print(s)