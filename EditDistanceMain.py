"""
Created on Sun Nov 26 03:46:04 2017

@author: Vinoth
Group 1 Batch 7
"""
#Main file to execute all the code
#importing libraries
import time
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from random import choice
from string import ascii_uppercase

#importing algorithm files
import PurelyRecursive
import BranchandBound
import GreedyApproximation
import DivideandConquer
import dynamicprograms
import Kstripsdynamicprogram


randomStringlength = 8
# Initialisation of strings

firstString  = "GTACASDFSWS"
secondString = "GGDCFATDMWS"



# Generate random sequence
#firstString = ''.join(choice(ascii_uppercase) for i in range(randomStringlength))
#secondString = ''.join(choice(ascii_uppercase) for i in range(randomStringlength))


#Calling recursive function
print("{:<20}".format("First String  :"),firstString)
print("{:<20}".format("Second String :"),secondString)

print("\nXXXXXXXXXXXXXXXXXXXXXXXXX")
print("--------- Purely recursive ---------")
time_start = time.clock()
print("{:<20}".format("Edit distance :"),PurelyRecursive.RecursiveEditDistance(firstString,secondString))
time_recursive =round((time.clock() - time_start),5)
print("{:<20}".format("Running time  :"),time_recursive , "seconds") 
#print("{:<20}".format("Sequence Alignment :"),PurelyRecursive.RecursiveSequenceAlignment(firstString,secondString))
print("XXXXXXXXXXXXXXXXXXXXXXXXX")
   
print("XXXXXXXXXXXXXXXXXXXXXXXXX")
print("--------- Branch and Bound ---------")
time_start = time.clock()
result, a1, a2 =BranchandBound.bbound(firstString,secondString,0,max(len(firstString),len(secondString)))
print("{:<20}".format("Edit distance :"),result)
time_branch = round((time.clock() - time_start),5)
print("{:<20}".format("Running time  :"),time_branch, "seconds") 
print("{:<20}".format("Sequence Alignment :"),a1,"\n",a2)
print("XXXXXXXXXXXXXXXXXXXXXXXXX")

print("XXXXXXXXXXXXXXXXXXXXXXXXX")
print("--------- Greedy Approximation ---------")
time_start = time.clock()
(align1,align2),ed = GreedyApproximation.greedyEditdistance(firstString,secondString)
print("{:<20}".format("Edit distance :"),ed)
time_greedy = round((time.clock() - time_start),5)
print("{:<20}".format("Running time  :"),time_greedy, "seconds") 
print("{:<20}".format("Sequence Alignment :"),(align1,align2))
print("XXXXXXXXXXXXXXXXXXXXXXXXX")


print("XXXXXXXXXXXXXXXXXXXXXXXXX")
print("--------- Divide and Conquer ---------")
time_start = time.clock()
(Z,W),ed = DivideandConquer.Hirschberg(firstString,secondString)
print("{:<20}".format("Edit distance :"),ed)
time_divide = round((time.clock() - time_start),5)
print("{:<20}".format("Running time  :"),time_divide, "seconds") 
print("{:<20}".format("Sequence Alignment :"),(Z,W))
print("XXXXXXXXXXXXXXXXXXXXXXXXX")

print("XXXXXXXXXXXXXXXXXXXXXXXXX")
print("--------- Dynamic Programming ---------")
time_start = time.clock()
ed = dynamicprograms.editDistDp(firstString,secondString,)
print("{:<20}".format("Edit distance :"),ed)
time_dynamic = round((time.clock() - time_start),5)
print("{:<20}".format("Running time  :"), time_dynamic, "seconds") 
print("XXXXXXXXXXXXXXXXXXXXXXXXX")

print("XXXXXXXXXXXXXXXXXXXXXXXXX")
print("--------- K Strips ---------")
time_start = time.clock()
ed = Kstripsdynamicprogram.runtime(Kstripsdynamicprogram.kstrip,firstString,secondString,2)
print("{:<20}".format("Edit distance :"),ed[1][0])
time_kstrips = round((time.clock() - time_start),5)
print("{:<20}".format("Running time  :"),time_kstrips, "seconds")
print("{:<20}".format("Sequence Alignment :"))
print(ed[1][2])
print(ed[1][3])
print(ed[1][4])
print("XXXXXXXXXXXXXXXXXXXXXXXXX")

'''
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (12, 12),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)'''
plt.figure(' Algorithms Time')
plt.plot([time_recursive, time_branch, time_greedy, time_divide, time_dynamic, time_kstrips])
plt.text(0,time_recursive, "Recursive")
plt.text(1,time_branch, "Brand and Bound")
plt.text(2,time_greedy, "Greedy")
plt.text(3,time_divide, "Divide")
plt.text(4,time_dynamic, "Dynamic")
plt.text(5,time_kstrips, "K Strips")
plt.ylabel('Time (seconds)')
plt.xlabel('Algorithms')
plt.show()
