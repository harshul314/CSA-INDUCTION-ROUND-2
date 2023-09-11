import random
import tkinter as tk
from tkinter import messagebox


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


user_cards = []
computer_cards = []
user_score = 0
computer_score = 0



def deal_card():
    card = random.choice(cards)
    return card

def new_game():
    global user_cards, computer_cards, user_score, computer_score
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    user_label.config(text=f"Your cards: {user_cards}, current score: {user_score}")
    computer_label.config(text=f"Computer's first card: {computer_cards[0]}")
    hit_button.config(state=tk.NORMAL)

    stand_button.config(state=tk.NORMAL)

    replay_button.config(state = tk.NORMAL)


def hit():
    global user_cards, user_score
    card = deal_card()
    user_cards.append(card)
    user_score += card
    user_label.config(text=f"Your cards: {user_cards}, current score: {user_score}")
    if user_score > 21:
        end_game("You lose!.Busted")

def stand():
    global computer_cards, computer_score
    while computer_score < 17:
        card2= deal_card()
        computer_cards.append(card2)
        computer_score = computer_score + card2
    computer_label.config(text=f"Computer's cards: {computer_cards}, score: {computer_score}")
    compare_scores()

def compare_scores():
    global user_score, computer_score
    if user_score > 21:
        end_game("You lose!")
    elif computer_score > 21:
        end_game("You win!")
    elif user_score == computer_score:
        end_game("It's a draw!")
    elif user_score > computer_score:
        end_game("You win!")
    else:
        end_game("You lose!")


def end_game(display):
    messagebox.showinfo("Game Over", display)
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)
    replay_button.config(state = tk.DISABLED)

root = tk.Tk()
root.title("Blackjack")


user_label = tk.Label(root, text="", padx=10)

user_label.pack()
computer_label = tk.Label(root, text="", padx=10)
computer_label.pack()




replay_button = tk.Button(root, text = "Replay", command = new_game, state = tk.DISABLED)
hit_button = tk.Button(root, text="Hit", command=hit, state=tk.DISABLED)
stand_button = tk.Button(root, text="Stand", command=stand, state=tk.DISABLED)
hit_button.pack()
stand_button.pack()
replay_button.pack()

new_game()

root.mainloop()






