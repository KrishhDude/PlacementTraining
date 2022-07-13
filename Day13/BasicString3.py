'''Write code for finding whether the given input word is a palindrome word or not.
A string is said to be palindrome if reverse of the string is same as string.
For example, “abba” is palindrome, but “abbc” is not palindrome.
Note :
You are not allowed to use any inbuilt function or shortcut for reversing the given string.

Input: Malayalam
Output: PALINDROME

Input Format

Enter the string of length "N" for which the palindrome checking has to be performed.

Constraints

1 <= N <= 25

Output Format

Check the input and print "PALINDROME" if the it is a palindrome word, otherwise print "NOT PALINDROME"

Sample Input 0

MalayalaM

Sample Output 0

PALINDROME
'''

a=input().upper()
flag=0
for i in range(len(a)//2):
    if a[i]==a[len(a)-i-1]:
        continue
    else:
        print("NOT PALINDROME")
        flag=1
        break
if flag==0:
    print("PALINDROME")
