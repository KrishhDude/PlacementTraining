'''
Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it from and after the most significant bit. Print the positive integer value after toggling all bits”.
Example :

Input : 10 → Integer

Output : 5 → result-Integer

Explanation:
Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.

Input Format

NA

Constraints

1<=N<=100

Output Format

NA

Sample Input 0

10

Sample Output 0

5
'''
n=int(input())
b=bin(n)[2:]
x=str(b)
bx=''
for i in x:
    if i=='0':
        bx=bx+'1'
    else:
        bx=bx+'0'
c=int(bx)
print(int(bx,2))