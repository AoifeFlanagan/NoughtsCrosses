from IPython.display import clear_output

# Welcome Message
def welcome():
    print("Welcome to Noughts and Crosses!")
    
# Display Board
def display_board(board):
    for row in range(3):
        print("-------------")
        print("| %s | %s | %s |" % tuple(board[3* row + c] for c in range(3)))
        
# Choose 'X' or 'O'
def player_input():  
    ask = True
    markers = ['X', 'O']
    
    global player_1
    global player_2
    
    while ask:
        player_1 = input('Player 1, would you like to be X or O? ').upper()
        
        if player_1 not in markers:
            print('Sorry, invalid choice.')
        else:
            player_2 = markers[markers.index(player_1.upper()) - 1]
            print(f'You have selected {player_1}')
            print(f"Player 2, you are {player_2}")
            ask = False
            
# Place Marker
def place_marker(board, marker, position):
    board[position -1] = marker
    
# Win Check
def win_check(board, mark):
    win_combinations = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    
    for n in win_combinations:
        if board[n[0]-1] == board[n[1]-1] == board[n[2]-1] == mark:
            return True
        
# Free Space Check
def space_check(board, position):
    return ' ' in board[position -1]

# Full Board Check (Tie)
def full_board_check(board):
    return ' ' not in board

# Player's Next Turn
def player_choice():
    ask = True
    acceptable_values = ['1','2','3','4','5','6','7','8','9','10']
    
    while ask:
        choice = input("Where would you like to go? \nPick a number between 1 (top left) and 9 (bottom right): ")
        
        if choice not in acceptable_values:
            print("Choose a number between 1 and 9!")
        else:
            break
            
    return int(choice)

# Replay
def replay():
    global board
    ask = True
    acceptable_values = ['yes', 'no']
    
    while ask:
        choice = input("Keep playing? (Yes or No) ").lower()
        
        if choice not in acceptable_values:
            clear_output()
            print("Type 'Yes' or 'No'")
        else:
            break
    
    if choice == 'yes':
        board  = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        return True
    else:
        print("Thank you for playing!")
        return False
    
# Game Logic
start_game = True
game_on = True
board  = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

while start_game:
    clear_output()
    welcome()
    player_input()
    
    while game_on:
        # Player 1 Turn
        clear_output()
        print("Player 1, your turn!")
        display_board(board)
        
        while True:
            position = player_choice()
            
            if space_check(board, position):
                place_marker(board, player_1, position)
                display_board(board)
                break
            else:
                print("You can't go there! Choose a position between 1 and 9.")
                
                
        if win_check(board, player_1):
            clear_output()
            display_board(board)
            print("Congratulations! player 1 Wins!")
            
            if replay():
                  break
            else:
                start_game = False
                break

        elif full_board_check(board):
            clear_output()
            display_board(board)            
            print("It's a tie! Game over.")

            if replay():
                  break
            else:
                start_game = False
                break

                
        # Player 2 Turn
        clear_output()
        print("Player 2, your turn!")
        display_board(board)
        
        while True:
            position = player_choice()
            
            if space_check(board, position):
                place_marker(board, player_2, position)
                display_board(board)
                break 
            else:
                print("You can't go there! Choose a position between 1 and 9.")

   
        if win_check(board, player_2):
            clear_output()
            display_board(board)            
            print("Congratulations! player 2 Wins!")
            
            if replay():
                 break
            else:
                start_game = False
                break
        
        elif full_board_check(board):
            clear_output()
            display_board(board)            
            print("It's a tie! Game over.")
        
            if replay():
                 break
            else:
                start_game = False
                break





