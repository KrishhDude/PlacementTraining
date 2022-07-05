def printPattern(n):
    s=1
    for i in range(1,n+1):
        print((" "*(n-i))+("*"*s))
        s+=2
'''
for n =4:
   *
  ***
 *****
*******
'''