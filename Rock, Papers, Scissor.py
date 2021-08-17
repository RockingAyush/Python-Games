# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:44:10 2020

@author: Ayush Padhy
"""

from random import randint
A = "Yes"
while A =="Yes" or A == "yes":
    player = input('rock (r), paper (p) or scissors (s)? ')
    print("Player =", player) 
    if player == "r" or player == "p" or player == "s":
        chosen = randint(1,3)
        if chosen == 1 :
            computer = 'r'
            print("Computer =", computer)
        elif chosen == 2 :
            computer = 'p'
            print("Computer =", computer)
        elif chosen == 3 :
            computer = 's'
            print("Computer =", computer)
        if player == computer:
            print('DRAW!')
        elif player == 'r' and computer == 's':
            print('Player wins!')
        elif player == 'r' and computer == 'p':
            print('Computer wins!')
        elif player == 'p' and computer == 'r':
            print('Player wins!')
        elif player == 'p' and computer == 's':
            print('Computer wins!')
        elif player == 's' and computer == 'p':
            print('Player wins!')
        elif player == "s" and computer == 'r':
            print('Computer wins!')
    else:
        print('Pls note that we are playing Rock, Paper and scissors!!!!')
    A = input("Do you want to play more(Yes/No)? ")