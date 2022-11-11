"""
Hangman game is a simple way to entertain oneself. The objective of it
is to guess a hidden word in a limited amount of attempts (6). Each attempt
one a player chooses a letter, and if the word contains it, the letter
pops up in the hidden word, otherwise they lose one life.

The program works as following: it first shows a hidden word as a dashed line.
Also a keyboard and number of left lines is displayed. Player can press any
letter on the keyboard, and if it is present in the word, one of the dashes
will turn into that letter. If a guess is wrong, the number of lives decreases
by 1. One letter can only be chosen once. If the player fails to guess
the word in 6 attempts, a "YOU LOST!" message pops up, as well as the correct word.
In case of guessing the word correctly, the player will see "YOU WON!" on their screen.
The structure of the program is divided into 2 parts, back end code for the game
and GUI code for the game.
Authors:
Name: Ngoc Mai Nguyen
Email: mai.n.nguyen@tuni.fi
Student number: 50358236
"""

import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox

'''
This part is for setting the game and the word choice from random.
The words are available in the words_list.txt file.
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']  # latin alphabet is used in the game


class game_hangman:
    """
    The central class of the program. Handles the hidden word,
    the list of all words,the displayed word and the amount of lives.
    """

    word = []
    wordslist = []
    displayed_word = [] #the displayed boards
    lives = 6 #number of lives
    answer = "" #correct final answer

    def importfile(self):
        """
        Imports file that contains the list of the words. Words are then
        transferred to a list variable "wordlist". If some error occurs,
        shows an error message.
        """

        file_name = 'words_list.txt'
        try:
            file = open(file_name, 'r')
        except OSError:
            print(f"Error: opening the file '{file_name} failed!")
            return
        file_list = []
        for file_line in file:
            file_line = file_line.rstrip()
            file_list.append(file_line)
            self.wordslist = file_list

    def choose_word(self):
        """
        Randomly chooses a word from a ready-made list using
        random library functions. Assigns the chosen word to
        the "word" variable as a list.
        """

        word = random.choice(self.wordslist)
        self.answer = word
        self.word = list(word)

    def initialdisplay_word(self, word):
        """
        Determines the chosen word as a dashed line in the initial conditions.
        :param word: (list) length of the chosen word tells the number of dashes
        """

        displayed_word = ['-'] * len(word)
        self.displayed_word = displayed_word

    def change_letter(self, letter):
        """
        This function reveals a guessed letter in the displayed word.
        :param letter: (str) a letter guessed
        """

        location = self.word.index(letter)
        self.displayed_word[location] = str(letter)


game_hangman()  # sets up the back-end part of the program
game_hangman.importfile(game_hangman)  # by opening a file,
game_hangman.choose_word(game_hangman)  # choosing a word and
game_hangman.initialdisplay_word(game_hangman, game_hangman.word) # letting that word be displayed.

"""
This part is for setting the GUI for the game and operations for virtual 
keyboard.
"""

mainw = Tk()
mainw.geometry("350x400") #setting up the size of the game board
mainw.resizable(0, 0) #the game board is not resizable
for i in range(7):
    mainw.columnconfigure(i, weight=1) #configure the grid (columns)
for j in range(9):
    mainw.rowconfigure(j, weight=1) #configure the grid (rows)

mainw.title("HANGMAN GAME") #Title of the game
mainw.option_add("*Font", "Courier 15") #Font and size of the whole game board
#Setting up the label
mainw._gametitle = Label(mainw, text="HANGMAN GAME")
mainw._gametitle.grid(row=0, columnspan=7)

#Setting up the displayed game board
mainw._displayboard = Label(mainw, text=game_hangman.displayed_word)
mainw._displayboard.grid(row=2, columnspan=7)

#setting up the displayed for lives left
mainw._livesavailable = Label(mainw, text=f"Lives left: {game_hangman.lives}")
mainw._livesavailable.grid(row=3, columnspan=7)


def createButton(letter, rownum, columnnum, index):
    """
    This function create a Tkinter Button for each Alphabet letter with command
    :param letter: (str) a letter guessed
    :param rownum: (int) index for row
    :param columnnum: (int) index for column
    :param index: (int) index of letter in the alphabet
    """
    if index % 2 == 0:
        color = None
    else:
        color = "white"
    letter = tk.Button(mainw, text=f"{letter}",
                       command=lambda: click(letter, alphabet[index]),
                       bd=10, bg=color)
    letter.grid(column=columnnum, row=rownum)


def updateDisplayedWord(letter):
    """
    This function updated the displayed gamboard after the player guessed it
    :param letter: (str) a letter guessed
    """
    displayboard = Label(mainw, text=game_hangman.displayed_word)
    displayboard.grid(row=2, columnspan=7)


def click(self, letter):
    """
    This function if for the Button's command.
    It will update the displayed gameboard, update lives left, and
    disable the Button so player can not choose a letter twice.
    :param letter: (str) a letter guessed
    """
    self.config(state='disabled')
    if letter not in game_hangman.word:
        game_hangman.lives -= 1
    else:
        game_hangman.change_letter(game_hangman, letter)
        updateDisplayedWord(letter)
    if game_hangman.lives == 0:
        message = Label(mainw, text=f"YOU LOST!")
        message.grid(row=1, columnspan=7)
        messagebox.showinfo("Result",
                            f"YOU LOST! Correct word: {game_hangman.answer}.")
    elif game_hangman.displayed_word == game_hangman.word:
        message = Label(mainw, text="YOU WON!")
        message.grid(row=1, columnspan=7)
        messagebox.showinfo("Result",
                            f"YOU WON! Correct word: {game_hangman.answer}.")
    mainw._livesavailable = Label(mainw, text=f"Lives left: {game_hangman.lives}")
    mainw._livesavailable.grid(row=3, columnspan=7)

#Setting up the virtual keyboard
rownum = 4
columnnum = 0
for letter in alphabet:
    index = alphabet.index(letter)
    createButton(letter, rownum, columnnum, index)
    columnnum += 1
    if columnnum == 7:
        columnnum = 0
        rownum += 1

mainw.mainloop()

'''
End of GUI Game 
'''
