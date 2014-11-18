'''
Created on Nov 17, 2014

@author: banderquartz
'''
import random

def roll_dice(number_sides, number_rolls):
    out = []
    for _ in range(number_rolls):
        out.append(random.randint(1, number_sides))
    return out 

for i, val in enumerate(roll_dice(6, 5)):
    print "Roll number " + str(i+1) + " resulted in " + str(val) 
