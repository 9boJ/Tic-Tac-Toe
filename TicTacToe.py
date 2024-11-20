from tkinter import * 
from random import *

aplz = 0

'''These are the variables for the Themes that you will need to add to the buttons'''
backGround = "white" #You change this in buttons by using bg="White"
textColour = "Black" #You change this by using fg="Black"
highLight = "Grey" #or grey idk what colour they use but you change this by using highlightbackground="gray"/"black"


def normalTheme():
    global backGround, textColour, highLight
    backGround = "white"
    textColour = "Black"
    highLight = "Black"
    root.configure(bg=backGround)  # Update main window background

def darkTheme():
    global backGround, textColour, highLight
    backGround = "black"
    textColour = "white"
    highLight = "gray"
    root.configure(bg=backGround)  # Update main window background
    
def tokyoHack_theme():
    global backGround, textColour, highLight
    backGround = "#800080"  # Example dark blue theme
    textColour = "#FFA07A"
    highLight = "#DA70D6"
    root.configure(bg=backGround)  # Update main window background

def valcanoTheme():
    global backGround, textColour, highLight
    backGround = "#550000"  # Example fiery red theme
    textColour = "#ffffff"
    highLight = "#ff4500"
    root.configure(bg=backGround)  # Update main window background

def nordTheme():
    global backGround, textColour, highLight
    backGround = "#2e3440"  # Example nordic theme
    textColour = "#d8dee9"
    highLight = "#81a1c1"
    root.configure(bg=backGround)  # Update main window background

def back_button(): 
    """A back button function that goes in every screen to return to main menu"""
    global backButton, textColour, backGround, highLight
    backButton = Button(root, text="Back to Main Menu", fg=textColour, bg=backGround, highlightbackground=highLight, command=open_main_menu)
    backButton.place(relx=0.5, rely=0.5, anchor="center")

def open_PvP_screen(): 
    """Makes a new screen when "Player vs Player" is clicked"""    
    global play1Name, play1ready, play2Name, play2ready, statusPlayer1, statusPlayer2, textColour, backGround, highLight

    # Put this at the start of every new screen so it deletes the old screen
    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()
    
    for i in range(3): # Configure 3 columns to have weight of 1
        root.grid_columnconfigure(i, weight=1)
    
    statusPlayer1 = FALSE # Status of Player 1 "Not ready"
    statusPlayer2 = FALSE # Status of Player 2 "Not ready"

    play1Name = Entry(root, fg=textColour, bg=backGround, highlightbackground=highLight) # Input box for player 1's username
    play1Name.grid(row=0, column=0, padx=10, pady=10) # Sets the box in row 0 and column 0 so all the weight for username can be in a line 
    play1Name.insert(0, "Player 1") # Example username 
    
    play1ready = Button(root, text="Ready!", command=lambda: ready("Player 1", play1Name.get()), fg=textColour, bg=backGround, highlightbackground=highLight) # When the user is ready the text in "play1Name" is passed to "ready()"
    play1ready.grid(row=0, column=1, padx=10, pady=10) # Sets the "Ready!" button in row 0 and column 1 so all the weight for username can be in a line

    play2Name = Entry(root, fg=textColour, bg=backGround, highlightbackground=highLight) # Input box for player 2's username
    play2Name.grid(row=0, column=2, padx=10, pady=10) # Sets the box in row 0 and column 2 so all the weight for username can be in a line
    play2Name.insert(0, "Player 2") # Example username

    play2ready = Button(root, text="Ready!", command=lambda: ready("Player 2", play2Name.get()), fg=textColour, bg=backGround, highlightbackground=highLight) # When the user is ready the text in "play2Name" is passed to "ready()"
    play2ready.grid(row=0, column=3, padx=10, pady=10)

    back_button()

