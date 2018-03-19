# Chapter 15 and 16 --> not circular permutations
# user input: num dice rolled/how many times rolled + binary probablility --> things with two outcomes but different weights (bais)
# program output: probablility of sum equalling some number; probability of sum = even or odd;
import math
import numpy as np
# import scipy
# from scipy.special import comb

#from scipy.special import comb
from scipy.misc import comb

def calculate_probability(p, n):
	# p = sum; n = num of dice
	#results = comb(p, n) #, exact=False, repetition=False)
	# fleaur = ((p-n)/6)
	countingSum = 0
	probablility = 0

	for k in range(0, int(math.floor((p-n)/6)) + 1): #range(0, math.floor((p-n)/6)):

		newCountingSum = math.pow(-1, k) * comb(n, k) * comb((p - 6*k - 1), (n-1))
		
		countingSum = countingSum + newCountingSum 
		
	
	probability = countingSum / (math.pow(6, n)) * 100
		
	percentage = str(probability) + "%"

	
	return percentage


x = calculate_probability(3, 3)

print x


