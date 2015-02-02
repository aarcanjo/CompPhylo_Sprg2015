# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:36:45 2015

@author: arcanjo

An Introduction to Likelihood
"""
from __future__ import division
from scipy.stats import binom
import matplotlib.pyplot as plot

"""
For the in-class version of this exercise, I'm going to perform a manual draw from a 
binomial using colored marbles in a cup. We'll arbitrarily define dark marbles as successes 
and light marbles as failures.
Record the outcomes here:
Draw 1: dark
Draw 2: dark
Draw 3: dark
Draw 4: dark
Draw 5: light
Number of 'successes': 4
Now record the observed number of succeses as in the data variable below.
"""
data = 4# Supply observed number of successes here.
numTrials = 5
from discSamp import * # I've stored my function in the file discSamp.py


"""
Now we need to calculate likelihoods for a series of different values for p to compare 
likelihoods. There are an infinite number of possible values for p, so let's confine 
ourselves to steps of 0.05 between 0 and 1.
"""

probs = []# Set up a list with all relevant values of p
for i in range(0,105,5): #range is set to include the probability =1
    probs.append(i/100)
print probs

'''Calculate the likelihood scores for these values of p, in light of the data you've collected'''
lh_probs = [] #creates the list to store all the binomial PMFs
for prob in probs:
    lh_probs.append(binPMF(data, numTrials, prob))
print lh_probs

''' Find the maximum likelihood value of p (at least, the max in this set)'''
maxLikelihood = max(lh_probs) #finds the maximum value in the likelihood list
index = lh_probs.index(max(lh_probs)) #finds the index of the maximum likelihood
maxLHProb = probs[index] #gets the probability associated to the maximum likelihood value
print "The maximum likelihood value is:", maxLikelihood, "for the p value of:", maxLHProb

'''What is the strength of evidence against the most extreme values of p (0 and 1)?'''

#both values (0 and 1) have a PMF = 0, wich means that it probabilities of 0 (no dark balls drawn) and 1 (no light
balls drawn) are improbable, since we have drawn at least one of each color already

'''Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)'''

lh_ratios = [] #creates a list to store the likelihood ratios for each probability 
for lh in lh_probs:
    lh_ratios.append(lh/maxLikelihood)
print lh_ratios

plot.plot(probs, lh_ratios) #plots the ratios into a graph
plot.xlabel('p values')
plot.ylabel('Likelihood ratio')
plot.show()

#this shows a curve skewed to the right, with highest peak at p=0.8
"""
Now let's try this all again, but with more data. This time, we'll use 20 draws from our cup 
of marbles.
"""
data2 = 12# Supply observed number of successes here.
numTrials2 = 20

''' Calculate the likelihood scores for these values of p, in light of the data you've collected'''
lh_probs = [] #from here on, everything is pretty much the same as before.
for prob in probs:
    lh_probs.append(binPMF(data2, numTrials2, prob))
print lh_probs

# Find the maximum likelihood value of p (at least, the max in this set)
maxLikelihood = max(lh_probs)
index = lh_probs.index(max(lh_probs)) 
maxLHProb = probs[index]
print "The maximum likelihood value is:", maxLikelihood, "for the p value of:", maxLHProb

# What is the strength of evidence against the most extreme values of p (0 and 1)?
# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)
lh_ratios = []
for lh in lh_probs:
    lh_ratios.append(lh/maxLikelihood)
print lh_ratios

plot.plot(probs, lh_ratios)
plot.xlabel('p values')
plot.ylabel('Likelihood ratio')
plot.show()

'''When is the ratio small enough to reject some values of p?'''
# For 0<p<0.3 and p>0.8
# it is interesting to notice that now the peak is on p=0.6, and that the maximum likelihood for this probability is
# L=0.179, while in the previous drawn the peak was on p=0.8 with L=0.409, in accordance with the fact that the
#smaller the number of datasets, the bigger the likelihood.
