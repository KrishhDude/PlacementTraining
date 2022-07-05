'''
Write a program to check whether two given strings are anagram of each other or not. An anagram of a string is another string of same length and contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other."silent" and "listen" are also anagram of each other.

Input Format

Enter the first string of length "m" in the first line as input.
Enter the second string of length "n" in the second line as input.

Constraints

1 <= m <= 20
1 <= n <= 20

Output Format

Print "YES" if the two strings are anagram of each other. Otherwise print "NO".

Sample Input 0

cat
act

Sample Output 0

YES

Sample Input 1

listen
silent

Sample Output 1

YES

'''
a=str(input())
b=str(input())
x=''.join(sorted(a))
y=''.join(sorted(b))
if(len(a)==len(b) and x==y):
    print("YES")
else:
    print("NO")