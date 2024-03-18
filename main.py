############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from replit import clear
from art import logo
import random


def deal_card():
    '''Return a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def total_point(points):
    '''Calculate the total point of the cards'''
    if (sum(points) == 21) and (len(points) == 2):
        return 0

    if 11 in points and sum(points) > 21:
        points.remove(11)
        points.append(1)

    return sum(points)


def compare(user_score, computer_score):

    if user_score == 0:
        print("You win with a Blackjack")
    elif computer_score == 0:
        print("You lose, opponent has Blackjack😱")
    elif user_score > 21:
        print("You went over. You lose😭")
    elif computer_score > 21:
        print("Opponent went over. You win😁")
    elif user_score == computer_score:
        print("Draw🙃")
    elif user_score > computer_score:
        print("You win😃")
    else:
        print("You lose😤")


def play_game():
    player_cards = []
    dealer_cards = []

    print(logo)

    for i in range(0, 2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    player_score = total_point(player_cards)
    dealer_score = total_point(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    if total_point(player_cards) == 0:
        return print("Win with a Blackjack😎")
    elif total_point(dealer_cards) == 0:
        return print("You lose. Your component has a Blackjack😱")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while another_card == 'y':

        player_cards.append(deal_card())
        player_score = total_point(player_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if (total_point(player_cards) > 21):
            return print("You went over. You lose")
        another_card = input(
            "Type 'y' to get another card, type 'n' to pass: ")

    while total_point(player_cards) < 16:
        print("You need at least 16 points to play")
        input("Type 'y' to get another card: ")
        player_cards.append(deal_card())
        player_score = total_point(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if (total_point(player_cards) > 21):
            return print("You went over. You lose")

    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = total_point(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    compare(player_score, dealer_score)

while True:
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        play_game()