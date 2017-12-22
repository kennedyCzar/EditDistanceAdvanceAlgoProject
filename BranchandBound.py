'''
*************************************************************
Branch and Branch algo for Edit Distance
**********by Ezukwoke Ifeanyi kenneth Group1 Batch7 Member*******
the arguments of the bbound are
    -->1. s1= first protein string
    -->2. s2= second protein string
    -->3. cost= initial cost at root node set to zero
    -->4. Bound= the bound/limitation parameter for edit distance computation
'''
import string
from time import time

def bbound(s1, s2, cost=0, bound=0):
    n = len(s1) #length of the first protein string
    m = len(s2) #length of the second protein string

    #check to see if the no string is entered:and return empty array if yes
    if n == 0 and m == 0:
        return 0, [], []

    #if the length of string 1 is 0 i.e no string to compare; return the content of string 2
    if n == 0:
        return m, ["_" for i in range(m)], [s2[i] for i in range(m)]

    #if the length of string 2 is 0 i.e no string to compare; return the content of string 1
    if m == 0:
        return n, [s1[i] for i in range(n)], ["_" for i in range(n)]

    #we check the cost of the last character of the first string and the next strin
    weightx = abs((n - 1) - m)
    weighty = weightx + cost
    #we check the cost of the last character of the second string and the next strin
    weightp = abs(n - (m - 1))
    weightq = weightp + cost

    #we check the cost of the last two characters of the both strings
    weightw = abs((n - 1) - (m - 1))
    if s1[-1] == s2[-1]:
        weightm = weightw + cost - 1
    else:
        weightm = weightw + cost
    ad1, ad2, ai1, ai2, ac1, ac2 = [], [], [], [], [], []

    #if the bound is greater than weighty we perform deletion
    if bound >= weighty:
        # Deletion branch for the algo
        deletion,ad1,ad2  = bbound(s1[:-1], s2, cost + 1, bound)  # Deletion
        deletion += 1
    else:
        deletion = 1000000

    #if the bound is greater or equal to the 
    if bound >= weightq:
        #Insertion branch for algo
        insertion,ai1,ai2 = bbound(s1, s2[:-1], cost + 1, bound)  # Insertion
        insertion += 1
    else:
        insertion = 1000000
    if bound >= weightw:
        #3 branch compare the last two protein strings
        if (s1[-1] != s2[-1]):
            substitution,ac1,ac2 = bbound(s1[:-1], s2[:-1], cost + 1, bound)
            substitution += 1
        else:
            substitution,ac1,ac2 = bbound(s1[:-1], s2[:-1], cost, bound)
    else:
        substitution = 1000000

    #store the value of the operations: deletion, insertion and substitution in an array
    values = [deletion, insertion, substitution]
    minval = min(deletion, insertion, substitution)
    if values.index(minval) == 0:
        ad1 = ad1 + [s1[-1]]
        ad2 = ad2 + ["_"]
        return minval, ad1, ad2
    elif values.index(minval) == 1:
        ai1 = ai1 + ["_"]
        ai2 = ai2 +[s2[-1]]
        return minval, ai1, ai2
    else:
        ac1 = ac1 + [s1[-1]]
        ac2 = ac2 + [s2[-1]]
        return minval, ac1, ac2

#the needed steps taken to compute the Edit distance is described here
def operations(al1, al2):
    print('************************************************************')
    print("The operation performed during branch and bound: \n")
    n = len(al1)
    for i in range(n):
        if al1[i] == "_":
            print("Deletion at index " + str(i))
        elif al2[i]== "_":
            print("Insertion " + al1[i] + " at index " + str(i))
        elif al1[i] != al2[i]:
            print("Substitution " + al1[i] + " for " + al2[i] + " at index " + str(i))


if __name__ == "__main__":
    print('=============================================================================')
    print("Branch and bound for edit distance")
    print('==========================================================================')
    s1 =input("Enter your first protein string: ")
    s2 =input("Enter your next protein string: ")
    start_time=time()
    result, a1, a2  = bbound(s1,s2,0,max(len(s1),len(s2)))
    print('\n*******ALIGNMENT*********')
    print(a1,'\n',a2)
    print('\nThe edit distance is: ',result)
    end_time=time()
    print('The time taken to compute the edit distance is : %3f seconds'%(end_time-start_time))
    print(operations(al1=s1,al2=s2))
    print('*****************')
    print('END OF PROGRAM')
    print('*****************')