#!/usr/bin/env python

#Calculate the frequencies of different Nucletodies in a DNA Sequence

dnaSeq = input("Enter your DNA sequence here:")

#Prompt user to enter their DNA sequence

#calculate the entire length of the DNA sequence.
print ("Total Sequence Length")
print (len(dnaSeq)) 

#count the number of A's
print ("Number of A's in the DNA sequence:")
print (dnaSeq.count('a'))

#count the number of C's
print ("Number of C's in the DNA sequence:")
print (dnaSeq.count('c'))

#count the number of T's
print ("Number of T's in the DNA sequence:")
print (dnaSeq.count('t'))

#count the number of G's
print ("Number of G's in the DNA sequence:")
print (dnaSeq.count('g'))
