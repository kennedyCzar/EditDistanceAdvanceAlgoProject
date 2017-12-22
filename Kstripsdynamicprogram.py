'''
function use and keywords:
    1. def init(s1,s2):
         s1-->first string
         s2-->next string

    2. def kstrip(s1, s2, k=1)
            k-->factor for computing edit distance
'''

import numpy as np
import random
import string
import time
import math
import copy
import sys


firstSequence  = ' '
secondSequence = ' '
intermediateSequence = ' '
# initialized computation
def init(s1, s2):
    m = np.empty((len(s1) + 1, len(s2) + 1))
    m[:] = np.inf
    # initializing the first row
    m[0] = np.arange(m.shape[1])
    # initializing the first column
    counter = 0
    for i in m:
        i[0] = counter
        counter += 1
    return m


#K-STRIP ALGORITHM
def kstrip(s1, s2, k=1):

    # K value exception
    if k > min((len(s1)), (len(s2))) or k < 1:
        raise Exception('K VALUE OUT OF BOUNDS')

    # INITIALIZATION
    m = init(s1, s2)

    # Offset counter
    offset = - (k-2)
    # Limit counter
    cap = k + 1 + abs(len(s1) - len(s2))
    # Loop for K-strips around the main diagonal
    for i in range(1, m.shape[0]):
        for j in range(max(1, offset), cap):
            # first condition : i is an insertion
            con1 = m[i - 1, j] + 1

            # second condition : j is a deletion
            con2 = m[i, j - 1] + 1

            # third condition : i and j are a substitution
            if s1[i - 1] == s2[j - 1]:
                # if same letters, we add nothing
                con3 = m[i - 1, j - 1]
            else:
                # if different letters, we add one
                con3 = m[i - 1, j - 1] + 1

            # assign minimum value
            m[i][j] = min(con1, con2, con3)
            # print("con1: {} con2: {} con3: {} min: {}".format(con1, con2, con3, m[i][i]))
            # Saving Result
        offset += 1
        if cap < m.shape[1]:
            cap += 1
    
    # Alignment for kstrip
    zero = 0
    mm = np.c_[[zero] * len(m[:]), m]
    p = np.r_[[[zero] * len(mm[1, :])], mm]

    backtrack = [[' ' for y in range(len(s2) + 2)] for x in range(len(s1) + 2)]
    backtrack[1][1] = 0

    for i in range(2, len(s1) + 2):
        backtrack[i][0] = s1[i - 2]
    for j in range(2, len(s2) + 2):
        backtrack[0][j] = s2[j - 2]

    for i in range(2, len(s1) + 2):
        backtrack[i][1] = '|'

    for j in range(2, len(s2) + 2):
        backtrack[1][j] = '_'

    for i in range(2, len(s1) + 2):
        for j in range(2, len(s2) + 2):
            #deletion on the vertical
            vertical = p[i - 1][j] + 1

            #inserion on the horizontal 
            horizontal = p[i][j - 1] + 1 
            if s1[i - 2] == s2[j - 2]:
                diagonal = p[i - 1][j - 1]
            else:
                #suubstitution along the dialgonal
                diagonal = p[i - 1][j - 1] + 1  

            mdistance = min(diagonal, vertical, horizontal)
            p[i][j] = mdistance

            if mdistance == diagonal:
                backtrack[i][j] = 'bn'
            elif mdistance == vertical:
                backtrack[i][j] = '|'
            else:
                backtrack[i][j] = '_'
    w = ""
    s = ""
    t = ""

    i = len(s1) + 1
    j = len(s2) + 1
    while not (i == 1 and j == 1):
        c = backtrack[i][j]
        if c == '|':
            w += s1[i - 2] + ' '
            s += '_' + ' '
            t += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            w += s1[i - 2] + ' '
            s += s2[j - 2] + ' '
            if s1[i - 2] == s2[j - 2]:
                t += '|' + ' '
            else:
                t += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            w += '_' + ' '
            s += s2[j - 2] + ' '
            t += ' ' + ' '
            j = j - 1


    #print(w[::-1])
    #print(t[::-1])
    #print(s[::-1])
    
    
    # prints the result of the strip 
    return m[m.shape[0] - 1][m.shape[1] - 1], m,w[::-1],t[::-1],s[::-1]
         
# compute the running time of the algo
def runtime(function, *args):
    start_time = time.time()
    result = function(*args)
    return time.time() - start_time, result


# function to randonmy print the required strings
def chargen(size=50, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
    
if __name__ == "__main__":
    s1 = chargen(6)
    s2 = chargen(6)
    print('First protein string #1 : ' + s1)
    print('Second protein string #2 : ' + s2)
    print("=================================")
    print("K-STRIP ALGORITHM")
    print("=================================")
    result = runtime(kstrip, s1, s2, k)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1][0])))
    print(result[1][1])
    print("RUNNING TIME :  %s seconds" % result[0])
    print("K :  %s" % k)
    # Printing Matrix not so important though
    print("")
    '''print(result[1][1])'''
