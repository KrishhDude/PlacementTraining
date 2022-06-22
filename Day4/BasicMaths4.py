'''
Write code for finding the GCD or HCF and LCM of given 2 numbers.

Input Format

Enter the first number M in the first line of input.
Enter the second number N in the second line of input.

Constraints

1<= M <=10000
1<= N <=10000

Output Format

For eg. the output should be printed as follows..
"HCF=10 LCM=2"

Sample Input 0

9
12

Sample Output 0

HCF=3 LCM=36


'''
m,n = int(input()),int(input())
min_num = min(m,n)
for i in range(min_num, 0, -1):
    if(m%i == 0 and n%i == 0):
        gcd = i; break
print("HCF={} LCM={}".format(gcd,m*n//gcd))