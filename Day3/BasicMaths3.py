#Write code for checking whether the given number is palindrome or not.
N=int(input())
n=N
rev=0
while N!=0:
    digit=N%10
    rev=(rev*10)+digit
    N=N//10
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")