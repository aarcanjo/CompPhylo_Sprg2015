# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:22:57 2015

@author: arcanjo

In-Class Markov Chain Exercise

Recall from your reading that any irreducible and aperiodic Markov chain has a
stationary distribution. To convince ourselves that things will converge for
such a chain with arbitrary transition probabilities, let's give it a try.
Work in pairs for this. It's more fun to be social.
"""
# Paste your Markov chain simulation function below, where the starting state
# is drawn with uniform probability from all possible states. Remember to also
# copy any import statements or other functions on which your simulator is
# dependent.

from discreteMarkov import *
from discSamp import *

# Define a 2x2 transition matrix. For fun, don't make all the probabilities
# equal. Also, don't use any 0s or 1s (to make sure the chain is irreducible
# and aperiodic).

states = ('A', 'B')
matrix = [[0.6,0.4], [0.3,0.7]]

# Simulate a single chain for three time steps and print the states

#print markovSim(states, matrix, 3)
# ['B', 'B', 'A']
'''
everything in this multi-line comment is part of my thinking process. I did not finish this in
time, but I plan on doing it soon.

chain = ['B', 'B', 'A']
i = 1
while i < len(chain):
    if chain[i] == chain[i-1]:
        index = states.index(chain[i])
        print matrix[index]
    else:
        index = states.index(chain[i])
        print matrix[index]
    i += 1'''
# Analytically calculate the progression of states for this chain.
'''n-step transition probability:
P(state1)*P(state2, state3|state1) =
P(state1)*P(state3|state1 - doesn't matter'-, state2)*P(state2|state1)=
P(state1)*P(state2|state1)*P(state3|state2)
P(A,A,B) = P(A)*P(A|A)*P(B|A)'''
'''def chainProb(chain, states, matrix):
    ''Calculates the probability of a certain Markov Chain.''
    initProb = 1.0/len(states) #defines the probability of begining the chain in any state   
    i = 1
    while i <= len(chain):
        if chain[i] == chain[i-1]:
            stateProbs = '''
pAA, pAB, pBB, pBA = .6, .4, .7, .3
print pAA, pAB, pBB, pBA            

chain = ['B', 'B', 'A']
pChainF = .5*pBB*pBA
print pChainF
        
# Calculate the probability of observing the state in step 3, given the initial
# state in step 1 (i.e., as if you didn't know the state in step 2).
'''P(A, ?, A)= P(A)*P(A|A)*P(A|A) + P(A)*P(B|A)*P(A|B)'''

pChainF2 = (.5*pBB*pBA)+(.5*pBA*pAA)
print pChainF2
# Now think of the chain progressing in the opposite direction. What is the
# probability of the progression through all 3 states in this direction? How
# does this compare to the original direction?

pChainR = .5*pAB*pBB
print pChainR

pChainR2 = (.5*pAB*pBB)+(.5*pAA*pAB)
print pChainR2


# Try the same "forward" and "reverse" calculations as above, but with this
# transition matrix:
revMat = [[0.77,0.23],
          [0.39,0.61]]
# and these starting frequencies for "a" and "b"
freqA = 0.63 
freqB = 0.37
chain = ['B', 'B', 'A']
init_freqs = [.63, .37]

pRevChainF = freqB*revMat[1][1]*revMat[1][0]
print pRevChainF

pRevChainR = freqA*revMat[0][1]*revMat[1][1]
print pRevChainR

pRevChainF2 = (freqB*revMat[1][1]*revMat[1][0])+(freqB*revMat[1][0]*revMat[0][0])
print pRevChainF2

pRevChainR2 = (freqA*revMat[0][1]*revMat[1][1]) + (freqA*revMat[0][0]*revMat[0][1])
print pRevChainR2"""

# What is (roughly) true about these probabilities?
'''They are roughly the same (forward and reverse) no matter if you know or not 
all the steps in the chain.'''
# Simulate 1,000 replicates (or 10K if your computer is fast enough) of 25
# steps. What are the frequencies of the 2 states across replicates through time?
# NOTE: Here is a function that reports the frequencies of a state through time
# for replicate simulations. You'll need to do this several times during this exercise.

def sims(states, trans_probs, chainSize, replicates, init_probs=[.5,.5]):
    '''This function replicates the simulation of Markov Chains of n chain Sizes.'''
    sims = []
    i=0
    while i < replicates:
        if chainSize < 0: #dummy check for invalid value for steps
            return 'Invalid number of steps. Must be positive integer.'
        initialState = discSamp(states, init_probs) #draws the first state with equal probability
        markov_chain = [] #creates the list to store the Markov chain
        markov_chain.append(initialState) #appends the first state to the Markov chain
        n = 0 #sets the starting index of the Markov list
        while n < chainSize-1: #sets the number of "steps" to run the chain
            if markov_chain[n] == states[0]: #checks if the current element is state[0]
                nextState = discSamp(states, trans_probs[0]) #if it's true, draws the next state based on the transition probabilities of state[0]
                markov_chain.append(nextState) #appends it to the Markov chain
            else:
                nextState = discSamp(states, trans_probs[1])
                markov_chain.append(nextState)
            n += 1 #increases the value of n to look at the next index
        sims.append(markov_chain)
        i +=1
    return sims

