"""
Created on Sun Nov 26 03:46:04 2017

@author: Vinoth
Group 1 Batch 7
"""

# Implementation of the recursive editdistance function
matchscore   = 2
mismatchscore = 1   

def RecursiveEditDistance(a, b):
    """Recursively calculate the edit distance between two strings, a and b.
    Returns the edit distance."""
    if(not a):
        return len(b)   # returns length of b if a is an empty string
    if(not b):
        return len(a)   # returns length of a if b is an empty string

    # Checking the last character equals on both the strings.
    if(a[-1]== b[-1]):
        costFunction = 0
    else:
        costFunction = 1

    #returning the minimum Edit distance call 
    return min(RecursiveEditDistance(a[:-1],b[:-1])+ costFunction,
               # Calling function without last characters in both the string
               (RecursiveEditDistance(a[:-1], b)+1),
               # Calling function after removing a last character in first string
               (RecursiveEditDistance(a, b[:-1])+1))
               # Calling function after removing a last character in second string


Insertionoperator='-'
def RecursiveSequenceAlignment (firstString, secondString):
    
    if len(firstString) == 0 or len(secondString) == 0:
        while len(firstString) < len(secondString):
            firstString = firstString + Insertionoperator
        while len(secondString) < len(firstString):
            secondString = secondString + Insertionoperator
        return firstString, secondString
    else:
        # Alignment without gap
        (firstString0, secondString0) = RecursiveSequenceAlignment (firstString[1:], secondString[1:])
        scoreWithoutGap = scoreFunction (firstString0, secondString0,matchscore,mismatchscore)
        if firstString[0] == secondString[0]: scoreWithoutGap += matchscore
        
        # Gap at firstString without the first character of secondString
        (firstString1, secondString1) = RecursiveSequenceAlignment (firstString, secondString[1:])
        scoreGapfirstString = scoreFunction (firstString1, secondString1,matchscore,mismatchscore) - mismatchscore
        
        # Gap at secondString without the firs character of firstString 
        (firstString2, secondString2) = RecursiveSequenceAlignment (firstString[1:], secondString)
        scoreGapsecondString = scoreFunction (firstString2, secondString2,matchscore,mismatchscore) - mismatchscore
        
        if scoreWithoutGap >= scoreGapfirstString and scoreWithoutGap >= scoreGapsecondString:
            return firstString[0] + firstString0, secondString[0] + secondString0
        elif scoreGapfirstString >= scoreGapsecondString:
            return Insertionoperator + firstString1, secondString[0] + secondString1
        else:
            return firstString[0] + firstString2, Insertionoperator + secondString2
    
def scoreFunction(firstString,secondString,matchscore,mismatchscore):
    score =0
    for i in range(len(firstString)):
        if(firstString[i] == secondString[i]):
            score += matchscore
        else:
            score -= mismatchscore
    return score
