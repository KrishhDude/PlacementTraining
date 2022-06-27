'''
Write code for finding the sum of series given below after accepting the value of 'n' as input.

S = 2/7 - 5/11 + 8/15 - 11/19 + ....

Input Format

Get the value of 'n' as input in line 1.

Constraints

1 <= n <= 100

Output Format

Display the final value of 'S' as output.
Print the output with 6 digit precision after decimal point.

Sample Input 0

2

Sample Output 0

-0.168831


'''

n = int(input())
sum=0; j=2; k=7; sign=1
for i in range(1,n+1):
    sum=sum+sign*(j/k)
    j=j+3
    k=k+4
    sign=sign*-1
print("{0:.6f}".format(sum))

#0 in {0:.6f} is the index of value inside paranthesis of sum
#that is if i give 2 values inside format, format(a,b),
#to format a, i give 0. to format b, i give 1