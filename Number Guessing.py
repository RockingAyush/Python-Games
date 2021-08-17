# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:17:41 2020

@author: Ayush Padhy
"""

#Guesses game
import random
print("Welcome to the Number Guessing games:")

b=input("Enter Your Name: ")

print("Hey "+ b + " i am thinking of no. between 1 to 25.... can you guess the no. in just 6 tries? Lets see")
print(""*2)
guesses=0
number = random.randint(1, 25)
print("And Ya, dont worry,i will also help you a little")

print(""*2)
for guesses in range (6):
    print("Enter your Guess")
    a=int(input("Enter:"))
    
    if number>a:
        print("You selected a value lower than what i had thought")
        
    if number<a:
        print("You selected a value higher than what i had thought")
        
    if number==a:
        break
print(""*3)
if a == number: 
    guesses = str(guesses + 1)
    print('Good job, ' + b + '! You guessed my number in ' + guesses + " guesses!")

if a!= number: 
    guesses = str(guesses)
    print('Oh. The number I was thinking of was ' + str(number) + '.')
   


    