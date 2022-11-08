'''
This is a script to play a basic game of Blackjack. I made this script as a part of the Udemy Pythoun Course From Zero to Hero.
I may eventually make the script be abel to have multiple players, include splits and doubling down, and more complicated blackjack rules. But for now, this is my first OOP script!
Written by: Jacoby Baker
To call scipt: python Blackjack_benchmark.py
'''

# import random so we can use the shuffle feature for the deck
import random

# SUIT, RANK, VALUE
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

'''
Define the Classes
'''

# Create the Card class and define the suits, rank of cards, and values of the cards
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Create the Deck class
class Deck():

    def __init__(self,num_of_decks):
        self.all_cards = []
        self.num_of_decks = num_of_decks

        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        # Take in the num_of_decks to determine how many decks to use
        self.all_cards = self.all_cards * self.num_of_decks

    # Make it so the deck and shuffle
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Define a way to deal a card
    def deal_one(self):
        return self.all_cards.pop(0)


# Create Player class
class Player():

    def __init__(self,name,chips=100):
        self.name = name
        self.chips = chips

    # Define placing a bet. Take in an input from the player for how much they want to bet. Make sure that the input is an integer them make sure they have enough chips to place the bet.
    def place_bet(self):
        while True:
            try:
                bet = int(input("Place bet: "))
                if bet in range(0,self.chips):
                    self.chips -= bet
                    print(f"{self.name} placed a bet of {bet} chips.")
                    return bet
                    break
                elif int(bet) > self.chips:
                    print(f"{self.name} doesn't have enough chips for that bet!")
            except:
                print("Bet must be a number!")
                continue

    # Define how to collect the winnings
    def collect_winnings(self,bet):
        self.chips += bet

    # Define a string to print if called
    def __str__(self):
        return f'{self.name} has {self.chips} chips.'


# Create a Hand class that can be used for either the player or dealer
class Hand():
    def __init__(self):
        self.cards = [] # Start with an empty list. This will fill with the cards that are dealt.
        self.value = 0 # Total value of the hand
        self.aces = 0 # Keep track of how many aces the hand has. Will use in def to change the value of the aces if needed

    # Add a card that is dealt to the hand and ajust the value of the hand and number of aces if necessary
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    # If the hannd's value is over 21 and there is at least 1 ace in the hand, change the ace's value to 1 instead of 11
    def adjust_for_ace(self):
        if self.aces > 0:
            while self.value > 21:
                self.value = 0
                for j in (range(len(self.cards))):
                        if self.cards[j].rank == "Ace":
                            self.cards[j].value = 1
                            self.value += self.cards[j].value
                            print("Ace's value changed to 1")
                        else:
                            self.value += self.cards[j].value

    # Return the value of the hand
    def __str__(self):
        return f"{self.cards.value}"


'''
Define the functions
'''

# Create some functions for gameplay
# Ask the player how many decks of cards they want to play with. This will be fed into the Deck() class
def num_decks():
    while True:
        try:
            n = int(input("How many decks of cards do you want to play with?"))
            if type(n) == int:
                print(f"You will be playing with {n} decks.")
                return n
                break
        except:
            print("Invalid choice! Please pick a number of decks to play with.\n")
            continue


# deal the round
def deal_round(new_deck,player1_hand, dealer_hand):
    for i in range(2):
        player1_hand.add_card(new_deck.deal_one())
        dealer_hand.add_card(new_deck.deal_one())

    print(f"\n**********\nThe dealer has a {dealer_hand.cards[1].value} face up.")
    print(f"{player_one.name}'s hand: {player1_hand.cards[0]} and {player1_hand.cards[1]} for a total of {player1_hand.value}")


# Check to see if the player has busted (hand value > 21)
def player_bust_check(player,player_hand):
    if player_hand.value > 21:
        print(f"{player.name} BUSTED!")
        return True

# Check to see if the dealer has busted (hand value > 21)
def dealer_bust_check(dealer_hand):
    if dealer_hand.value > 21:
        print("The dealer BUSTED!")
        return True


