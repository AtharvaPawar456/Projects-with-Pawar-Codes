# Hangman Game with a GUI

# pip install tkinter

import tkinter as tk
from tkinter import messagebox

# Initialize the game
word = "hangman"
guesses = []
remaining_attempts = 6

def check_letter(letter):
    global remaining_attempts
    if letter in guesses:
        return
    guesses.append(letter)
    if letter not in word:
        remaining_attempts -= 1
        if remaining_attempts == 0:
            messagebox.showinfo("Hangman", "You lost!")
            window.destroy()
    else:
        if all(char in guesses for char in word):
            messagebox.showinfo("Hangman", "You won!")
            window.destroy()

def create_buttons():
    buttons_frame = tk.Frame(window)
    buttons_frame.pack()

    for letter in "abcdefghijklmnopqrstuvwxyz":
        button = tk.Button(buttons_frame, text=letter.upper(), width=4, command=lambda l=letter: check_letter(l))
        button.pack(side=tk.LEFT)

def create_word_label():
    word_frame = tk.Frame(window)
    word_frame.pack()

    for char in word:
        if char in guesses:
            label = tk.Label(word_frame, text=char.upper() + " ")
        else:
            label = tk.Label(word_frame, text="_ ")
        label.pack(side=tk.LEFT)

# Create the main window
window = tk.Tk()
window.title("Hangman")

# Create the game elements
create_word_label()
create_buttons()

# Run the game loop
window.mainloop()
