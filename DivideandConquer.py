# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:46:04 2017

@author: leila jamshidian sales
"""
from operator import add
def argmin(iterable):
    return max(enumerate(iterable), key=lambda x: -x[1])[0]


def editDistDP(str1, str2):
    "Returns the last row of edit distance matrix"
   # Solve the problem row-by-row. O(m+n)
    m = len(str1)
    n = len(str2)
    columnx = [x for x in range(m+1)]
    rowy = [y for y in range(n+1)]

    # Solving row-by-row and intializing first element of each row from the first column
    for i in range(1,m+1):
        new_rowy = []
        new_rowy.append(columnx[i])
        for j in range(1,n+1):

            # If last characters are same, no cost is incurred
            if str1[i-1] == str2[j-1]:

                new_rowy.append(rowy[j-1])

           # If last character are different, consider all

           # possibilities and find minimum

            else:

                new_rowy.append( 1 + min(new_rowy[-1],        # Insert

                                   rowy[j],        # Remove

                                   rowy[j-1])     )    # Replace
       #print (rowy)
        rowy = new_rowy
    return rowy

def NeedlemanWunsch(X,Y):
    "Just works when atleast len(X) ==1 or len(Y) == 1"
    editdistance = 0
    if len(X) == len(Y):
        if X!=Y:
            editdistance+=1
        return (X,Y),editdistance
    else:
        
        #This functions assumes len(X) < len(Y) always, hence flipping if required
        flip = False
        if len(X) > len(Y):
            temp = X
            X = Y
            Y = temp
            flip = True
        str1 = ""
        
        #Shifting single-charecter string X, until it matches one charecter in Y
        for charecter in Y:
            if charecter != X:
                str1 += '-'
                editdistance+=1
            else:
                str1 += X
                
        #Returning the alignment
        if flip:
            return (Y,str1),editdistance
        else:
            return (str1,Y),editdistance
                
        
def Hirschberg(X,Y):
    Z = ""
    W = ""
    
    #Trivial Cases
    if len(X) == 0:
        for i in range(len(Y)):
            Z = Z + '-'
            W = W + Y[i]
        editdistance = len(Y)
    elif len(Y) == 0:
        for i in range(len(X)):
            Z = Z + X[i]
            W = W + '-'
        editdistance = len(X)
    elif len(X) == 1 or len(Y) == 1:
        (Z,W),editdistance = NeedlemanWunsch(X,Y)
        
    #Divide the problem into optimal subproblems
    else:
        xlen = len(X)
        xmid = int(len(X)/2)
        ylen = len(Y)

        #Finding optimal partition for Y, corresponding to partition [X[0],X[xmid],X[-1]] 
        ScoreL = editDistDP(X[0:xmid], Y)
        ScoreR = editDistDP(X[xmid:][::-1], Y[::-1])
        ymid = argmin(  map(add, ScoreL, ScoreR[::-1])  )
 
        #Recursively calling on the two generated subproblems
        (z1,w1),ed1 = Hirschberg(X[0:xmid], Y[0:ymid])
        (z2,w2),ed2 = Hirschberg(X[xmid:], Y[ymid:])
        (Z,W) = z1 + z2, w1 + w2
        editdistance = ed1+ed2

    return (Z,W),editdistance

'''
X = 'AGTACGCA'
Y = 'TATGC'
(Z,W),ed = Hirschberg(X,Y)
print (Z,W)
print (ed)
'''
