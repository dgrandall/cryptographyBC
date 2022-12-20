#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 01:45:35 2022

@author: dan
"""

import sys 
from termcolor import cprint 


CHARACTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def translateMessage(key,message,mode):

    translated = [] # stores the encrypted/decrypted message string
    keyIndex = 0 # tracks which subkey to use. 
    #key = key.upper() #The program assumes that the key is in all uppercase letters. To make
    # sure the key is valid, this line calls upper() on key.
    for symbol in message: # Loop through each symbol in message. 
        #num = CHARACTERS.find(symbol.upper())
        num = CHARACTERS.find(symbol)
        if num != -1: # -1 means symbol.upper() was not found in CHARACTERS. 
            if mode == 'encrypt':
                num += CHARACTERS.find(key[keyIndex]) # add if encrypting 
            elif mode == 'decrypt': # the subkey will always evaluate to key[keyIndex]
                num -= CHARACTERS.find(key[keyIndex]) # subtract if decrypting
                
            num %= len(CHARACTERS) # Handle any wraparound . Assigns num to the remainder of the equation num % len(CHARACTERS)
            
            translated.append(CHARACTERS[num])
            # add the encrypted / decrypted symbol to the end of translate: 
            #if symbol.isupper(): 
                #translated.append(CHARACTERS[num])
            #elif symbol.islower(): 
                #translated.append(CHARACTERS[num].lower())
            
            keyIndex += 1 #Move to the next letter in the key. 
            if keyIndex == len(key): 
                keyIndex = 0 
        
        else: 
            # append the symbol without encrypting/decrypting 
            translated.append(symbol)
    
    return ''.join(translated)

def encryptMessage(key,message):
    return translateMessage(key,message,'encrypt')

def decryptMessage(key,message):
    return translateMessage(key,message,'decrypt')
    

    
cprint("please paste your message here (must not exceed 500 characters): ",'cyan')
myMessage = str(input().upper())
if len(myMessage) > 500: 
    cprint('This message is too long please rerun the program and paste a shorter message', 'red')
    sys.exit()
 

cprint("please paste your designated key here: ",'cyan')
myKey = str(input())

cprint("please input either encrypt or decrypt: ",'cyan')
myMode = str(input())
if myMode != 'encrypt' and myMode != 'decrypt': 
    cprint('Invalid mode input. Please rerun the program and enter either encrypt or decrypt','red')
    sys.exit()
    
if myMode == 'encrypt': # this function is one of the starting points for the entire script
    translated = encryptMessage(myKey,myMessage)

if myMode == 'decrypt': # this function is one of the starting points for the entire script
    translated = decryptMessage(myKey,myMessage)

cprint('%sed message:' % (myMode.title()),'cyan')
print(translated)
#    pyperclip.copy(translated)
#    print()
#    print('The message has been copied to the clipboard')

    
    





    