def ready(player, userName):
    """When a user clicks a "Ready" button, check which player it is and give them a username.
       After the username is given, the "Ready" buttons and inputs are disabled.
    """
    global play1Name, play1ready, userName1, userName2, statusPlayer1, statusPlayer2, playerturn1, playerturn2, randomtrun, textColour, backGround, highLight

    if player == "Player 1":
        userName1 = userName # Sets the username for player 1  
        play1Name.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the entry 
        play1ready.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the button "Ready"
        statusPlayer1 = True # Sets the status of player 1 to ready
    elif player == "Player 2":
        userName2 = userName # Sets the username for player 2
        play2Name.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the entry
        play2ready.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the button "Ready"
        statusPlayer2 = True # Sets the status of player 2 to ready
   
    back_button() # Button that goes to the main screen

    if statusPlayer1 and statusPlayer2:
        for widget in root.winfo_children(): # Remove all the current widgets on the screen
            widget.destroy()
    
        for i in range(2):
            root.columnconfigure(i, weight=1) # Sets the window to 2 columns 

        pickPlayer = Label(root, text="Who wants to go first", fg=textColour, bg=backGround, highlightbackground=highLight) # Title that shows "Who wants to go first"
        pickPlayer.grid(row=1, column=1, columnspan=1, padx=10, pady=10) # Places the title slightly above the center
        
        # Players can pick who wants to go first or randomly
        playerturn1 = Button(root, text=userName1, command=lambda: trunXorO(userName1), fg=textColour, bg=backGround, highlightbackground=highLight) # Player 1 can go first
        playerturn1.grid(row=2, column=0, padx=10, pady=10) # Places the button to the left 

        playerturn2 = Button(root, text=userName2, command=lambda: trunXorO(userName2), fg=textColour, bg=backGround, highlightbackground=highLight) # Player 2 can go first
        playerturn2.grid(row=2, column=2, padx=10, pady=10) # Places the button to the right

        randomtrun = Button(root, text="Random", command=lambda: trunXorO("Random"), fg=textColour, bg=backGround, highlightbackground=highLight) # Random button to pick who goes first
        randomtrun.grid(row=3, column=1, padx=10, pady=10) # Places the button in the middle        

        back_button()
    
    

def trunXorO(player):
    """Shows who is "X" and "O"."""
    global playerturn1, playerturn2, randomtrun, userName1, userName2, textColour, backGround, highLight, backButton

    playerturn1.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the button
    playerturn2.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the button
    randomtrun.config(state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight) # Disables the button

    if player == "Random": # If the players want to go first randomly
        randomTrunPicker = randint(1, 100) # Picks a number from 1 to 100
        if (randomTrunPicker % 2) == 0: # If the number "randomTrunPicker" is even, player 1 will be first
            player = userName1
        else: # If the number "randomTrunPicker" is odd, player 2 will be first
            player = userName2

    titleText = Label(root, text="X or O", fg=textColour, bg=backGround, highlightbackground=highLight) # Shows "X or O"
    titleText.grid(row=4, column=1, columnspan=1, padx=10, pady=10) # Places the label in the middle

    firstplayer = Button(root, text=player, fg=textColour, bg=backGround, highlightbackground=highLight) # Shows which player is going first
    firstplayer.grid(row=5, column=1, padx=10, pady=10) # Places the button in the middle

    x = Button(root, text="X", command=lambda: PvP_Game(firstplayer.cget("text"), "X"), fg=textColour, bg=backGround, highlightbackground=highLight) # Button if the player wants to be "X"
    x.grid(row=6, column=0, padx=10, pady=10) # Places the button slightly to the left

    o = Button(root, text="O", command=lambda: PvP_Game(firstplayer.cget("text"), "O"), fg=textColour, bg=backGround, highlightbackground=highLight) # Button if the player wants to be "O"
    o.grid(row=6, column=2, padx=10, pady=10) # Places the button slightly to the right

    randomXorO = Button(root, text="Random", command=lambda: PvP_Game(firstplayer.cget("text"), "Random"), fg=textColour, bg=backGround, highlightbackground=highLight) # Button if the player wants to be "X" or "O" randomly
    randomXorO.grid(row=7, column=1, padx=10, pady=10) # Places the button in the middle

    backButton.grid(row = 8, column= 1)
