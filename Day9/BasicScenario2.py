#calculate area of circle. radius should be less than 30 and greater thatn 20

r=float(input())
pi=3.1415
if(r<20 or r>30):
    print("Wrong Input")
else:
    a=pi*r*r
    print("Area =", "{0:.3f}".format(a))