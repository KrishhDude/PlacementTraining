'''
An international round table conference will be held in india. Presidents from all over the world representing their respective countries will be attending the conference. The task is to find the possible number of ways(P) to make the N members sit around the circular table such that the president and prime minister of India will always sit next to each other.

Constraints:
2<=N<=50
Example 1 :

Input :
4 → Value of N(No. of members)

Output :
4 → Possible ways of seating the members

Explanation:
2 members should always be next to each other.
So, 2 members can be in 2! ways.
Rest of the members can be arranged in (4-2)! ways.(2 is subtracted because the previously selected two members will be considered as single members now).
So total possible ways 4 members can be seated around the circular table (4-2)! x 2! = 4.
Hence, output is 4.
Example 2 :

Input :
10 → Value of N(No. of members)

Output :
80640 → Possible ways of seating the members

Explanation:
2 members should always be next to each other.
So, 2 members can be in 2! ways.
Rest of the members can be arranged in (10-2)! Ways. (2 is subtracted because the previously selected two members will be considered as a single member now).
So, total possible ways 10 members can be seated around a round table is (10-2)! x 2! = 80640 ways.
Hence, output is 80640.

Input Format

The candidate has to write the code to accept one input.
First input - Accept value of number of N(Positive integer number)

Constraints

2<=N<=50

Output Format

The output should be a positive integer number or print the message(if any) given in the problem statement(Check the output in Example 1 and Example 2).

Sample Input 0

4

Sample Output 0

4

Sample Input 1

10

Sample Output 1

80640
'''