#!/usr/bin/env python
# coding: utf-8

#This is a simple rock, paper scissors game where you play against comp

import random

def game(player1):
    choice =['rock','paper','scissors']
    computer = random.choice(choice)
    print("-------------------------------------")
    print("You played -",player1.upper())
    print('Computer plays -',computer.upper())
    print("-------------------------------------")
    if player1 == computer:
        print("It's a tie")
    elif player1=='rock' and computer=='scissors':
        print('Player wins')
    elif player1=='rock' and computer=='paper':
        print('Computer wins')
    elif player1=='paper' and computer=='scissors':
        print('Computer wins')
    elif player1=='paper' and computer=='rock':
        print('You win')
    elif player1=='scissors' and computer=='rock':
        print('Computer wins')
    elif player1=='scissors' and computer=='paper':
        print('Good game, you won!')
    else:
        print('Oops, something went wrong, try again')
        playgame()
        
    print("Thanks for playing!")
    print("-------------------------------------")
    print("Would you like to try again ? Y/N")
    again = input().lower()
    if again=='y' or again=='yes':
        print("Lets go again")
        print("-------------------------------------")
        playgame()
    else:
        print("See you later!")
        print("-------------------------------------")
    return 

def playgame():
    print("---------ROCK PAPER SCISSORS---------")
    print("-------------------------------------")
    print("You have a choice of \n -ROCK \n -SCISSORS \n -PAPER")
    play= input('Enter a choice from above - ').lower()
    return game(play)

if __name__=="__main__":
    print("---------ROCK PAPER SCISSORS---------")
    print("-------------------------------------")
    print("You have a choice of \n -ROCK \n -SCISSORS \n -PAPER")
    play= input('Enter a choice from above - ').lower()
    game(play)
    