def PvP_Game(player, xoro):
    """The Game Tic Tac Toe"""
    global userName1, userName2, playTurn, lst, turnsPlayed, textColour, backGround, highLight

    for widget in root.winfo_children():  # Remove all the current widgets on the screen
        widget.destroy()

    # If the player wanted to be "X" or "O" randomly
    if xoro == "Random":  # Randomly pick who is "X" and "O"
        randomTrunPicker = randint(1, 100)  # Picks a number from 1 to 100
        if (randomTrunPicker % 2) == 0:  # If the number is even, player 1 will be "X"
            xoro = "X"
        else:  # If the number is odd, player 1 will be "O"
            xoro = "O"

    player1 = player  # This is player 1

    if player1 == userName1:  # Sets who is player 1 and player 2
        player2 = userName2
    else:
        player2 = userName1

    # Sets who is "X" and "O" and who goes first
    if xoro == "X":  # Player 1 is "X" and is going first, player 2 is "O"
        player1Shap = "X"
        player2Shap = "O"
        playTurn = 1
    else:  # Player 2 is "O" and is going first, player 1 is "X"
        player1Shap = "O"
        player2Shap = "X"
        playTurn = 0

    lst = ["0", "1", "2",  # For keeping track of where "X" and "O" are placed
           "3", "4", "5",
           "6", "7", "8"]
    turnsPlayed = 0  # How many turns have been played

    root.title("TicTacToe Player VS Player")  # Add a title to the root

    for i in range(3):  # Configure rows and columns to expand with the window
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)

    # Create buttons for row 1
    a1 = Button(root, command=lambda: clicked(a1, 0), fg=textColour, bg=backGround, highlightbackground=highLight)
    b1 = Button(root, command=lambda: clicked(b1, 1), fg=textColour, bg=backGround, highlightbackground=highLight)
    c1 = Button(root, command=lambda: clicked(c1, 2), fg=textColour, bg=backGround, highlightbackground=highLight)

    buttonRowi = [a1, b1, c1]  # Holds the buttons that need to be placed
    for i in range(3):  # Place buttons in the grid with sticky directions for expansion
        buttonRowi[i].grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

    # Create buttons for row 2
    a2 = Button(root, command=lambda: clicked(a2, 3), fg=textColour, bg=backGround, highlightbackground=highLight)
    b2 = Button(root, command=lambda: clicked(b2, 4), fg=textColour, bg=backGround, highlightbackground=highLight)
    c2 = Button(root, command=lambda: clicked(c2, 5), fg=textColour, bg=backGround, highlightbackground=highLight)

    buttonRowii = [a2, b2, c2]  # Holds the buttons that need to be placed
    for i in range(3):  # Place buttons in the grid with sticky directions for expansion
        buttonRowii[i].grid(row=1, column=i, sticky="nsew", padx=5, pady=5)

    # Create buttons for row 3
    a3 = Button(root, command=lambda: clicked(a3, 6), fg=textColour, bg=backGround, highlightbackground=highLight)
    b3 = Button(root, command=lambda: clicked(b3, 7), fg=textColour, bg=backGround, highlightbackground=highLight)
    c3 = Button(root, command=lambda: clicked(c3, 8), fg=textColour, bg=backGround, highlightbackground=highLight)

    buttonRowiii = [a3, b3, c3]  # Holds the buttons that need to be placed
    for i in range(3):  # Place buttons in the grid with sticky directions for expansion
        buttonRowiii[i].grid(row=2, column=i, sticky="nsew", padx=5, pady=5)

    showPlayer1 = Button(root, text=player1, fg=textColour, bg=backGround, highlightbackground=highLight)  # Shows the name of user 1
    showPlayer1.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)  # Places the button at the bottom of row 1
    showPlayer2 = Button(root, text=player2, fg=textColour, bg=backGround, highlightbackground=highLight)  # Shows the name of user 2
    showPlayer2.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)  # Places the button at the bottom of row 3

    showPlayer1Shap = Button(root, text=player1Shap, fg=textColour, bg=backGround, highlightbackground=highLight)  # Shows "X" or "O" of user 1
    showPlayer1Shap.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)  # Places the button at the bottom of row 1
    showPlayer2Shap = Button(root, text=player2Shap, fg=textColour, bg=backGround, highlightbackground=highLight)  # Shows "X" or "O" of user 2
    showPlayer2Shap.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)  # Places the button at the bottom of row 3

    back_button()  # Button that goes to main screen
    backButton.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)  # Places the button in the middle but lower

