'''
Write code for generate the given pattern based on the input given. image

Input Format

In the first line of the input get the value "N" which determines no. of rows in the pattern.

Constraints

1 <= N <= 10

Output Format

Print the pattern

Sample Input 0

1

Sample Output 0

*

Sample Input 1

2

Sample Output 1

 *
**

Sample Input 2

3

Sample Output 2

  *
 **
***


'''
n=int(input())
for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)