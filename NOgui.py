import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_play = True

amount = int(input("Enter bet amount: "))
per_round = amount / 5

def deduct():
    global amount
    amount -= per_round

def adduct():
    global amount
    amount += per_round

def deal_card():
    card = random.choice(cards)
    return card

for i in range(5):
    print(f"this is round {i + 1}")
    user_cards = []
    computer_cards = []

    for number in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}\n")
    print(f"Computer's first card: {computer_cards[0]}")

    while user_score < 21:
        hit_or_stand = input("Type 'y' to hit or 'n' to stand: ")
        if hit_or_stand == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
            break

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer's cards: {computer_cards}, computer score: {computer_score}")

    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("It's a draw!")
        elif computer_score == 0 or user_score > 21:
            print("Computer wins!")
            deduct()
        elif user_score == 0 or computer_score > 21:
            print("You win!")
            adduct()
        elif user_score > computer_score:
            print("You win!")
            adduct()
        else:
            print("Computer wins!")
            deduct()

    compare(user_score, computer_score)

    play = input("Do you want to play another round of Blackjack? Type 'y' or 'n': ")
    if play != 'y':
        is_play = False

print(f"Your final amount is {amount}")
