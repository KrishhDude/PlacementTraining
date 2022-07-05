'''
Write code for finding the peak elements in an integer array.
[A peak element is the one which is not smaller than its left and right neighboring values. ie. arr[i-1] <= arr[i] => arr[i+1], arr[i] is a peak element.First and Last elements of the array may also be a peak element.For the last and first element only one comparison is needed. An array may have more than one peak element. You have to find all of them.]

Input Format

Input the size N of the integer array in line 1.
Input all the elements of the array in line 2.

Constraints

2 <= N <= 100

Output Format

Print all peak elements in the order of its occurance with a space between them.

Sample Input 0

4
5 10 20 15

Sample Output 0

20

Sample Input 1

5
100 20 100 40 50 

Sample Output 1

100 100 50
'''
ar=[]
n=int(input())
ar=[int(x) for x in input().split()]
peak=[]; l=len(ar)
if(ar[0]>=ar[1]):
    peak.append(ar[0])
for i in range(1,len(ar)-1):
    if(ar[i]>=ar[i-1] and ar[i]>=ar[i+1]):
        peak.append(ar[i])
if(ar[l-1]>=ar[l-2]):
    peak.append(ar[len(ar)-1])
print(*peak)