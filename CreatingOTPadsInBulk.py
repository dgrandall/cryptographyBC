#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:42:42 2022

@author: dan
"""
import secrets
CHARS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # all of the possible characters 

otpadkey = [] 
for i in range(1,501): # The number of keys to generate
    for j in range(500): # the length of the keys 
        otpadkey.append(secrets.choice(CHARS))
    otpadkey=''.join(otpadkey)     # for use in lists 

    otpkeysfile = open('/home/dan/Documents/OneTimePad/otpkeysfile.txt','a') # input your own file path. Ensure to use the correct syntax for your operating system
    otpkeysfile.write(str(i))
    otpkeysfile.write("::")
    otpkeysfile.write(otpadkey)
    otpkeysfile.write(",\n")
    otpkeysfile.close()
    
    otpadkey = [] # extremely important to reset this to an empty list 

