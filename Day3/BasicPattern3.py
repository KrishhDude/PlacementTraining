'''
Noble was asked by the Karunya administration to design a new logo for Karunya. After thinking a lot he came with a logo
image Now he wants you to help him design a program that generates the given logo in all official papers depending on the value N. Write a program to design the logo.

Input Format

N value should be taken as input in the first line.

Constraints

3<=N<=10

Output Format

The logo should be printed based on the value N

Sample Input 0

3

Sample Output 0

***
**
*
**
***

'''
N=int(input())
for i in range(N+1,1,-1):
    for j in range(i,1,-1):
        print('*',end='')
    print()  
for i in range(2,N+1):
    for j in range(-1,i-1):
        print('*',end='')
    print()

'''
#first half
for i in range(1,n+1):
    for j in range(1,n-i+1+1):
        print('*',end='')
    print()

#second half
for i in range(2,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
'''