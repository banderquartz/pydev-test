'''
Created on Nov 17, 2014

@author: mike
'''
import random

def roll_dice(num_sides, num_rolls):
    out = []
    for _ in range(num_rolls):
        out.append(random.randint(1, num_sides))
    return out 

for i, val in enumerate(roll_dice(6, 5)):
    print "Roll number " + str(i+1) + " resulted in " + str(val) 