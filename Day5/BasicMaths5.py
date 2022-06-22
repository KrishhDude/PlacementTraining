'''
Write code for checking whether the 2 given numbers are amicable pair or not.
The smallest pair of amicable numbers is (220, 284). They are amicable because the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; and the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.

Input Format

Enter the first number M in the first line of input. Enter the second number N in the second line of input.

Constraints

1 <= M <= 100000
1 <= M <= 100000

Output Format

Print whether the given pair of numbers are Amicable or not in the below format.
"Amicable"
"Not Amicable"

Sample Input 0

220
284

Sample Output 0

Amicable


'''

n,m = int(input()), int(input())
nsum=0; msum=0;
for i in range(1,(n//2)+1):
    if(n%i)==0:
        nsum+=i
for i in range(1,(m//2)+1):
    if(m%i)==0:
        msum+=i
if nsum==m and msum==n:
    print("Amicable")
else:
    print("Not Amicable")