# Make a function for the player to ask if they want to hit on their current hand value or stay.
def hit_or_stay(new_deck,player1_hand,player):
    busted = False
    if player1_hand.value == 21: # If the player gets a Blackjack, print that.
        print("BLACKJACK!!!")
    while player1_hand.value < 21: # While the player's hand is under 21, ask if they want to hit or stay. If hit, deal them another card.
        hit = input("\nDo you want to hit? (Yes or No)").capitalize()
        if hit not in ["Yes", "Y", "No", "N"]:
            print("Invalid choice!")
        elif hit in ["Yes","Y"]:
            print(f"{player.name} hits!")
            player1_hand.add_card(new_deck.deal_one())
            print(f"{player1_hand.cards[-1]} added for a total value of {player1_hand.value}")
            player1_hand.adjust_for_ace() # If the player's hand value is > 21 and the player has at least one ace, change the ace's value to 1.
            busted = player_bust_check(player,player1_hand) # If the player has >21 hand value and no aces to lower the value, print BUSTED!
            print(f"\n{player.name}'s hand has a value of {player1_hand.value}")
        else:
            break
    if busted:
        player1_hand.value = 0 # This will be used to trigger the dealer to not play if the player busts. It will also be used in the check_winner() function


# Define the dealer's play. The dealer will hit until their hand's value is 17 or higher.
def dealer_play(new_deck,dealer_hand,player1_hand):
    if player1_hand.value == 0: # If the player busted, do nothing.
        pass
    else:
        if dealer_hand.value == 22: # A check to see if the dealer has two Ace's on the deal. If so, make one's value 1.
                dealer_hand.adjust_for_ace()
        busted = False
        hitting = True
        print(f"\nThe dealer's hand: {dealer_hand.cards[0]} and {dealer_hand.cards[1]} for a total of {dealer_hand.value}")
        while hitting:
            if dealer_hand.value < 17:
                print("The dealer hits!")
                dealer_hand.add_card(new_deck.deal_one())
                print(f"{dealer_hand.cards[-1]} added for a total value of {dealer_hand.value}")
                dealer_hand.adjust_for_ace()
            else:
                hitting = False
            busted = dealer_bust_check(dealer_hand)
        if busted:
            dealer_hand.value = 0

# Compare the value's of the player and dealer's hads to see who wins. Return who the winner is.
def winner_check(player,player_hand,dealer_hand):
    print(f"\n**********\n{player.name} has {player_hand.value} VS the dealer's {dealer_hand.value}")
    if player_hand.value > dealer_hand.value:
        print(f"{player.name} beat the dealer!")
        return "Player"
    elif player_hand.value < dealer_hand.value:
        print("The dealer won!")
        return "Dealer"
    else:
        print("TIE!")
        return "TIE"


# Take in the output of the winner_check() to determine where the bet should go.  Print statements for who won.
def payout(winner,player,chips):
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

# Ask if the player would like to play again.
def play_again():
    print("\n**********\n")
    play = input("\nDo you want to play again? (Yes or No)").capitalize()
    if play[0] not in ["Y","N"]:
        print("Invalid choice!")
    elif play[0] == "Y":
        return True
    else:
        return False


'''
Make the game logic!
'''
# game logic
game_on = True

print("Welcome to the Blackjack table! You have a starting balance of 100 chips. \n\nGood luck!\n")

num_of_decks = num_decks()

# Make a deck, shuffle it
new_deck = Deck(num_of_decks)
new_deck.shuffle()

# Create player (input for name?) - Provide a 'bank roll/chips'
player_one = Player(input("Who is playing?"))

while game_on:

    # Ask player for a bet. Check that the player has enough chips to make said bet.
    bet = 0
    bet = player_one.place_bet()

    # Deal 1 card to player (face up), one to dealer (face down), one to player (face up), and one to dealer (face up)
    player1_hand = Hand()
    dealer_hand = Hand()
    deal_round(new_deck,player1_hand, dealer_hand)


    # Ask the player if they want to Hit, If yes: deal one card to the player. Check to see if the value is < 21.
    # If over 21, print BUST! if <= 21, ask if player wants to Hit
    hit_or_stay(new_deck,player1_hand,player_one)

    # When player's hand is <= 21 and they stay - Check dealer's value. if dealer < 17, dealer hits. If dealer >= 17 dealer stays.
    # If dealer > 21, dealer busts and player wins!
    dealer_play(new_deck,dealer_hand,player1_hand)

    # Compare dealer value to player value. If player > dealer, player wins and doubles bet. If player < dealer, house wins and player looses bet.
    winner = winner_check(player_one,player1_hand,dealer_hand)
    payout(winner,player_one,bet)

    # Ask if player would like to play again.
    game_on = play_again()

print("Thanks for playing!")
