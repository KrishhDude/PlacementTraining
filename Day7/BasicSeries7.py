'''
Write code for finding the sum of series given below after getting the value of 'n' as input.

S= (1*2)/(1+2) + (2*3)/(2+3) + (3*4)/(3+4) + .....

Input Format

Get the value of 'n' as input in line 1.

Constraints

1 <= n <= 1000

Output Format

Display the final value of 'S' as output.
Print the output with a 5 digit precision after decimal point.
Precision of floating point numbers is the accuracy upto which a floating point number can hold the values after decimal.

Sample Input 0

2

Sample Output 0

1.86667


'''


n=int(input())
sum=0; i=1; j=2
for i in range(i,n+1):
    sum+=(i*j)/(i+j)
    i+=1
    j+=1
print("{0:.5f}".format(sum))