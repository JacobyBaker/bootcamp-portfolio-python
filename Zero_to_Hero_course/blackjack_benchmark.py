'''
This is a script to play a basic game of Blackjack.
I made this script as a part of the Udemy Pythoun Course From Zero to Hero.
I may eventually make the script be abel to:
have multiple players, include splits and doubling down, and more complicated blackjack rules.
But for now, this is my first OOP script!
Written by: Jacoby Baker
To call scipt: python blackjack_benchmark.py
'''

# import random so we can use the shuffle feature for the deck
import random

# SUIT, RANK, VALUE
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Define Classes
class Card:
    '''Create the Card class and define the suits, rank of cards, and values of the cards'''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit



class Deck():
    '''Create the Deck class'''
    def __init__(self,decks):
        self.all_cards = []
        self.decks = decks

        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        # Take in the num_of_decks to determine how many decks to use
        self.all_cards = self.all_cards * self.decks
    def shuffle(self):
        '''Make it so the deck and shuffle'''
        random.shuffle(self.all_cards)
    def deal_one(self):
        '''Define a way to deal a card'''
        return self.all_cards.pop(0)

class Player():
    '''Create Player class'''
    def __init__(self,name,chips=100):
        self.name = name
        self.chips = chips
    def place_bet(self):
        '''Define placing a bet. Take in an input from the player for how much they want to bet.'''
        while True:
            try:
                num_chips = int(input("Place bet: "))
                if int(num_chips) > self.chips:
                    print(f"{self.name} doesn't have enough chips for that bet!")
                elif bet in range(0,self.chips):
                    self.chips -= num_chips
                    print(f"{self.name} placed a bet of {num_chips} chips.")
                    return num_chips
            except: # Make sure the input is an integer and that there are enough chips to place the bet.
                print("Bet must be a number!")
                continue
    def collect_winnings(self,chip_bet):
        '''define how to collect the winnings'''
        self.chips += chip_bet
    def __str__(self):
        '''Define a string to print if called'''
        return f'{self.name} has {self.chips} chips.'

class Hand():
    '''Create a Hand class that can be used for either the player or dealer'''
    def __init__(self):
        self.cards = [] # Start with an empty list. This will fill with the cards that are dealt.
        self.value = 0 # Total value of the hand
        self.aces = 0 # Keep track of how many aces the hand has.
    def add_card(self,card):
        '''Add a card to the hand and ajust self.value self.aces if necessary'''
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1
    def adjust_for_ace(self):
        '''If the self.hand value > 21 and at least 1 ace, change the ace's value to 1'''
        if self.aces > 0:
            while self.value > 21:
                self.value = 0
                for j in range(len(self.cards)):
                    if self.cards[j].rank == "Ace":
                        self.cards[j].value = 1
                        self.value += self.cards[j].value
                        self.aces -= 1
                        print("Ace's value changed to 1")
                    else:
                        self.value += self.cards[j].value
    def __str__(self):
        '''Return the value of the hand'''
        return f"{self.value}"


# Create some functions for gameplay
def num_decks():
    '''Ask how many decks of cards to play with. This will be fed into the Deck() class'''
    while True:
        try:
            n_decks = int(input("How many decks of cards do you want to play with? "))
            if type(n_decks) == int:
                print(f"You will be playing with {n_decks} decks.")
                return n_decks
                # break
        except:
            print("Invalid choice! Please pick a number of decks to play with.\n")
            continue

def deal_round(deck,player,player_hand,d_hand):
    '''deal the round'''
    for i in range(2):
        player_hand.add_card(deck.deal_one())
        d_hand.add_card(deck.deal_one())
    print(f"\n**********\nThe dealer has a {d_hand.cards[1]} face up.")
    print(f"{player.name}'s hand: {player_hand.cards[0]} and {player_hand.cards[1]} for a total of {player_hand.value}")

def player_bust_check(player,player_hand):
    '''Check to see if the player has busted (hand value > 21)'''
    if player_hand.value > 21:
        print(f"{player.name} BUSTED!")
        return True

def dealer_bust_check(d_hand):
    '''Check to see if the dealer has busted (hand value > 21)'''
    if d_hand.value > 21:
        print("The dealer BUSTED!")
        return True

