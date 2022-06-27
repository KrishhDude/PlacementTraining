'''
There are total n number of monkeys sitting on the branches of a huge tree. As travellers offer bananas and peanuts, the monkeys jump down the tree. Every monkey can eat k bananas or j peanuts. If total m number of bananas and p number of peanuts are offered by travellers, calculate how many monkeys remain on the tree after some of them jumped down to eat. At a time one monkey gets down and finishes eating and go to the other side of the road. The monkey who climbed down does not climb up again if its stomach is filled. Monkey can either eat k bananas or j peanuts. If for last monkey there are less than k bananas left on the ground only that monkey can eat bananas less than k along with less than j peanuts, only if both can togetherly satisfy its hunger.
Write code to take inputs as n, k, j, m, p and return the number of monkeys left on the tree. Where,
n = Total no of monkeys
k = Number of bananas eatable by single monkey(Monkey that jumped down last may get less than k bananas)
j = Number of peanuts eatable by single monkey(Monkey that jumped down last may get less than j peanuts)
m = Total number of bananas
p = Total number of peanuts
Remember that the monkeys always eat Bananas and Peanuts, so there is no possibility of k and j having a value zero.

Input Format

Accept the input n in the first line.
Accept the input k in the second line.
Accept the input j in the third line.
Accept the input m in the fourth line.
Accept the input p in the fifth line.

Constraints

n>0
k>0
j>0
m>=0
p>=0

Output Format

For any wrong input display
"INVALID INPUT"
For valid inputs display
Number of monkeys left on the tree: x

Sample Input 0

20
2
3
12
12

Sample Output 0

Number of monkeys left on the tree: 10

Sample Input 1

20
5
5
14
14

Sample Output 1

Number of monkeys left on the tree: 15
'''

n=int(input()); k=int(input()); j=int(input())
m=int(input()); p=int(input()) 
#n monkeys, k bananas and j peanuts eatable
#m total banana, p total peanuts
if(n<=0 or k<=0 or j<=0 or m<0 or p<0):
    print("INVALID INPUT")
else:
    bmonk = m/k
    pmonk = p/j
    ate = int(bmonk + pmonk)
    mremaining = n-ate
    if mremaining<0:
        print("Number of monkeys left on the tree:",0)
    else:
        print("Number of monkeys left on the tree:",mremaining)