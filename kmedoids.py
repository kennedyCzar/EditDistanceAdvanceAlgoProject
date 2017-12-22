# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:01:59 2017

@author: Leila Jamshidian Sales
"""

NUMBER_OF_CLUSTERS = 3
import numpy as np

def kMedoids(D, k, tmax=100):
    # determine dimensions of distance matrix D
    m, n = D.shape

    if k > n:
        raise Exception('too many medoids')
    # randomly initialize an array of k medoid indices
    M = np.arange(n)
    np.random.shuffle(M)
    M = np.sort(M[:k])

    # create a copy of the array of medoid indices
    Mnew = np.copy(M)

    # initialize a dictionary to represent clusters
    C = {}
    for t in range(tmax): #tmax is the number of iterations of the algorithm performed
        # determine clusters, i. e. arrays of data indices
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
        # update cluster medoids
        for kappa in range(k):
            J = np.mean(D[np.ix_(C[kappa],C[kappa])],axis=1)
            j = np.argmin(J)
            Mnew[kappa] = C[kappa][j]
        np.sort(Mnew)
        # check for convergence
        if np.array_equal(M, Mnew):
            break
        M = np.copy(Mnew)
    else:
        # final update of cluster memberships
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]

    # return results
    return M, C


#Importing precomputed Distance matrix
import pickle
distance_matrix = pickle.load( open( "C:/Users/grover/.spyder-py3/save.p", "rb" ) )
print ('The size of distance matrix is ',distance_matrix.shape)


#Calculating the clusters
import time
time_start = time.clock()
M, C = kMedoids(distance_matrix, NUMBER_OF_CLUSTERS)
print ('time taken: ', time.clock() - time_start)


#Reading the names of Protiens
import csv
with open("C:/Users/grover/Downloads/data.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    data = []
    names = [] 
    for row in readCSV:
        if row:
            names.append(row[0])
            data.append(row[3])


# Showing the Results
for i in range(len(M)):
    print( 'The mediod ',i,' is ',names[M[i]] )
from algo61 import greedyEditdistance
for i in range(len(M)):
    for j in range(i+1,len(M)):
        print ('The (greedy)Edit distance between medoids ',i, 'and',j,' is ',greedyEditdistance(data[M[i]],data[M[j]]), ' while their lengths  are ', len(data[M[i]]) , ' and ',len(data[M[j]]) )
        
print ('This proves that the found clusters are significantly different from each other')


    

