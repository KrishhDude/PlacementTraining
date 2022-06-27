
'''

Output Format

Print the desired pattern based on the input given by the user.

Sample Input 0

3

Sample Output 0

  A 
 A B 
A B C

========================================================================
n = int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end='')
    for k in range(1,i+1):
        #print("* ",end='')
        print("*",end=' ')
    print()

Input (stdin)

3

Your Output (stdout)

  * 
 * * 
* * * 
==============================================================================
'''

n = int(input())
x='A'
c=ord(x)
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end='')
    for k in range(1,i+1):
        print(chr(ord('A')+k-1), end=" ")
        #print("* ",end='')
        #print("*",end=' ')
    print()
