'''
There is a jar full of candies for sale at a mall counter. Jar has the capacity t, that is jar can contain maximum t candies when jar is full. At any point of time, jar can have k number of candies where k<=t. Candies are served to the customers and jar never remains empty. As and when last n candies are sold, jar is refilled with new candies in such a way that jar gets full.
Write a code to implement above scenario. Display jar at counter with available number of candies. Input should be the number of candies one customer can order at a point of time. Update the jar after each purchase and display jar at counter.

Output should give the number of candies sold and updated number of candies in jar.

If input is more than candies in jar, return: “INVALID INPUT”

Given,

t=10, where t is number of candies available

k >= 5, where k is number of minimum candies that must be inside jar ever.If any purchase violates this condition may leads to print "INVALID INPUT".

Input Format

Input the value of the variable 'n' as the no. of candies sold.

Constraints

10<=t<=10

Output Format

Example 1:(t=10, k>=5)

Input:
3
Output:
NUMBER OF CANDIES SOLD: 3
NUMBER OF CANDIES LEFT: 7

Example 2:(t=10, k>=5)

Input:
0
Output:
INVALID INPUT
NUMBER OF CANDIES LEFT: 10

Sample Input 0

3

Sample Output 0

NUMBER OF CANDIES SOLD: 3
NUMBER OF CANDIES LEFT: 7

Sample Input 1

0

Sample Output 1

INVALID INPUT
NUMBER OF CANDIES LEFT: 10
'''
n=int(input())
if(n>0 and n<=5):
    print("NUMBER OF CANDIES SOLD:", n)
    print("NUMBER OF CANDIES LEFT:", 10-n)
else:
    print("INVALID INPUT")
    print("NUMBER OF CANDIES LEFT: 10")
'''
n=int(input())
if(n,=0 or n>5):
    print("invalid input")
    print(10 left)
else:
    print(number sold: n)
    print(number left: 10-n)
'''