test = sims(states, revMat, 3, 10)

print test

def mcStateFreqSum(sims,state="a"):
    """
    Pass this function a list of lists. Each individual list should be the
    states of a discrete-state Markov chain through time (and all the same
    length). It will return a list containing the frequency of one state
    ("a" by default) across all simulations through time.
    """
    freqs = []
    for i in range(len(sims[0])): # Iterate across time steps
        stateCount = 0
        for j in range(len(sims)): # Iterate across simulations
            if sims[j][i] == state:
                stateCount += 1
        freqs.extend([float(stateCount)/float(len(sims))])
    return freqs
    
sum1 = mcStateFreqSum(test, 'A')
sum2 = mcStateFreqSum(test, 'B')

print 'Frequency of A:', sum1
print 'Frequency of B:', sum2
# Run replicate simulations
init_freqs = [.63, .37]
revMat = [[0.77,0.23],
          [0.39,0.61]]
          
repSim = sims(states, revMat, 25, 1000, init_freqs)

# Summarize the frequency of one state through time

freqA = mcStateFreqSum(repSim, 'A')
print freqA

freqB = mcStateFreqSum(repSim, 'B')
print freqB
# What do you notice about the state frequencies through time? Try another round
# of simulations with a different transition matrix. How do the state freq.
# values change?
"""repSim10k = sims(states, revMat, 25, 10000, init_freqs)
freqA10k = mcStateFreqSum(repSim10k, 'A')
freqB10k = mcStateFreqSum(repSim10k, 'B')

print freqA10k, freqB10k
[0.6237, 0.6249, 0.6287, 0.6327, 0.6305, 0.6293, 0.6249, 0.6243, 0.6312, 0.6231, 0.6245, 0.6183, 0.6262, 0.6328, 0.6393, 0.6333, 0.6246, 0.6354, 0.6375, 0.6355, 0.6266, 0.6273, 0.6297, 0.6276, 0.6293] [0.3763, 0.3751, 0.3713, 0.3673, 0.3695, 0.3707, 0.3751, 0.3757, 0.3688, 0.3769, 0.3755, 0.3817, 0.3738, 0.3672, 0.3607, 0.3667, 0.3754, 0.3646, 0.3625, 0.3645, 0.3734, 0.3727, 0.3703, 0.3724, 0.3707]

repSim10k = sims(states, revMat, 25, 10000)
freqA10k = mcStateFreqSum(repSim10k, 'A')
freqB10k = mcStateFreqSum(repSim10k, 'B')

print freqA10k, freqB10k
[0.5022, 0.58, 0.6097, 0.6238, 0.6182, 0.6269, 0.6247, 0.6317, 0.6385, 0.6306, 0.6347, 0.6332, 0.626, 0.6309, 0.6305, 0.6363, 0.6364, 0.6387, 0.6347, 0.6287, 0.6279, 0.6311, 0.629, 0.6289, 0.6246] [0.4978, 0.42, 0.3903, 0.3762, 0.3818, 0.3731, 0.3753, 0.3683, 0.3615, 0.3694, 0.3653, 0.3668, 0.374, 0.3691, 0.3695, 0.3637, 0.3636, 0.3613, 0.3653, 0.3713, 0.3721, 0.3689, 0.371, 0.3711, 0.3754]"""

#results for a different transition matrix and initial frequencies
"""repSim10k = sims(states, matrix, 25, 10000)
freqA10k = mcStateFreqSum(repSim10k, 'A')
freqB10k = mcStateFreqSum(repSim10k, 'B')

print freqA10k, freqB10k
[0.501, 0.457, 0.4315, 0.4308, 0.4293, 0.4288, 0.4315, 0.4305, 0.4274, 0.4233, 0.4337, 0.4255, 0.4315, 0.4279, 0.4272, 0.4381, 0.4278, 0.4323, 0.4257, 0.4171, 0.4246, 0.4289, 0.4257, 0.4233, 0.432] [0.499, 0.543, 0.5685, 0.5692, 0.5707, 0.5712, 0.5685, 0.5695, 0.5726, 0.5767, 0.5663, 0.5745, 0.5685, 0.5721, 0.5728, 0.5619, 0.5722, 0.5677, 0.5743, 0.5829, 0.5754, 0.5711, 0.5743, 0.5767, 0.568]
"""
# Now, calculate a vector of probabilities for the focal state (e.g., 'a')
# based on the transition matrix directly (not by simulation). How do these
# values compare to the simulated frequencies?
