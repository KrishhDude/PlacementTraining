def LCM(x: int, y: int) -> int:
    if x>y:
        big=x
    else:
        big=y
    while(True):
        if(big%x==0 and big%y==0):
            return big
            break
        big+=1
    pass