def clicked(button, buttonId):
    """When one box is clicked, changes it to the player's turn and checks for the winner."""
    global playTurn, lst, turnsPlayed, textColour, backGround, highLight

    if playTurn == 1:  # If the current player is "X"
        button.config(text="X", state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight)
        playTurn = 0  # Change the turn
    elif playTurn == 0:  # If the current player is "O"
        button.config(text="O", state="disabled", fg=textColour, bg=backGround, highlightbackground=highLight)
        playTurn = 1  # Change the turn

    lst[buttonId] = button.cget("text")  # Keep track of where "X" and "O" are placed

    turnsPlayed += 1  # Adds one to "turnsPlayed" to keep track of the number of turns played

    xoro = ["X", "O"]  # Shapes "X" or "O"

    for i in xoro:
        """Checks for a winner"""
        if lst[0] == i and lst[1] == i and lst[2] == i:  # Check for a winner in row 1
            winer(i)
        elif lst[3] == i and lst[4] == i and lst[5] == i:  # Check for a winner in row 2
            winer(i)
        elif lst[6] == i and lst[7] == i and lst[8] == i:  # Check for a winner in row 3
            winer(i)
        elif lst[0] == i and lst[4] == i and lst[8] == i:  # Check for a winner diagonally
            winer(i)
        elif lst[6] == i and lst[4] == i and lst[2] == i:  # Check for a winner diagonally
            winer(i)
        elif lst[0] == i and lst[3] == i and lst[6] == i:  # Check for a winner in column 1
            winer(i)
        elif lst[1] == i and lst[4] == i and lst[7] == i:  # Check for a winner in column 2
            winer(i)
        elif lst[2] == i and lst[5] == i and lst[8] == i:  # Check for a winner in column 3
            winer(i)
        elif turnsPlayed == 9:  # If the board is full, declare a tie
            winer("No winners")

def winer(player):
    """When one of the players wins, congratulates the player."""
    global textColour, backGround, highLight

    for widget in root.winfo_children():  # Remove all the current widgets on the screen
        widget.destroy()

    if player == "No winners":
        textNowins = Label(root, text="No Winners", fg=textColour, bg=backGround, highlightbackground=highLight)
        textNowins.place(relx=0.5, rely=0.5, anchor="center")  # Slightly above the center

        textGoodluck = Label(root, text="Good luck next time", fg=textColour, bg=backGround, highlightbackground=highLight)
        textGoodluck.place(relx=0.5, rely=0.55, anchor="center")
    elif player == "X" or player == "O":
        winerPlayer = Label(root, text=player, fg=textColour, bg=backGround, highlightbackground=highLight)
        winerPlayer.place(relx=0.5, rely=0.45, anchor="center")  # Slightly above the center

        textIs = Label(root, text="Is", fg=textColour, bg=backGround, highlightbackground=highLight)
        textIs.place(relx=0.5, rely=0.5, anchor="center")  # Centered vertically

        textWinner = Label(root, text="Winner", fg=textColour, bg=backGround, highlightbackground=highLight)
        textWinner.place(relx=0.5, rely=0.55, anchor="center")  # Slightly below the center

        congratsText = Label(root, text="Congratulations!", fg=textColour, bg=backGround, highlightbackground=highLight)
        congratsText.place(relx=0.5, rely=0.6, anchor="center")

    back_button()  # Button that goes to the main screen
    backButton.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)  # Places the button in the middle but lower


