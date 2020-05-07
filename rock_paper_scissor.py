""" This file is to program rock paper scissors game with PC"""

import random


class game(object):
    """ Rock paper scissors game class with PC"""

    def __init__(self):
        self.game_choices = ['rock', 'paper', 'scissors']

    def your_guess(self):
        """ Guess one of rock paper scissors"""
        guess = input("Enter your guess: ")
        guess = guess.lower()
        if guess in self.game_choices:
            return guess
        else:
            print("Your guess is not a valid choice, try again!")

    def pc_guess(self):
        """This function prints a random choice by PC from the given list"""
        return random.choice(self.game_choices)

    def lets_play(self):
        """ This function is to play the game specified number of turns from user"""
        guess = self.your_guess()
        if guess in self.game_choices:
            pc_guess = self.pc_guess()
            print(pc_guess)
        if guess == "rock":
            if pc_guess == "rock":
                print("It's a tie")
            elif pc_guess == "paper":
                print("I win!")
            else:
                print("you win")
        if guess == "paper":
            if pc_guess == "rock":
                print("You win!")
            elif pc_guess == "paper":
                print("It's a tie!")
            else:
                print("I win")
        if guess == "scissors":
            if pc_guess == "rock":
                print("I win!")
            elif pc_guess == "paper":
                print("you win!")
            else:
                print("It's a tie")