def hit_or_stay(deck,player_hand,player):
    '''Make a function for the player to ask if they want to hit on their current hand value or stay.'''
    busted = False
    if player_hand.value == 21: # If the player gets a Blackjack, print that.
        print("BLACKJACK!!!")
    while player_hand.value < 21: # While the player's hand is under 21, ask if they want to hit or stay.
        hit = input("\nDo you want to hit? (Yes or No)").capitalize()
        if hit not in ["Yes", "Y", "No", "N"]:
            print("Invalid choice!")
        elif hit in ["Yes","Y"]: # If hit, deal them another card.
            print(f"{player.name} hits!")
            player_hand.add_card(deck.deal_one())
            print(f"{player_hand.cards[-1]} added for a total value of {player_hand.value}")
            player_hand.adjust_for_ace() # If player's hand is >21 check if there is an ace to adjust
            busted = player_bust_check(player,player_hand) # If the player's hand's final value  >21 print BUSTED!
            print(f"\n{player.name}'s hand has a value of {player_hand.value}")
        else:
            break
    if busted:
        player_hand.value = 0 # Used to trigger the dealer to not play if the player busts. It will also be used in the check_winner() function

def dealer_play(deck,d_hand,player_hand):
    '''Define the dealer's play. The dealer will hit until their hand's value is 17 or higher.'''
    if player_hand.value == 0: # If the player busted, do nothing.
        pass
    else:
        if d_hand.value == 22: # A check to see if the dealer has two Ace's on the deal. If so, make one's value 1.
            d_hand.adjust_for_ace()
        busted = False
        hitting = True
        print(f"\nThe dealer's hand: {d_hand.cards[0]} and {d_hand.cards[1]} for a total of {d_hand.value}")
        while hitting:
            if d_hand.value < 17:
                print("The dealer hits!")
                d_hand.add_card(deck.deal_one())
                print(f"{d_hand.cards[-1]} added for a total value of {d_hand.value}")
                d_hand.adjust_for_ace()
            else:
                hitting = False
            busted = dealer_bust_check(d_hand)
        if busted:
            d_hand.value = 0

def winner_check(player,player_hand,d_hand):
    '''Compare the value's of the player and dealer's hads to see who wins. Return who the winner is.'''
    print(f"\n**********\n{player.name} has {player_hand.value} VS the dealer's {d_hand.value}")
    if player_hand.value > d_hand.value:
        print(f"{player.name} beat the dealer!")
        return "Player"
    elif player_hand.value < d_hand.value:
        print("The dealer won!")
        return "Dealer"
    else:
        print("TIE!")
        return "TIE"

def payout(winner,player,chips):
    '''Take in the output of the winner_check() to determine where the bet should go.'''
    print("\n**********\n")
    if winner == "Player": #If the player won, double the bet and return the chips.
        winnings = chips*2
        player.collect_winnings(winnings)
        print(f"\nCongratulations {player.name}, you won {winnings} chips!")
    elif winner == "Dealer": # If the dealer won, nothing.
        print(f"\nSorry {player.name}, you lost your bet of {chips} chips!")
    else: # If Tie, return the bet to the player.
        player.collect_winnings(chips)
        print("\nThis round was a tie, no one wins.")
    print(f"{player.name} has {player.chips} chips left!")

def play_again():
    '''Ask if the player would like to play again.'''
    print("\n**********\n")
    play = input("\nDo you want to play again? (Yes or No)").capitalize()
    if play[0] not in ["Y","N"]:
        print("Invalid choice!")
    elif play[0] == "Y":
        return True
    else:
        return False

# game logic
game_on = True

print("Welcome to the Blackjack table! You have a starting balance of 100 chips. \n\nGood luck!\n")

num_of_decks = num_decks()

# Make a deck, shuffle it
new_deck = Deck(num_of_decks)
new_deck.shuffle()

# Create player (input for name?) - Provide a 'bank roll/chips'
player_one = Player(input("Who is playing? "))

while game_on:

    # Ask player for a bet. Check that the player has enough chips to make said bet.
    bet = 0
    bet = player_one.place_bet()

    # Deal the cards, dealer:(face down/face up), plaeyer(face up/face up)
    player1_hand = Hand()
    dealer_hand = Hand()
    deal_round(new_deck,player_one,player1_hand, dealer_hand)


    # Ask the player if they want to Hit,
    hit_or_stay(new_deck,player1_hand,player_one)

    # When player's hand is <= 21 and they stay, dealer plays
    dealer_play(new_deck,dealer_hand,player1_hand)

    # Compare hands to see who wins
    winning_hand = winner_check(player_one,player1_hand,dealer_hand)
    payout(winning_hand,player_one,bet)

    # Ask if player would like to play again.
    game_on = play_again()

print("Thanks for playing!")
