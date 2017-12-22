"""
Created on Sun Nov 26 03:46:04 2017

@author: Vinoth
Group 1 Batch 7
"""

import numpy as np
from numpy import array
 
def editDistDp(str1, str2):
    m=len(str1)
    n=len(str2)
    # Create a table to store results of subproblems: divide and conquer approach
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    scoring = [[1 for x in range(n+1)] for x in range(m+1)]
   # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
           # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j	# The minimum operations = j
             # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i	# Min. operations = i
             # If last characters are same, ignore last character
            # and recur for remaining string, that is; performing a recursion
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
             # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1+min(dp[i][j-1],    	# Insert
                                   dp[i-1][j],    	# Remove
                                   dp[i-1][j-1])	# Replace

    print("XXXXXXX Dynamic Program XXXXXXX")
    for i in range(m+1):
        for j in range(n+1):
            print(dp[i][j],end='  ')
        print(' ')
    
    # Initialisation of Alignment
    conf1 = np.empty((len(str1) + 1, len(str2) + 1))
    conf1[:] = np.inf
    # initializing the first row
    conf1[0] = np.arange(conf1.shape[1])
    # initializing the first column
    counter = 0
    for i in conf1:
        i[0]    = counter
        counter = 1 + counter
    
    conf2 = np.c_[[0]*len(conf1[:]),conf1]
    conf3 = np.r_[[[0]*len(conf2[1,:])],conf2]
    backmatrix = [[' ' for y in range(len(str2) + 2)] for x in range(len(str1) + 2)]
    backmatrix[1][1] = 0

    for i in range(2, len(str1) + 2):
        backmatrix[i][0] = str1[i - 2]
    for j in range(2, len(str2) + 2):
        backmatrix[0][j] = str2[j - 2]

    for i in range(2, len(str1) + 2):
        backmatrix[i][1] = '|'

    for j in range(2, len(str2) + 2):
        backmatrix[1][j] = '-'

    for i in range(2, len(str1) + 2):
        for j in range(2, len(str2) + 2):
            vertical = conf3[i - 1][j] + 1
            horizontal = conf3[i][j - 1] + 1
            if str1[i - 2] == str2[j - 2]:
                diagonal = conf3[i - 1][j - 1]
            else:
                diagonal = conf3[i - 1][j - 1] + 1

            minimumDist = min(diagonal, vertical, horizontal)
            conf3[i][j] = minimumDist

            if minimumDist == diagonal:
                backmatrix[i][j] = 'bn'
            elif minimumDist == vertical:
                backmatrix[i][j] = '|'
            else:
                backmatrix[i][j] = '-'

    firstSequence = ""
    secondSequence = ""
    op = ""

    i = len(str1) + 1
    j = len(str2) + 1
    while not (i == 1 and j == 1):
        c = backmatrix[i][j]
        if c == '|':
            firstSequence += str1[i - 2] + ' '
            secondSequence += '-' + ' '
            op += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            firstSequence += str1[i - 2] + ' '
            secondSequence += str2[j - 2] + ' '
            if str1[i - 2] == str2[j - 2]:
                op += '|' + ' '
            else:
                op += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            firstSequence += '-' + ' '
            secondSequence += str2[j - 2] + ' '
            op += ' ' + ' '
            j = j - 1

    firstSequence = firstSequence[::-1]
    secondSequence = secondSequence[::-1]   
    return (dp[len(str1)][len(str2)],firstSequence,secondSequence)
    
#the main function is used here plus updates to manually input the strings at run time
if __name__ == "__main__":
    str1="INTENTION"
    str2="EXECUTION"
    print('Edit Distance',editDistDp(str1, str2))
   
   
