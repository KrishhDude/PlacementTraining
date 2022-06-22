'''
Write code for generate the given pattern based on the input.The input given by the user determines how many stars are there in the middle row.If the input given is 4, the below given pattern should be printed.

image

Input Format

In the first line of the input, get the value "N" which determines the no. of stars in the middle row.

Constraints

2 <= N <= 15

Output Format

Print the desired pattern based on the input given by the user.

Sample Input 0

3

Sample Output 0

  *
 **
***
 **
  *


'''n=int(input())
for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
for j in range(n-1,0,-1):
    print((" ")*(n-j)+("*"*j))