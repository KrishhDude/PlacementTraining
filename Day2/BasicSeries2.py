'''
Write code for finding the sum of series given below by accepting the value of 'N' as input.
S = 2 + 5 + 10 + 17 + 26 + 37 + 50 . . . . to 'N' terms

Input Format

Get the value of 'N' as input in line 1.

Constraints

2 <= N <= 100

Output Format

Display the value of 'S' as output.
'''
N=int(input())
i=1
S=0
while(i<=N):
    S=S+(i*i)+1
    i+=1
print(S)