"                 Player vs Computer starts here                "  
board = [" " for _ in range(9)]  # Just a for loop to build the buttons for the game board
buttons = []  # This is to update the button text and to also disable them afterward
current_turn = "Player"  # Tracks whose turn it is
difficulty = None  # This is just a global variable that is used to set the difficulty
turnLabel = None  # This is also a global variable just to display whose turn it is

def reset_game_state():  # This is for resetting the game
    global board, buttons, current_turn, difficulty, turnLabel
    board = [" " for _ in range(9)]  # Resetting the board to its initial state
    buttons = []  # When resetting the board, we also reset our buttons
    current_turn = "Player"  # Reset the current player's turn to whoever is playing
    difficulty = None  # Reset the difficulty to nothing; automatically changes to the chosen difficulty
    turnLabel = None  # Same thing as the difficulty

def check_winner(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # These are row win conditions
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # These are column win conditions
        [0, 4, 8], [2, 4, 6]              # These are the diagonal win conditions
    ]
    for condition in win_conditions: 
        if all(board[i] == symbol for i in condition):  # Check if all spaces in a win condition contain the same symbol
            return True
    return False

def is_full():  # Check if there are any empty spaces left
    return " " not in board  # If it returns True, no win conditions were met, and the result is a tie

def find_best_move(symbol):  # Logic for hard mode of the computer
    for i in range(9):
        if board[i] == " ":  # Test empty spaces
            board[i] = symbol
            if check_winner(symbol):  # If the resulting move leads to a win condition, return that spot
                board[i] = " "
                return i
            board[i] = " "  # Undo move and check the opponent's potential winning move
    return None 

def update_turnLabel():  # Update the text showing whose turn it is
    turnLabel.config(text=f"{current_turn}'s Turn", bg=backGround, fg=textColour, highlightbackground=highLight)

def player_move(index): 
    global current_turn
    if board[index] == " " and current_turn == "Player":  # Ensure the chosen button is empty and it's the player's turn
        board[index] = "X"  # Place "X" on the board
        buttons[index].config(text="X", state="disabled", bg=backGround, fg=textColour, highlightbackground=highLight)

        if check_winner("X"):  # Check if the move results in a win
            end_game("Player wins!")
        elif is_full():
            end_game("It's a tie!")  # If the board is full, it's a tie
        else:  # Switch to the computer's turn
            current_turn = "Computer"
            update_turnLabel()
            root.after(500, easyMode if difficulty == "Easy" else hardMode)

def easyMode():  # Logic for the computer's easy mode
    global current_turn
    if current_turn == "Computer":  # Ensure the function only runs during the computer's turn
        available_moves = [i for i in range(len(board)) if board[i] == " "]  # Find available moves
        move = choice(available_moves)  # Pick a random move

        board[move] = "O"  # Place "O" on the board
        buttons[move].config(text="O", state="disabled", bg=backGround, fg=textColour, highlightbackground=highLight)

        if check_winner("O"):  # Check if the move results in a win
            end_game("Computer wins!")
        elif is_full():
            end_game("It's a tie!")
        else:  # Switch back to the player's turn
            current_turn = "Player"
            update_turnLabel()

def hardMode():  # Logic for the computer's hard mode
    global current_turn
    if current_turn == "Computer":  # Ensure the function only runs during the computer's turn
        move = find_best_move("O")  # Look for the best move for "O"

        if move is None:  # If no winning move, block the player's winning move
            move = find_best_move("X")
        
        if move is None:  # If neither is possible, pick a random move
            available_moves = [i for i in range(len(board)) if board[i] == " "]
            move = choice(available_moves)
        
        board[move] = "O"  # Place "O" on the board
        buttons[move].config(text="O", state="disabled", bg=backGround, fg=textColour, highlightbackground=highLight)

        if check_winner("O"):  # Check if the move results in a win
            end_game("Computer wins!")
        elif is_full():
            end_game("It's a tie!")
        else:  # Switch back to the player's turn
            current_turn = "Player"
            update_turnLabel()

