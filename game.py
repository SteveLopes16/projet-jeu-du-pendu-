import tkinter as tk
from tkinter import ttk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Pendu")
        self.words = ["python", "programming", "hangman", "developer", "interface"]
        self.word_to_guess = random.choice(self.words)
        self.guessed_word = ["_" for _ in self.word_to_guess]
        self.attempts_left = 6
        self.guessed_letters = set()
        self.create_widgets()

    def create_widgets(self):
        # Écran d'affichage du mot à deviner
        self.word_label = ttk.Label(self.root, text=" ".join(self.guessed_word), font=('Arial', 20))
        self.word_label.grid(row=0, column=0, columnspan=6)

        # Entrée pour les lettres devinées
        self.letter_entry = ttk.Entry(self.root, font=('Arial', 20))
        self.letter_entry.grid(row=1, column=0, columnspan=4)
        
        # Bouton pour soumettre la lettre
        self.guess_button = ttk.Button(self.root, text="Deviner", command=self.guess_letter)
        self.guess_button.grid(row=1, column=4)

        # Label pour afficher les tentatives restantes
        self.attempts_label = ttk.Label(self.root, text=f"Tentatives restantes: {self.attempts_left}", font=('Arial', 15))
        self.attempts_label.grid(row=2, column=0, columnspan=6)

        # Label pour afficher les lettres déjà devinées
        self.guessed_letters_label = ttk.Label(self.root, text=f"Lettres devinées: {', '.join(self.guessed_letters)}", font=('Arial', 15))
        self.guessed_letters_label.grid(row=3, column=0, columnspan=6)

    def guess_letter(self):
        letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)
        
        if letter in self.guessed_letters or len(letter) != 1 or not letter.isalpha():
            return

        self.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            for index, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[index] = letter
        else:
            self.attempts_left -= 1

        self.update_widgets()

        if self.attempts_left <= 0:
            self.end_game(False)
        elif "_" not in self.guessed_word:
            self.end_game(True)

    def update_widgets(self):
        self.word_label.config(text=" ".join(self.guessed_word))
        self.attempts_label.config(text=f"Tentatives restantes: {self.attempts_left}")
        self.guessed_letters_label.config(text=f"Lettres devinées: {', '.join(self.guessed_letters)}")

    def end_game(self, won):
        result_text = "Vous avez gagné!" if won else f"Vous avez perdu! Le mot était '{self.word_to_guess}'."
        self.word_label.config(text=result_text)
        self.guess_button.config(state=tk.DISABLED)
        self.letter_entry.config(state=tk.DISABLED)
