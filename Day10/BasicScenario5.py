'''
Display sequence of Fibonacci series based on the count given by user and count total even numbers and odd numbers in that series except zero.
Fibonacci series should start with 1.
Total count of even numbers should be displayed in the first row and odd numbers should be displayed in the next row.
The count given by user for Fibonacci series should be greater than 5 and less than or equal to 20, otherwise display "INVALID INPUT".
If the count given by the user is space or character display “INVALID INPUT”.The text message displayed should be in exact format as it is case sensitive.

Input Format

Get the count 'c' of fibonacci numbers to be displayed.

Constraints

5 < c <= 20

Output Format

In the first line output the fibanocci numbers with a space between each fibanocci number.
In the second line output the count of even fibonacci numbers.
In the third line output the count of odd fibonacci numbers.

Sample Input 0

7

Sample Output 0

1 1 2 3 5 8 13
2
5
'''
try:
    n=int(input())
except:
    print("INVALID INPUT")
    exit()
f0 =0; f1=1; fn=1; even=0; odd=0
if(n<=5 or n>20):
    print("INVALID INPUT")
else:
    for i in range(1, n+1):
        print(f1,end=' ')
        if(f1%2==0):
            even+=1
        else:
            odd+=1
        f0=f1; f1=fn; fn=f0+f1
    print()
    print(even)
    print(odd)
