#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:42:42 2022

@author: dan
"""
import secrets
from collections import Counter # for frequency analysis 
import time
CHARS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # all of the possible characters 

otpadkey = [] 

startTime = time.time()

for j in range(500000): # the length of the keys 
    otpadkey.append(secrets.choice(CHARS))
    
print(Counter(otpadkey))    #quick frequency analysis to see the distribution of randomness 

otpadkey=''.join(otpadkey)     # Join each element in the list to make a string without spaces. For use in lists 

print('Time in seconds it took to create this key: '+ str(time.time()-startTime))    

otpadkey = [] # reset the key after usage 

