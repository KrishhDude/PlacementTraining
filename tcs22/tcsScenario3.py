'''
An automobile company manufactures both two wheelers(TW) and four wheelers(FW). A company manager wants to make the production of both type of vehicles according to the given data below:
1st data; Total number of vehicles (two-wheeler + four-wheeler) = v
2nd data; Total number of wheels = w
The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.

Input Format

Print “INVALID INPUT”, if inputs did not meet the constraints.
The candidate has to write the code to accept two positive numbers separated by a new line.
First Input line - Accept value of v.
Second Input line- Accept value for w.

Constraints

2<=w
w%2=0
v < w

Output Format

The code should generate two outputs, each separated by a single space character(see the example).
Additional messages in the output will result in the failure of test case.

Sample Input 0

200
540

Sample Output 0

TW=130 FW=70

Explanation 0

130+70 = 200 vehicles
(130x2)+(70x4)= 540 wheels
'''
v,w=int(input()), int(input())
if(w<2 or w%2!=0 or v>=w):
    print("INVALID INPUT")
    exit()
else:
    y=int((w-2*v)/2)
    x=int(v-y)
print('TW=',x," FW=",y,sep="")