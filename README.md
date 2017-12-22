# Minimum Edit Distance Advance Algo Project UJM
Minimum Edit Distance (Advance Algorithm Project)- Implementing Dynamic, Greedy, Branch and Bound, K-strip Algo
-------------------------------------------------------------------------------------------------------------------------
1. Team Members : 
• Vinothkumar Ganeshan*.
• Ezukwoke kenneth*.
• Leila Jamshidian sales*.
• Milica Madzarevic*.

2. TO-DO List :
• Alignment.
• K strip calculation order.
• Divide and Connquer.
• Greedy Algorithm.
• Pure Recursive approach.
• Branch and Bound Using Heuristic.
• Experimental Protocol (Analyze Protin Samples on Cloud Servers).
• GUI (Project Data).
• Report.

---------------------------------------------------------------------------------------------------------
3. Description : 
The objective of this project is to implement some algorithms for computing the Edit distance (ED) (an adaptation of the LCS problem) and to provide an experimental study of their running time and the quality of the solution given.

4 Work to do : 
You must program different algorithms for the ED problem, including:

• The classic algorithm based on dynamic programming. The algorithm is similar to the LCS problem, your first job will be to look for informations about this algorithm.

• The version combining dynamic programming and divide and conquer approaches allowing one to solve the problem with a linear space complexity (similar version as the one seen for LCS).

• The pure recursive version (having an exponential time complexity).

• A branch-and-bound version of the recursive approach (see lecture slides).

• An approximated version of the classical dynamic programming approach where one fills only a stripe of size k around the diagonal of the matrix. (different band values must be evaluated).

• An approximated version based on a greedy approach (to be defined, cf lecture notes).

Note that all the algorithms must be able to output the distance of a solution and a possible alignment corresponding to an (approximated) ED.

A graphical user interface could be proposed to illustrate the behavior of the algorithm(s), but this is not required and must be done after the implementation of ED algorithms.

The running time of the algorithms and the quality of the solutions given (in terms of optimality) have to be evaluated on problems of different sizes (ie the length of the input strings). A random generator of problems could be used for example. You have to provide a full and rigorous experimental study to illustrate the different strong and weak points of each algorithm.

The algorithms must be also evaluated on a protein database available here: http://forge.info.univ-angers.fr/~gh/Shspdb/index.php?action=0&mode=0, (experimental set up to be defined).