def end_game(result_text):
    for button in buttons:
        button.config(state="disabled")  # First, it will disable all the buttons
    turnLabel.config(text=result_text, bg=backGround, fg=textColour, highlightbackground=highLight)  # Update the label with the result

    button_frame = Frame(root, bg=backGround, highlightbackground=highLight)  # Create a new frame for the buttons
    button_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
    
    play_again_button = Button(button_frame, text="Play Again", command=reset_board, bg=backGround, fg=textColour, highlightbackground=highLight)
    play_again_button.grid(row=0, column=0, sticky="nsew")

    main_menu_button = Button(button_frame, text="Main Menu", command=open_main_menu, bg=backGround, fg=textColour, highlightbackground=highLight)
    main_menu_button.grid(row=0, column=1, sticky="nsew")

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

def reset_board():
    global board, current_turn
    board = [" " for _ in range(9)]  # Resets the board
    current_turn = "Player"  # Resets turn to the player
    for button in buttons:
        button.config(text=" ", state="normal", bg=backGround, fg=textColour, highlightbackground=highLight)
    update_turnLabel()  # Resets the turn label

def start_pvc_game(selected_difficulty, first_turn):
    global difficulty, current_turn
    difficulty = selected_difficulty  # Set difficulty
    current_turn = first_turn  # Set first turn
    open_game_board()

    if current_turn == "Computer":
        root.after(500, easyMode if difficulty == "Easy" else hardMode)

