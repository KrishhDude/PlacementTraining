'''
We have to estimate the cost of painting a property. Interior wall painting cost is Rs. 18 per sq.ft. and exterior wall painting cost is Rs. 12 per sq.ft. If a user enters zero as the number of walls then skip surface area values as user may don’t want to paint that wall and for any wrong input print "Invalid Input".

Input Format

Take input as
1. Number of interior walls 'n'
2. Number of exterior walls 'm'
3. Surface area of each interior wall in units of sq.ft.
4. Surface area of each exterior wall in units of sq.ft.

Constraints

0 <= n <= 10
0 <= m <= 10

Output Format

Calculate and display the total cost of, painting the property in the following format.
Total Estimated Cost: X INR

Sample Input 0

6
3
12.3
15.2
12.3
15.2
12.3
15.2
10.10
10.10
10.00

Sample Output 0

Total Estimated Cost: 1847.4 INR
'''
n=int(input()) #interior
m=int(input()) #exterior

if(0<=n and n<=10 and 0<=m and m<=10):
    nsurf=[]
    msurf=[]
    if n<0 or m<0:
        print("Invalid Input")
        exit()
    for i in range(n):
        nsurf.append(float(input()))
    for j in range(m):
        msurf.append(float(input()))
    if(nsurf and msurf):
        print("Total Estimated Cost:",(sum(nsurf)*18+sum(msurf)*12),"INR")
    else:
        if(nsurf):
            print("Total Estimated Cost:",sum(nsurf)*18,"INR")
        elif msurf:
            print("Total Estimated Cost:",sum(msurf)*12,"INR")        
        else:
            print("Total Estimated Cose: 0.0 INR")
else:
    print("Invalid Input")

'''
n,m = int(input()), int(input())
cost=0
if(n<0 or n>10 or m<0 or m>10):
    print("Invalid Input")
    exit()
for i in range(1,n+1):
    tmp = float(input())
    cost+=tmp*18
for j in range(1,m+1):
    tmp = float(input())
    cost+=tmp*12
print("Total Estimated Cost:","{0:.1f} INR".format(cost))
'''