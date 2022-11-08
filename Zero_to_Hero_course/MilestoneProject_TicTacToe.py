#!/usr/bin/env python
# coding: utf-8

# # Milestone Project 1
# Congratulations on making it to your first milestone!
# You've already learned a ton and are ready to work on a real project.
# 
# ### Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
# 
# Here are the requirements:
# 
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.
# 
# ### There are 4 Jupyter Notebooks related to this assignment:
# 
# This Assignment Notebook
# A "Walkthrough Steps Workbook" Notebook
# A "Complete Walkthrough Solution" Notebook
# An "Advanced Solution" Notebook
# I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!
# 
# There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:
# 
# ## HAVE FUN!

# #### Make a function that displays the current board

# In[13]:


from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print("These are the positions you can choose:")
    print('7','|','8','|','9')
    print('---------')
    print('4','|','5','|','6')
    print('---------')
    print('1','|','2','|','3')
    
    print('\n')
    
    print("Tic Tac Toe Battlefield!: \n")
    print(' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ')
    print(' ',board[7],' ','|',' ',board[8],' ','|'' ',board[9],' ')
    print(' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ')
    print('---------------------')
    print(' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ')
    print(' ',board[4],' ','|',' ',board[5],' ','|'' ',board[6],' ')
    print(' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ')
    print('---------------------')
    print(' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ')
    print(' ',board[1],' ','|',' ',board[2],' ','|'' ',board[3],' ')
    print(' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ')
    
    


# #### Make a function where players can choose to play as 'X' or 'O'

# In[23]:


def pick_player():
    
    p1 = ''
    choice = 'Pick something else'
    
    while choice not in ['X','x','O','o']:
        
        choice = input('Player 1 choose your combat icon (X or O): ')
        
        if choice not in ['X','x','O','o']:
            print("Sorry, you need to pick either 'X' or 'O' ")
        
        else:
            p1 = choice.upper()
            
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
        
    print(" \nPlayer 1 will play as ", p1, '\nPlayer 2 will play as ', p2, ' \n ')
    
    return (p1,p2)
        


# In[3]:


import random

def player_start():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'


# In[4]:


def position_choice(players):
    open = False
    
    while not open:
        if turn == 'player1':
            choice = input('Player 1, pick an open position to place your icon: ')
            if choice in ['1','2','3','4','5','6','7','8','9']:
                if position_check(board,int(choice)):
                    open = True
                    return int(choice)
                else:
                    print("That place is taken, please select an open position.")

            else:
                print("Invalid! Pick a position between 1-9.")
        else:
            choice = input('Player 2, pick an open position to place your icon: ')
            if choice in ['1','2','3','4','5','6','7','8','9']:
                if position_check(board,int(choice)):
                    open = True
                    return int(choice)
                else:
                    print("That place is taken, please select an open position.")

            else:
                print("Invalid! Pick a position between 1-9.")
           


# In[5]:


def position_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False


# In[6]:


def place_icon(board,marker,position):
    
    board[position] = marker       
    return board
    


# In[7]:


def winner_check(board,marker):

    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
           (board[4] == marker and board[5] == marker and board[6] == marker) or
           (board[7] == marker and board[8] == marker and board[9] == marker) or
           (board[1] == marker and board[4] == marker and board[7] == marker) or
           (board[2] == marker and board[5] == marker and board[8] == marker) or
           (board[3] == marker and board[6] == marker and board[9] == marker) or
           (board[1] == marker and board[5] == marker and board[9] == marker) or
           (board[3] == marker and board[5] == marker and board[7] == marker))


# In[8]:


def full_board(board):
    return ((board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and 
             board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and 
             board[7] != ' ' and board[8] != ' ' and board[9] != ' '))
    


# In[18]:


def replay():
    keep_going = "na"
    
    while keep_going not in ('Y','y','N','n'):
        keep_going = input("Do you want to play again? (Y or N): ")

        if keep_going.lower() == 'y':
            return True
        elif keep_going.lower() == 'n':
            return False
        


# In[24]:


while True:
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    clear_output()
    # welcome message
    print("Welcome to Tic Tac Toe!")
    player1,player2 = pick_player()
    turn = player_start()

    if turn == 'player1':
        print("Player 1 will go first!")
    else:
        print("Player 2 will go first!")

    play_game = input("Are you ready to play? (Y or N)")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
                
        display_board(board)

        if turn == 'player1':

            position = position_choice(turn)

            board = place_icon(board, player1, position)
                        
            display_board(board)

            if winner_check(board,player1):
                print("Congratulations Player 1, you won!")
                game_on = False
            else:
                if full_board(board):
                    print("The game is over, no one won!")
                    break
                else:
                    turn = 'player2'

        elif turn == 'player2':
            
            position = position_choice(turn)

            board = place_icon(board, player2, position) 
                        
            display_board(board)

            if winner_check(board,player2):
                print("Congratulations Player 2, you won!")
                game_on = False
            else:
                if full_board(board):
                    print("The game is over, no one won!")
                    break
                else:
                    turn = 'player1'
    
    if not replay():
        break

       
  


# In[ ]:





# In[ ]:




