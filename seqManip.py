# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 11:06:50 2015

@author: Ana Carolina Arcanjo, e-mail: a.arcanjo@gmail.com
"""


"""
With the skills you have now learned in the first part of this script, try this
exercise:
*** Sequence Manipulation Exercise ***
"""

'''- At the beginning of the script, define a DNA sequence (taken from
https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)'''

dnaSeq = 'aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggc' #defines the string DNA
#the last two nucleotides tg were deleted so the last two functions could run without exceptions

'''- Print the length of the sequence to the screen along with text explaining
the value'''

print 'The sequence length is:', len(dnaSeq) #prints the length of the DNA sequence


'''- Create and store the RNA equivalent of the sequence, then print to screen.'''

rnaSeq = '' #creates an empty string to store the RNA equivalent of dnaSeq
for i in range(len(dnaSeq)): #looks each nucleotide in dnaSeq
    if dnaSeq[i] == 't': #adds u to the rnaSeq if the ith element in dnaSeq is a t
        rnaSeq = rnaSeq + 'u'
    else: #adds the other nucleotides to rnaSeq
        rnaSeq = rnaSeq + dnaSeq[i]
        
print(rnaSeq) #prints the RNA equivalent of dnaSeq


'''- Create and store the reverse complement of your sequence, then print to
screen.'''

revComp = '' #creates an empty string to store the reverse complement of dnaSeq
for i in range(len(dnaSeq)): #looks each nucleotide in dnaSeq 
    if dnaSeq[i] == 'a': #adds timine to the reverse complement of dnaSeq
        revComp = revComp + 'T'
    elif dnaSeq[i] == 't': #adds Adenine to the reverse complement of dnaSeq
        revComp = revComp + 'A'
    elif dnaSeq[i] == 'g': #adds citosine to the reverse complement of dnaSeq
        revComp = revComp + 'C'
    else: #adds guanine to the reverse complement of dnaSeq
        revComp = revComp + 'G'
        
revComp = revComp.lower() #converts revComp to lowercase.

print(revComp) #prints the reverse complement of dnaSeq to the screen
        

'''- Extract the bases corresponding to the 13rd and 14th codons from the
sequence, then print them to the screen.'''

codon_list = [] #creates an empty list to store the codons in dnaSeq
for n in range(0, len(dnaSeq), 3): #searches dnaSeq from the beginning to the end, with an interval of 3 bases
    codon = dnaSeq[n:n+3] #defines a codon
    codon_list.append(codon) #adds the codon to the codon_list
    
    
print(codon_list[12]+codon_list[13]) #prints the sequence for the 13rd and 14th codons in dnaSeq
    

'''- Create a function to translate the nucleotide sequence to amino acids
using the vertebrate mitochondrial genetic code (available from
https://github.com/jembrown/CompPhylo_Spr2015/blob/master/VertMitTransTable.txt).'''


aa = ['F','L','I','M','V','S','P','T','A','Y',
      '*','H','Q','N','K','D','E','C','W','R',
      'G'] #defines the list of amino acids

codons = [['TTT', 'TTC'],
          ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
          ['ATT', 'ATC'],
          ['ATG', 'ATA'],
          ['GTT', 'GTC', 'GTA', 'GTG'],
          ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
          ['CCT', 'CCC', 'CCA', 'CCG'],
          ['ACT', 'ACC', 'ACA', 'ACG'],
          ['GCT', 'GCC', 'GCA', 'GCG'],
          ['TAT', 'TAC'],
          ['TAA', 'TAG', 'AGA', 'AGG'],
          ['CAT', 'CAC'],
          ['CAA', 'CAG'],
          ['AAT', 'AAC'],
          ['AAA', 'AAG'],
          ['GAT', 'GAC'],
          ['GAA', 'GAG'],
          ['TGT', 'TGC'],
          ['TGA', 'TGG'],
          ['CGT', 'CGC', 'CGA', 'CGG'],
          ['GGT', 'GGC', 'GGA', 'GGG']] #defines the list of codons

def amino(codon):
    '''takes as input a codon string (a string of three letters) and returns
     the corresponding vertebrate mitochondrial amino acid.'''
    for i in range(len(aa)): #checks the index of each amino acid in aa list
         for s in range(len(codons[i])): #checks the index of the codons lists
            if codons[i][s] == codon: #looks at each element in the codons list and compares to input
                return aa[i] #returns the amino acid if matches
            else:
                s = s + 1 #looks at the other element in the same index in the codons list if there is no match

def codingStrandToAA(DNA):
    '''Takes a sequence of DNA nucleotides from the coding strand and returns 
    the corresponding amino acids as a string.'''
    aaSeq = '' #creates an empty string to store the amino acid sequence
    DNA = DNA.upper() #uppercase the dnaSeq (if not uppercased already)
    for index in range(0, len(DNA), 3): #creates the index from 0 to the end of the sequence, with increase of 3
        codon = DNA[index:index+3] #defines a codon in the dnaSeq
        aaSeq = aaSeq + amino(codon) #adds the corresponding amino acid to the amino acid sequence by calling the amino() function
    return aaSeq #returns the resulting amino acid sequence


'''- Translate the sequence and print it to the screen.'''

print(codingStrandToAA(dnaSeq)) #prints the translated sequence to the screen
