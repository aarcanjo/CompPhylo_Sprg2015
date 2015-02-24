# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 18:28:32 2015
Discrete-time Markov chains

@author: Ana Arcanjo
"""

"""
In this exercise, we will explore Markov chains that have discrete state spaces
and occur in discrete time steps. To set up a Markov chain, we first need to
define the states that the chain can take over time, known as its state space.
To start, let's restrict ourselves to the case where our chain takes only two
states. We'll call them A and B.
"""

# Create a tuple that contains the names of the chain's states
markovStates = ('A','B')
print markovStates
print markovStates[0]


"""
The behavior of the chain with respect to these states will be determined by
the probabilities of taking state A or B, given that the chain is currently in
A and B. Remember that these are called conditional probabilities (e.g., the
probability of going to B, given that the chain is currently in state A is
P(B|A).)
We record all of these probabilities in a transition matrix. Each row
of the matrix records the conditional probabilities of moving to the other
states, given that we're in the state associated with that row. In our example
row 1 will be A and row 2 will be B. So, row 1, column 1 is P(A|A); row 1,
column 2 is P(B|A); row 2, column 1 is P(A|B); and row 2, column 2 is P(B|B).
All of the probabilities in a ROW need to sum to 1 (i.e., the total probability
associated with all possibilities for the next step must sum to 1, conditional
on the chain's current state).
In Python, we often store matrices as "lists of lists". So, one list will be
the container for the whole matrix and each element of that list will be
another list corresponding to a row, like this: mat = [[r1c1,r1c2],[r2c1,r2c2]].
We can then access individual elements use two indices in a row. For instance,
mat[0][0] would return r1c1. Using just one index returns the whole row, like
this: mat[0] would return [r1c1,r1c2].
Define a transition matrix for your chain below. For now, keep the probabilties
moderate (between 0.2 and 0.8).
"""

# Define a transition probability matrix for the chain with states A and B
trans_probs = [[0.6, 0.4], 
               [0.3, 0.7]]
# Try accessing a individual element or an individual row
# Element
transAB = trans_probs[0][1]
print transAB
# Row
transB = trans_probs[1]
print transB


"""
Now, write a function that simulates the behavior of this chain over n time
steps. To do this, you'll need to return to our earlier exercise on drawing
values from a discrete distribution. You'll need to be able to draw a random
number between 0 and 1 (built in to scipy), then use your discrete sampling
function to draw one of your states based on this random number.
"""
# Import scipy U(0,1) random number generator
import scipy
# Paste or import your discrete sampling function
from discSamp import *
# Write your Markov chain simulator below. Record the states of your chain in
# a list. Draw a random state to initiate the chain.
def markovSim(states, prob_matrix, steps):
    '''This function takes as input a tuple or list of states in a Markov chain,
    the matrix of transition probabilities associated with those states and the
    number of steps to create the resulting Markov chain.'''
    if steps < 0: #dummy check for invalid value for steps
        return 'Invalid number of steps. Must be positive integer.'
    initialState = random.choice(states) #draws the first state with equal probability
    markov_chain = [] #creates the list to store the Markov chain
    markov_chain.append(initialState) #appends the first state to the Markov chain
    n = 0 #sets the starting index of the Markov list
    while n <= steps-1: #sets the number of "steps" to run the chain
        if markov_chain[n] == states[0]: #checks if the current element is state[0]
            nextState = discSamp(states, prob_matrix[0]) #if it's true, draws the next state based on the transition probabilities of state[0]
            markov_chain.append(nextState) #appends it to the Markov chain
        else: 
            nextState = discSamp(states, prob_matrix[1])
            markov_chain.append(nextState)
        n += 1 #increases the value of n to look at the next index
    return markov_chain
        
# Run a simulation of 10 steps and print the output.
print markovSim(markovStates, trans_probs, 10)
'''['A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B']'''

# ----> Try to finish the above lines before Tues, Feb. 10th <----
# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?
countA = 0
countT = 0
countC = 0
countG = 0
i = 0
while i < 100:
    sim_chain = markovSim(nucleotides, nucl_transition, 100)    
    if sim_chain[-1] == 'A':
        countA += 1
    elif sim_chain[-1] == 'T':
        countT += 1
    elif sim_chain[-1] == 'C':
        countC += 1
    else:
        countG += 1
    i += 1
    
#print 'The simulated Markov chains end in A in about:', countA, 'times.'
#print 'The simulated Markov chains end in B in about:', countB, 'times.'
'''The simulated Markov chains end in A in about: 38 times.
The simulated Markov chains end in B in about: 62 times.'''    
# Try defining a state space for nucleotides: A, C, G, and T. Now define a
# transition matrix with equal probabilities of change between states.
nucleotides = ['T', 'A', 'C', 'G']
nucl_transition = [[.5, .125, .25, .125],
                   [.125, .5, .125, .25],
                   [.25, .125, .5, .125],
                   [.125, .25, .125, .5]]
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
print 'A: ', countA, 'C: ', countC, 'T: ', countT, 'G: ', countG                  
'''A:  23 C:  29 T:  23 G:  25, for transition probs equal:
nucl_transition = [[.25, .25, .25, .25],
                   [.25, .25, .25, .25],
                   [.25, .25, .25, .25],
                   [.25, .25, .25, .25]]'''
'''A:  47 C:  13 T:  25 G:  15 for transition probs :
nucl_transition = [[.5, .125, .25, .125],
                   [.125, .5, .125, .25],
                   [.25, .125, .5, .125],
                   [.125, .25, .125, .5]]'''
            
