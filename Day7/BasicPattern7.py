'''
Write code for generate the given pattern based on the input.The input given by the user determines how many rows are there in the pattern.If the input is 4, the below given pattern should be printed.
image
NOTE: Once the upper limit of capital alphabets is reached(means after "Z"), the pattern should continue, by again starting from the lower limit of capital alphabets(means from "A").

Input Format

In the first line of input get the value 'n' which determines the no. of rows are there in the pattern.

Constraints

2 <= n <= 25

Output Format

Print the desired pattern based on the input given by the user.

Sample Input 0

3

Sample Output 0

  A
 B C
DEFGH

=============================================================
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end='')
    for k in range(1, 2*i): #((2*i+1)-1) = 2*i
        if(k==1 or k==2*i-1 or i==n):
            print("*", end='')
        else:
            print(" ", end='')
    print()



    Custom TestcaseCorrectness of code is not checked for custom test case. The generated output is displayed below.

Compilation Successful

Input (stdin)

4

Your Output

   *
  * *
 *   *
*******

'''

n=int(input())
#x=ord('A')
inc=0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end='')
    for k in range(1, 2*i):
        if(k==1 or k==2*i-1 or i==n):
            #print(chr(x), end="")
            print(chr(65 + inc), end='')
            inc = (inc+1)%26
            #x+=1
        else:
            print(" ", end='')
    print()