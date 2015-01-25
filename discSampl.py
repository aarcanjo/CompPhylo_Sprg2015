# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 13:56:58 2015

@author: Ana Carolina Arcanjo e-mail: a.arcanjo@gmail.com
Code referent to the exercise 2 for Computational Phylogenetics. 
This exercise is due on Tuesday, Jan 27th.

*** Discrete Sampling Practice ***

---> Creating useful functions <---


"""
import time #imports the time module to start timing the execution of functions

'''(1) Write a function that multiplies all consecutively decreasing numbers between a maximum and a minimum 
supplied as arguments. (Like a factorial, but not necessarily going all the way to 1). This calculation 
would look like = max * max-1 * max-2 * ... * min'''

def consecutiveMultiplier(intMax, intMin):
    '''This function takes two integers as arguments (intMax and intMin) and multiplies the consecutive 
    numbers from intMax to intMin (like a factorial, but not necessarily reaching 1).'''
    result = 1 #creates the variable that will store the result of the multiplication
    for i in range(intMax-intMin+1): #establishes the range of numbers to create the consecutive numbers
       result = result * (intMax - i) #multiplies the result by the next consecutive number
    return result #returns the result
print(consecutiveMultiplier(10,5))


'''(2) Using the function you wrote in (1), write a function that calculates the binomial coefficient 
(see Definition 1.4.12 in the probability reading). Actually, do this twice. The first time (2a) calculate 
all factorials fully. Now re-write the function and cancel as many terms as possible so you can avoid
unnecessary multiplication (see the middle expression in Theorem 1.4.13).'''

#2a
def binCoeff(n,k):
    '''This function calculates the binomial coefficient for two integers n and k.'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient using the factorial formula for each element
        coeff = consecutiveMultiplier(n, 1) / (consecutiveMultiplier(n-k, 1)*consecutiveMultiplier(k, 1))
        return coeff


#2b
def binCoeff2(n,k):
    '''This function calculates the binomial coefficient for two integers n and k in a more concise way.'''
    if k > n: #establishes the value of the binomial coefficient if k > n
        return 0
    else: #calculates the binomial coefficient by cancelling out the common terms in both parts of the division
        coeff = consecutiveMultiplier(n, n-k+1)/consecutiveMultiplier(k,1)
        return coeff

'''(3) Try calculating different binomial coefficients using both the functions from (2a) and (2b) for 
different values of n and k. Try some really big values there is a noticeable difference in speed between 
the (2a) and (2b) function. Which one is faster? By roughly how much?'''

ini1 = time.time() #calls the function time to mark the beginning of the run   
print(binCoeff(100000,5000)) #executes the function binCoeff()
fin1 = time.time() #calls the function time to mark the end of the run
print "binCoeff() function took", fin1-ini1, "seconds to process." # 7.609444 seconds to run

ini2 = time.time() #calls the function time to mark the beginning of the run
print(binCoeff2(100000,5000)) #executes the function binCoeff2()
fin2 = time.time() #calls the function time to mark the end of the run
print "binCoeff2() function took", fin2-ini2, "seconds to process." # 0.02311 seconds to run


'''(4) Use either function (2a) or (2b) to write a function that calculates the probability of k successes 
in n Bernoulli trials with probability p. This is called the Binomial(n,p) distribution. See Theorem 3.3.5 
for the necessary equation. [Hint: pow(x,y) returns x^y (x raised to the power of y)].'''

def binProb(k,n,p):
    '''This function calculates the probability of k successes in n Bernoulli trials with probability p.
    Both k and n are positive integers and 0<p<1. All k, n and p are provided by the user.'''
    prob = 0.0 #creates the variable prob
    if k < 0 or k > n: #specifies the value of prob in case k is not a positive integer < n
        return 0
    else: #calculates the binomial probability mass function for the values given
        prob = binCoeff2(n, k) * (pow(p,k)*pow(1-p, n-k))
        return prob #returns the probability

print(binProb(102, 100, 0.03))


'''(5) Now write a function to sample from an arbitrary discrete distribution. This function should take two 
arguments. The first is a list of arbitrarily labeled events and the second is a list of probabilities 
associated with these events. Obviously, these two lists should be the same length.'''

"""
---> Sampling sites from an alignment <---

Imagine that you have a multiple sequence alignment with two kinds of sites. One type of site pattern 
supports the monophyly of taxon A and taxon B. The second type supports the monophyly of taxon A and taxon C.
"""

'''
(6) For an alignment of 400 sites, with 200 sites of type 1 and 200 of type 2, sample a new alignment (a 
new set of site pattern counts) with replacement from the original using your function from (5). Print out 
the counts of the two types.

(7) Repeat (6) 100 times and store the results in a list.

(8) Of those 100 trials, summarize how often you saw particular proportions of type 1 vs. type 2. 

(9) Calculate the probabilities of the proportions you saw in (8) using the binomial probability mass function 
(PMF) from (4).

(10) Compare your results from (8) and (9).

(11) Repeat 7-10, but use 10,000 trials.'''
