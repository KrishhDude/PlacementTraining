'''
Write code for finding the index of the first occurance of the given character in a string without using any inbuilt function.

Input Format

Enter the input string of length N in the 1st line.
Enter the character needs to be searched in the second line.

Constraints

1<=N<=100

Output Format

Output the index of the first occurrance of the given character in the string. Print "-1" if the character is not available in the string.

Sample Input 0

I love programming
p

Sample Output 0

8

Sample Input 1

I am going to get a very good job
p

Sample Output 1

-1
'''
ar=input()
c=input()
flag=0
for i in range(len(ar)):
    if ar[i]==c:
        print(i+1)
        flag==1
        exit()
if flag==0:
    print(-1)