def open_game_board():
    for widget in root.winfo_children():
        widget.destroy()
    
    global buttons, turnLabel
    buttons = []  # Reset buttons list

    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    for i in range(9):  # Create game board buttons
        button = Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                        command=lambda i=i: player_move(i), bg=backGround, fg=textColour, highlightbackground=highLight)
        button.grid(row=i // 3, column=i % 3, sticky="nsew")
        buttons.append(button)
    
    turnLabel = Label(root, text="", font=("Arial", 14), bg=backGround, fg=textColour, highlightbackground=highLight)
    turnLabel.grid(row=3, column=0, columnspan=3)
    update_turnLabel()

def choose_first_turn():
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Who will go first?", font=("Arial", 18), bg=backGround, fg=textColour).pack(pady=20)

    Button(root, text="Player First", font=("Arial", 12), command=lambda: start_pvc_game(difficulty, "Player"),
           bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=10)
    Button(root, text="Computer First", font=("Arial", 12), command=lambda: start_pvc_game(difficulty, "Computer"),
           bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=10)

    Button(root, text="Back to Difficulty Selection", font=("Arial", 10), command=open_PvC_screen,
           bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=20)

def open_PvC_screen():
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Please pick Difficulty", font=("Arial", 18), bg=backGround, fg=textColour).pack(pady=10)

    Button(root, text="Easy Mode", font=("Arial", 12), command=lambda: set_difficulty_and_choose_turn("Easy"),
           bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=5)
    Button(root, text="Hard Mode", font=("Arial", 12), command=lambda: set_difficulty_and_choose_turn("Hard"),
           bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=5)

    Button(root, text="Return to Main Menu", font=("Arial", 10), command=open_main_menu,
           bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=20)

def set_difficulty_and_choose_turn(selected_difficulty):
    global difficulty
    difficulty = selected_difficulty  # Set difficulty
    choose_first_turn()

def open_settings():
    """Settings menu to adjust window size and themes."""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Settings", font=("Arial", 18), bg=backGround, fg=textColour).pack(pady=10)

    # Section for changing window size
    Label(root, text="Change Window Size", font=("Arial", 14), bg=backGround, fg=textColour).pack(pady=5)
    size_frame = Frame(root, bg=backGround)  # Ensure frame blends with background
    size_frame.pack(pady=10)

    Label(size_frame, text="Width:", font=("Arial", 12), bg=backGround, fg=textColour).grid(row=0, column=0, padx=5, pady=5)
    width_entry = Entry(size_frame, width=10, bg=backGround, fg=textColour, highlightbackground=highLight)
    width_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(size_frame, text="Height:", font=("Arial", 12), bg=backGround, fg=textColour).grid(row=1, column=0, padx=5, pady=5)
    height_entry = Entry(size_frame, width=10, bg=backGround, fg=textColour, highlightbackground=highLight)
    height_entry.grid(row=1, column=1, padx=5, pady=5)

    def apply_window_size():
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            root.geometry(f"{width}x{height}")
        except ValueError:
            Label(root, text="Invalid size! Please enter numbers only.", font=("Arial", 10),
                  fg="red", bg=backGround).pack(pady=5)

    Button(size_frame, text="Apply", command=apply_window_size, bg=backGround, fg=textColour, highlightbackground=highLight).grid(row=2, column=0, columnspan=2, pady=5)

    # Section for changing themes
    Label(root, text="Select Theme", font=("Arial", 14), bg=backGround, fg=textColour).pack(pady=5)

    theme_frame = Frame(root, bg=backGround)  # Ensure frame blends with background
    theme_frame.pack(pady=10)

    Button(theme_frame, text="Normal Theme", command=lambda: apply_theme(normalTheme), bg=backGround, fg=textColour, highlightbackground=highLight).grid(row=0, column=0, padx=5, pady=5)
    Button(theme_frame, text="Dark Theme", command=lambda: apply_theme(darkTheme), bg=backGround, fg=textColour, highlightbackground=highLight).grid(row=0, column=1, padx=5, pady=5)
    Button(theme_frame, text="Tokyo Hack Theme", command=lambda: apply_theme(tokyoHack_theme), bg=backGround, fg=textColour, highlightbackground=highLight).grid(row=1, column=0, padx=5, pady=5)
    Button(theme_frame, text="Volcano Theme", command=lambda: apply_theme(valcanoTheme), bg=backGround, fg=textColour, highlightbackground=highLight).grid(row=1, column=1, padx=5, pady=5)
    Button(theme_frame, text="Nord Theme", command=lambda: apply_theme(nordTheme), bg=backGround, fg=textColour, highlightbackground=highLight).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Back button to return to the main menu
    Button(root, text="Back to Main Menu", command=open_main_menu, bg=backGround, fg=textColour, highlightbackground=highLight).pack(pady=20)

def apply_theme(theme_function):
    """Apply a theme and refresh the current screen to update colors."""
    theme_function()  # Update theme colors
    open_settings()  # Refresh the settings screen

def open_main_menu():
    for widget in root.winfo_children():
        widget.destroy()
    
    for i in range(3):
        root.grid_columnconfigure(i, weight=0)
        root.grid_rowconfigure(i, weight=0)

    reset_game_state()

    title_screen = Label(root, text="TIC TAC TOE", height=5, font=("Arial", 18),
                         bg=backGround, fg=textColour, highlightbackground=highLight)
    title_screen.pack(fill="both", expand=True)

    buttonFrame = Frame(root, bg=backGround, highlightbackground=highLight)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=1)
    buttonFrame.columnconfigure(2, weight=1)

    PvP_button = Button(buttonFrame, text="Player vs Player", command=open_PvP_screen,
                        bg=backGround, fg=textColour, highlightbackground=highLight)
    PvP_button.grid(row=0, column=1, sticky="NESW")
    divider1 = Label(buttonFrame, bg=backGround)
    divider1.grid(row=1, column=1, sticky="NESW")
    PvC_button = Button(buttonFrame, text="Player vs Computer", command=open_PvC_screen,
                        bg=backGround, fg=textColour, highlightbackground=highLight)
    PvC_button.grid(row=2, column=1, sticky="NESW")
    divider2 = Label(buttonFrame, bg=backGround)
    divider2.grid(row=3, column=1, sticky="NESW")
    settingsBtn = Button(buttonFrame, text="Settings", command=open_settings,
                         bg=backGround, fg=textColour, highlightbackground=highLight)
    settingsBtn.grid(row=4, column=1, sticky="NESW")

    buttonFrame.pack(expand=True, fill="both")

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
# root.iconbitmap("laggames/logo.png")

open_main_menu()

root.mainloop()
