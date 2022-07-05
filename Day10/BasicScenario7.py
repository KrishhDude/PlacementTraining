'''
There is a bucket of water, with a capacity of x litres. It is supposed to fill with a mug of y litres water capacity. Say for example x=100 and y=10, then the bucket will get full of a minimum of 8 mugs(bucket capacity >=80% and <=100%). Bucket filling is to be stopped once equal or more than 80% of bucket capacity is filled. The amount of water taken at a time in a mug is not fixed as it can be any value less than or equal to y. Notify the user, to stop once the bucket is full, that is equal to or more than 80% of the capacity of the bucket and the count of, mugs of water poured into the bucket.
Note that bucket's capacity will always be greater than mug’s capacity and there is enough water available to fill the bucket.

Input Format

Input the capacity of bucket in litres.
Input the capacity of mug in litres.
Input the amount of water in mug one after other.
If the amount of water entered by the user is less than zero or greater than mug’s capacity display “INVALID INPUT” and quit.
If the capacity of mug entered is greater than the capacity of bucket then quit with the error message “INVALID INPUT”.

Constraints

x > y

Output Format

When the bucket is full the output should be in the following format:
BUCKET FULL!
NUMBER OF MUGS: x

Sample Input 0

100
20
20
20
20
20
20

Sample Output 0

BUCKET FULL!
NUMBER OF MUGS: 4

'''
filled=0; mug_count=0; flag=0
buck_cap,mug_cap = int(input()), int(input())
min_bcap = buck_cap*0.8
if(buck_cap<=mug_cap):
    flag=1
else:
    while(filled<min_bcap):
        tmp=int(input())
        if(tmp>mug_cap or tmp<0):
            flag=1
            break
        else:
            filled+=tmp
            mug_count+=1
if(flag==0):
    print("BUCKET FULL!\nNUMBER OF MUGS:", mug_count)
else:
    print("INVALID INPUT")