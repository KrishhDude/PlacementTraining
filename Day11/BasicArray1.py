'''
Write code for reversing any given integer array of size N without using another array.
Note :
Don't try to print the array in reverse order.
You are not allowed to use any inbuilt function for reversing the given array.
You have to convert the given array by storing the numbers in reverse order.

Input Format

Get the size of the array as input in line 1.
Get the array as input in line 2

Constraints

1<=N<=100

Output Format

Output the integer array of size N in reverse order.

Sample Input 0

5
1 2 3 4 5

Sample Output 0

5 4 3 2 1
'''

ar=[]
n=int(input())
ar=[int(x) for x in input().split()]
l=0; h=len(ar)-1
for i in range(len(ar)//2):
    tmp=ar[l]
    ar[l]=ar[h]
    ar[h]=tmp
    l+=1; h-=1
print(*ar)
