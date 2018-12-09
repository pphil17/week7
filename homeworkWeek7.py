#!/usr/bin/env python

#Calculate the frequencies of different Nucletodies in a DNA Sequence

dnaSeq = input("Enter your DNA sequence here:")

#Prompt user to enter their DNA sequence

#calculate the entire length of the DNA sequence.
print ("Total Sequence Length")
print (len(dnaSeq)) 

#count the number of A's
print ("Number of A's in the DNA sequence:")
print (dnaSeq.lower().count('a'))

#count the number of C's
print ("Number of C's in the DNA sequence:")
print (dnaSeq.lower().count('c'))

#count the number of T's
print ("Number of T's in the DNA sequence:")
print (dnaSeq.lower().count('t'))

#count the number of G's
print ("Number of G's in the DNA sequence:")
print (dnaSeq.lower().count('g'))

# DB: Good! My only suggestion is to make it more general by allowing both upper- and 
#     lowercase sequences. You can do this by adding .lower() to dnaSeq (see above).