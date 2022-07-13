'''
Write code for finding the minimum and maximum value from an integer array of size "N" without sorting or using any inbuilt functions.
Sample Array: 1 2 3 4 5 6 7 8 9 10
Output
1 10

Input Format

Get the size of the array as input in line 1. Get the array as input in line 2.

Constraints

1 <= N <= 25

Output Format

Output the Minimum and Maximum value from the input array with a space between them.

Sample Input 0

5
10 40 30 20 50

Sample Output 0

10 50
'''
n=int(input())
l=[int(x) for x in input().split()]
low=l[0]; max=l[0]
for i in range(n):
    if l[i]<low:
        low=l[i]
    if l[i]>max:
        max=l[i]
print(low, max)
