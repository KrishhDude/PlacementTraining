def sumOfEvenOdd(num):
    evenSum,oddSum = 0,0
    while(num != 0):
        dig=num%10
        if(dig%2==0):
            evenSum+=dig
        else:
            oddSum+=dig
        num=num//10
    return [evenSum, oddSum]
    pass
