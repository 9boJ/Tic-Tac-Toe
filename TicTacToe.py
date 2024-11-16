from tkinter import * 
from random import *

'''These are the variables for the Themes that you will need to add to the buttons'''
backGround = "white" #You change this in buttons by using bg="White"
textColour = "Black" #You change this by using fg="Black"
highLight = "Black" #or grey idk what colour they use but you change this by using highlightbackground="gray"/"black"

def back_button(): 
    """A back button function that goes in every screen to return to main menu"""
    global backButton, textColour
    backButton = Button(root, text="Back to Main Menu", fg = textColour, command=open_main_menu)
    backButton.place(relx=0.5, rely=0.5, anchor="center")

def open_PvP_screen(): 
    """Makes a new screen when "Player vs Player" is cliked"""    
    global play1Name, play1ready, play2Name, play2ready, statusPlayer1, statusPlayer2, textColour

    #put this at the start of every new screen so it deletes the old screen btw if your making a new screen
    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()
    
    for i in range(3): # Configure 3 columns to have weight of 1
        root.grid_columnconfigure(i, weight=1)
    
    statusPlayer1 = FALSE # Status of Player 1 "Not ready"
    statusPlayer2 = FALSE # Status of Player 2 "Not ready"

    play1Name = Entry(root, fg = textColour) # Input box for player 1's username
    play1Name.grid(row=0, column=0, padx=10, pady=10) # sets the box in row 0 and column 0 so all the wight for user name can be in a line 
    play1Name.insert(0,"Player 1") # Example username 
    
    play1ready = Button(root,text="Ready!", command= lambda: ready("Player 1",play1Name.get()), fg = textColour) # When the user is ready the text in "play1Name" is pass to "reday()"
    play1ready.grid(row=0, column=1, padx=10, pady=10) # sets the "Ready !" button in row 0 and column 1 so all the wight for user name can be in a line

    play2Name = Entry(root, fg = textColour) # Input box for player 2's username
    play2Name.grid(row=0, column=2, padx=10, pady=10) # sets the box in row 0 and column 2 so all the wight for user name can be in a line
    play2Name.insert(0,"Player 2")# Example username

    play2ready = Button(root, text="Ready!", command= lambda: ready("Player 2",play2Name.get()), fg = textColour) # When the user is ready the text in "play2Name" is pass to "reday()"
    play2ready.grid(row=0, column=3, padx=10, pady=10)

    back_button()

def ready(player,userName):
    """When a user clicks a "Ready" button, check which play is it and give thme a user name. After the username is given them the "Ready" 
        buttons and inputs are disabled.
    """
    global play1Name, play1ready, userName1, userName2, statusPlayer1, statusPlayer2, playerturn1, playerturn2, randomtrun, textColour
    
    if player == "Player 1":
        userName1 = userName # Sets the user name for player 1  
        play1Name.config(state="disabled") # Disables the entry 
        play1ready.config(state="disabled") # Disables the button "Ready"
        statusPlayer1 = True # Sets the staus of play 1 to ready
    elif player == "Player 2":
        userName2 = userName # Sets the user name for player 2
        play2Name.config(state="disabled") # Disables the entry
        play2ready.config(state="disabled") # Disables the button "Ready"
        statusPlayer2 = True # Sets the staus of play 2 to ready
    
    if statusPlayer1 and statusPlayer2:
        for widget in root.winfo_children(): # Remove all the current widgets on the screen
            widget.destroy()
    
        for i in range(2):
            root.columnconfigure(i,weight=1) # Sets the window to 2 columns 

        pickPlayer = Label(root, text = "Who wants to go first", fg = textColour) # Title that shows "Who wnates to go first"
        pickPlayer.grid(row=1, column=1, columnspan=1, padx=10, pady=10) # places the title in midly to the top
        
        # Player can picke who wnates to first or randomly
        playerturn1 = Button(root,text=userName1, command=lambda: trunXorO(userName1), fg = textColour) # Player 1 can go first
        playerturn1.grid(row=2, column=0, padx=10, pady=10) # places the button to the right 

        playerturn2 = Button(root,text=userName2, command=lambda: trunXorO(userName2), fg = textColour) # Player 1 can go first
        playerturn2.grid(row=2, column=2, padx=10, pady=10) # places the button to the left

        randomtrun = Button(root,text="Random",command=lambda: trunXorO("Random"), fg = textColour) # who  go first can be random
        randomtrun.grid(row=3, column=1, padx=10, pady=10) # places the button in the midly

    back_button() # button that goes to main screen

def trunXorO(player):
    """ Showes whos is "X" and "O" """
    global playerturn1, playerturn2, randomtrun, userName1, userName2

    playerturn1.config(state="disabled") # Disables the button
    playerturn2.config(state="disabled") # Disables the button
    randomtrun.config(state="disabled") # Disables the button

    # If the players wnats to go first randomly
    if player == "Random":
        randomTrunPicker = randint(1,100) # Picks a number from 1 to 100
        if (randomTrunPicker % 2) == 0: # If the number "randomTrunPicker" is ever player 1 will be first
            player = userName1
        else: # If the number "randomTrunPicker" is odd player 2 will be first
            player = userName2

    backButton.grid(row=8, column=1, padx=10, pady=10) # Places the button in the midly but lower

    titleText = Label(root, text = "X or O") # Showes "X or O"
    titleText.grid(row=4, column=1, columnspan=1, padx=10, pady=10)# Places the label in the midly

    firstplayer = Button(root,text=player)  # Shows whice player is going firts 
    firstplayer.grid(row=5, column=1, padx=10, pady=10) # Places the button in the midly

    x = Button(root,text="X", command=lambda: PvP_Game(firstplayer.cget("text"),"X")) # Button if the player wants to be "X"
    x.grid(row=6, column=0, padx=10, pady=10) # Places the button in the midly but to the right

    o = Button(root,text="o", command=lambda: PvP_Game(firstplayer.cget("text"),"O")) # Button if the player wants to be "O"
    o.grid(row=6, column=2, padx=10, pady=10, ) # Places the button in the midly but to the left

    randomXorO = Button(root,text="Random",command=lambda: PvP_Game(firstplayer.cget("text"),"Random")) # Button if the player wants to be "X" or "O" randomly
    randomXorO.grid(row=7, column=1, padx=10, pady=10) # Places the button in the midly

def PvP_Game(player,xoro):
    """ The Game Tic Tac Toe """
    global userName1, userName2, playTurn, lst, turnsPlayed, textColour

    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()

    # If the player wnated to be "X" or "O" randomly
    if xoro == "Random": # randomly picke who is "X" and "O"
        randomTrunPicker = randint(1,100) # Picks a number from 1 to 100
        if (randomTrunPicker % 2) == 0: # If the number "randomTrunPicker" is ever player 1 will be "X"
            xoro = "X"
        else: # If the number "randomTrunPicker" is odd player 1 will be "O"
            xoro = "O"
    
    player1 = player # This is player 1 
    
    if player1 ==  userName1: # Sets who is player 1 And player 2
        player2 = userName2
    else:
        player2 = userName1
    
    #Sets who is "X" and "O" and who goes first 
    if xoro == "X": # Player 1 is "X" and is going first, player 2 is "O"
        player1Shap = "X"
        player2Shap = "O"
        playTurn = 1
    else:  # Player 2 is "O" and is going first, player 1 is "X"
        player1Shap = "O" 
        player2Shap = "X"
        playTurn = 0
        
    lst = ["0","1","2", # For keep track where "X" and "O" are placed
       "3","4","5",
       "6","7","8"]
    turnsPlayed = 0 # How many truns have been played

    root.title("TicTacToe Player VS Player") # Add a title to the root "TicTacToe Player VS Player"

    for i in range(3): # Configure rows and columns to expand with the window
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)
    
    # Create buttons for row 1
    a1 = Button(root, command=lambda: clicked(a1,0), fg = textColour)
    b1 = Button(root, command=lambda: clicked(b1,1), fg = textColour)
    c1 = Button(root, command=lambda: clicked(c1,2), fg = textColour)

    buttonRowi= [a1,b1,c1] # Holdes the buttons that need to be placed 
    for i in range(3): # Place buttons in the grid with sticky directions for expansion
        buttonRowi[i].grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

    # Create buttons for row 2 
    a2 = Button(root, command=lambda: clicked(a2,3), fg = textColour)
    b2 = Button(root, command=lambda: clicked(b2,4), fg = textColour)
    c2 = Button(root, command=lambda: clicked(c2,5), fg = textColour)

    buttonRowii= [a2,b2,c2] # Holdes the buttons that need to be placed 
    for i in range(3): # Place buttons in the grid with sticky directions for expansion
        buttonRowii[i].grid(row=1, column=i, sticky="nsew", padx=5, pady=5)

    # Create buttons for row 3
    a3 = Button(root, command=lambda: clicked(a3,6), fg = textColour)
    b3 = Button(root, command=lambda: clicked(b3,7), fg = textColour)
    c3 = Button(root, command=lambda: clicked(c3,8), fg = textColour)

    buttonRowiii= [a3,b3,c3] # Holdes the buttons that need to be placed 
    for i in range(3): # Place buttons in the grid with sticky directions for expansion
        buttonRowiii[i].grid(row=2, column=i, sticky="nsew", padx=5, pady=5)
    
    showPlayer1 = Button(root, text=player1, fg = textColour) # Shows the play name of user 1
    showPlayer1.grid(row=4, column=0, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 1
    showPlayer2 = Button(root, text=player2, fg = textColour) # Shows the play name of user 2
    showPlayer2.grid(row=4, column=2, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 3

    showPlayer1Shap = Button(root, text=player1Shap, fg = textColour) # Shows the play is "X" or "O" of user 1
    showPlayer1Shap.grid(row=5, column=0, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 1
    showPlayer2Shap = Button(root, text=player2Shap, fg = textColour) # Shows the play is "X" or "O" of user 2
    showPlayer2Shap.grid(row=5, column=2, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 1
    
    back_button() # Button that goes to main screen
    backButton.grid(row=5, column=1, sticky="nsew", padx=5, pady=5) # Places the button in the midly but lower
    backButton.config(fg = textColour)

def clicked(button,buttonId):
    """When one of box is cliked chagnes it the player turn and check for winer"""
    global playTurn, lst, turnsPlayed, textColour
    
    if playTurn == 1: # If the first paly is "X" it plces a "X" where the player cliked and disabled that box
        button.config(text="X", state = "disabled")
        playTurn = 0 # Chagnes the turn
    elif playTurn == 0: # If the first paly is "X" it plces a "O" where the player cliked and disabled that box
        button.config(text="O", state = "disabled")
        playTurn = 1 # Chagnes the turn
    
    lst[buttonId] = button.cget("text") # Keep the track of where the "X" and "O" are plcesd

    turnsPlayed = turnsPlayed + 1 # Adds one "turnsPlayed" to keep trck of many turn have been played
    
    xoro = ["X","O"] # Shapes "X" or "O"
    
    for i in xoro: 
        """Checks for winer"""
        if lst[0] == i and lst[1] == i and lst[2] == i: # Check for winer in row 1 
            if i == "X":
                winer("X") 
            elif i == "O":
                winer("O")
        elif lst[3] == i and lst[4] == i and lst[5] == i: # Check for winer in row 2
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif lst[6] == i and lst[7] == i and lst[8] == i: # Check for winer in row 3
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif lst[0] == i and lst[4] == i and lst[8] == i: # Check for winer diagonal
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif lst[6] == i and lst[4] == i and lst[2] == i: # Check for winer diagonal
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif lst[0] == i and lst[3] == i and lst[6] == i: # Check for winer in column 1 
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif lst[1] == i and lst[4] == i and lst[7] == i: # Check for winer in column 2
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif lst[2] == i and lst[5] == i and lst[8] == i: # Check for winer in column 3
            if i == "X":
                winer("X")
            elif i == "O":
                winer("O")
        elif turnsPlayed == 9:
            winer("No winers")

def winer(player):
    """ When one of the players wins it will Congratulate the player """

    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()

    if player == "No winers":
        
        textNowins = Label(root, text="No Winners", fg = textColour)
        textNowins.place(relx=0.5, rely=0.5, anchor="center")  # Slightly above the center

        textGoogluck = Label(root, text="Good luck next time", fg = textColour)
        textGoogluck.place(relx=0.5, rely=0.55, anchor="center")
    elif player == "X" or player == "O":

        winerPlayer = Label(root, text=player, fg = textColour)
        winerPlayer.place(relx=0.5, rely=0.45, anchor="center")  # Slightly above the center

        textIs = Label(root, text="Is", fg = textColour)
        textIs.place(relx=0.5, rely=0.5, anchor="center")  # Centered vertically

        textWiner = Label(root, text="Winner", fg = textColour)
        textWiner.place(relx=0.5, rely=0.55, anchor="center")  # Slightly below the center

        congrauText = Label(root, text="Congratulations!", fg = textColour)
        congrauText.place(relx=0.5, rely=0.6, anchor="center")

    back_button() # Button that goes to main screen
    backButton.grid(row=5, column=1, sticky="nsew", padx=5, pady=5) # Places the button in the midly but lower
"                 Player vs Computer starts here                "  

board = [" " for _ in range(9)] #just a for loop to build the buttons for the game board
buttons = [] #this is to update the button text and to also disable them afterwards
current_turn = "Player" #Tracks whos turn it is
difficulty = None #This is just a global variable that is used to set the difficulty 
turnLabel = None #This is also a global variable just to display who's turn it is

def reset_game_state(): #This is for reseting the game
    global board, buttons, current_turn, difficulty, turnLabel
    board = [" " for _ in range(9)] #reseting the board to it initial state
    buttons = [] #when reseting the board we also have to reset our buttons
    current_turn = "Player" #reset the current players turn to who ever is playing
    difficulty = None #have to reset the difficulty to nothing but automatically changes to whatever was chosen depending on what the player picked
    turnLabel = None #Same thing as the difficulty

def check_winner(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #These are row win conditions 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #These are coloumn win conditions 
        [0, 4, 8], [2, 4, 6]             #These are the diagonal win conditions
    ]
    for condition in win_conditions: 
        if all(board[i] == symbol for i in condition): #This function is to just go through the win conditions to see if the win confidition contains all the same Character like X or O
            return True
    return False

def is_full(): #This function just checks if there are any empty spaces left
    return " " not in board #If it returns True that means no win conditions were met and the result is a tie

def find_best_move(symbol): #This function was made for the Hard mode of the Computer and takes both parameters "X" and "O"
    for i in range(9):
        if board[i] == " ": #the Computer iterates through the board and tests out the empty spaces
            board[i] = symbol
            if check_winner(symbol): #if the resulting space may lead to a win condition it will take that spot for O
                board[i] = " " 
                return i
            board[i] = " " #if the move doesn't result to a win condition it undoes its move then checks the win conditions to "X" to try to block it by switching the symbol parameter to "X"
    return None 

def update_turnLabel(): #This function is to just update the Text showing who's turn it is
    turnLabel.config(text=f"{current_turn}'s Turn")

def player_move(index): 
    global current_turn
    if board[index] == " " and current_turn == "Player": #First we check if the chosen button is empty and also checks to see if it is the players turn
        board[index] = "X" #If both requirements are met then it places X on that spot 
        buttons[index].config(text="X", state="disabled") #Then we disable the button

        if check_winner("X"): #This is to check if the resulting move is a win for the player
            end_game("Player wins!") 
        elif is_full():
            end_game("It's a tie!") #If the resulting move leads to a full board its just a tie
        else: #If the resulting move did none of those that means there is still stuff that can happen in the game and it switches to the computers turn
            current_turn = "Computer"
            update_turnLabel()
            root.after(500, easyMode if difficulty == "Easy" else hardMode)

def easyMode(): #This is the logic behind the computers easy mode
    global current_turn
    if current_turn == "Computer": #It starts by that easy mode only runs when its the computers turn
        available_moves = []
        for i in range(len(board)): #the computer loops through the board to check for empty spaces
            if board[i] == " ":
                available_moves.append(i)
        move = choice(available_moves) #It will then pick a random spot from those available spots using the choice function from the import random module 
        board[move] = "O"
        buttons[move].config(text="O", state="disabled") #Disables the button once its been used

        if check_winner("O"):  #Same as the player move function we have to check if the computers move results to any of these
            end_game("Computer wins!")
        elif is_full():
            end_game("It's a tie!")
        else:
            current_turn = "Player"
            update_turnLabel()

def hardMode(): #This is the logic behind the hard mode of the computer which trys to go for the win and can also block off the player from winning
    global current_turn
    if current_turn == "Computer": #Also ensures that this function only works when its the computers turn  
        move = find_best_move("O") #This goes back to the find best move function 

        if move is None: #When it can't find a winning move now it checks for X's wining move
            move = find_best_move("X")
        
        if move is None: #if niether is doable it'll just place randomly, it is only possible to beat the computer by forcing it to play a random move
            available_moves = []
            for i in range(len(board)): 
                if board[i] == " ":
                    available_moves.append(i)
            move = choice(available_moves)
        
        board[move] = "O" #This is just the computer making its move
        buttons[move].config(text="O", state="disabled") #disables the button afterwards

        if check_winner("O"): #Same as The player move function we need to check if that move meets any win condition or leads to a tie
            end_game("Computer wins!")
        elif is_full():
            end_game("It's a tie!")
        else:
            current_turn = "Player"
            update_turnLabel()

def end_game(result_text):
    for button in buttons:
        button.config(state="disabled") #First it will disable all the buttons
    turnLabel.config(text=result_text) #Then it will change the Label to show who won/if its a tie

    button_frame = Frame(root) #Now it creates a new frame so we can add new buttons
    button_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
    
    play_again_button = Button(button_frame, text="Play Again", command=reset_board) #Adds a play again button
    play_again_button.grid(row=0, column=0, sticky="nsew")

    main_menu_button = Button(button_frame, text="Main Menu", command=open_main_menu) #Adds a return to main menu button if you feel like your done with the game
    main_menu_button.grid(row=0, column=1, sticky="nsew")

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

def reset_board(): 
    global board, current_turn
    board = [" " for _ in range(9)] #resets the boards button to be empty
    current_turn = "Player" #and it resets to who ever started the game first
    for button in buttons:
        button.config(text=" ", state="normal") #Enables them
    update_turnLabel() #and also resets the turn label

def start_pvc_game(selected_difficulty, first_turn):
    global difficulty, current_turn
    difficulty = selected_difficulty #This just determines what difficulty was picked 
    current_turn = first_turn #This is also just to determine who goes first
    open_game_board()

    if current_turn == "Computer": 
        root.after(500, easyMode if difficulty == "Easy" else hardMode)
        #If it was the computers turn first there would be a delay of 500 miliseconds before it starts due to a bug where sometimes the computer would just not play at all and the you would be stuck there

def open_game_board(): #This is just the UI of the playing board
    for widget in root.winfo_children():
        widget.destroy()
    
    global buttons, turnLabel
    buttons = [] #Restores the buttons list to be empty incase it wasn't already 

    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    for i in range(9): #This is the playing board itsself
        button = Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                        command=lambda i=i: player_move(i), fg = textColour) 
        button.grid(row=i // 3, column=i % 3, sticky="nsew")
        buttons.append(button)
    
    turnLabel = Label(root, text="", font=("Arial", 14)) #This is just to show where the turn Label will be displayed
    turnLabel.grid(row=3, column=0, columnspan=3)
    update_turnLabel()

def choose_first_turn():
    global textColour
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Who will go first?", font=("Arial", 18), fg = textColour).pack(pady=20) #Just a text 

    Button(root, text="Player First", font=("Arial", 12), command=lambda: start_pvc_game(difficulty, "Player"), fg = textColour).pack(pady=10) #When either one of these buttons are clicked the start_pvc_game function is called with the difficulty you have chosen from the previous screen
    Button(root, text="Computer First", font=("Arial", 12), command=lambda: start_pvc_game(difficulty, "Computer"), fg = textColour).pack(pady=10)

    Button(root, text="Back to Difficulty Selection", font=("Arial", 10), command=open_PvC_screen, fg = textColour).pack(pady=20) #Takes you to the previous screen

def open_PvC_screen(): #This is your initial choice between picking the easy or the hard mode, basically just a UI 
    global textColour
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Please pick Difficulty", font=("Arial", 18), fg = textColour).pack(pady=10)

    Button(root, text="Easy Mode", font=("Arial", 12), command=lambda: set_difficulty_and_choose_turn("Easy"), fg = textColour).pack(pady=5) #Calls the set difficulty function with your chosen difficulty
    Button(root, text="Hard Mode", font=("Arial", 12), command=lambda: set_difficulty_and_choose_turn("Hard"), fg = textColour).pack(pady=5)

    Button(root, text="Return to Main Menu", font=("Arial", 10), command=open_main_menu, fg = textColour).pack(pady=20)

def set_difficulty_and_choose_turn(selected_difficulty):
    global difficulty
    difficulty = selected_difficulty #This function is just used to set the difficulty 
    choose_first_turn()

def open_main_menu():
    
    global buttonFrame, textColour

    for widget in root.winfo_children():
        widget.destroy()
    
    for i in range(3):
        root.grid_columnconfigure(i, weight=0)
        root.grid_rowconfigure(i, weight=0)

    reset_game_state()

    root.title("Tic Tac Toe") # Sets the title of window to "Tic Tac Toe"

    title_screen = Label(root, text="TIC TAC TOE", height=5, font=("arial", 18), fg = textColour)
    title_screen.pack(fill="both", expand=True)

    buttonFrame = Frame(root)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=1)
    buttonFrame.columnconfigure(2, weight=1)

    PvP_button = Button(buttonFrame, text="Player vs Player", command=open_PvP_screen, fg = textColour)
    PvP_button.grid(row=0, column=1, sticky="NESW")
    divider1 = Label(buttonFrame, fg = textColour)
    divider1.grid(row=1, column=1, sticky="NESW")
    PvC_button = Button(buttonFrame, text="Player vs Computer", command=open_PvC_screen, fg = textColour)
    PvC_button.grid(row=2, column=1, sticky="NESW")
    divider2 = Label(buttonFrame, fg = textColour)
    divider2.grid(row=3, column=1, sticky="NESW")
    settingsBtn = Button(buttonFrame, text="Settings", command=open_settings, fg = textColour)
    settingsBtn.grid(row=4, column=1, sticky="NESW")

    buttonFrame.pack(expand=True, fill="both")

def open_settings(): 
    """Open an meun where play can change the size of window and colour for text, background"""
    global backButton

    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()
     
    for i in range(5): # Configure 4 columns and 2 rows to have weight of 1
        root.grid_rowconfigure(i, weight=1) 
        if i < 3:
                root.grid_columnconfigure(i, weight=1)

    textwindowsetting = Label(root, text="Window setting",font=24, fg = textColour) # Text "Window setting"
    textwindowsetting.grid(row = 0, column= 1, sticky="NESW") # The text is placed in the midly top
    
    getwinHeight = root.winfo_height() # Gets the current window height
    getwinWidth = root.winfo_width()# Gets the current window width


    setwinWidth = Entry(root, fg = textColour) # Input box for new width for window 
    setwinWidth.grid(row=1, column=0, padx=10, pady=10) # sets the box in row 1 and column 0 so all the wight for user name can be in a line 
    setwinWidth.insert(0,str(getwinWidth)) # Shows the current width of the window

    setwinHeight = Entry(root, fg = textColour) # Input box for new height for window 
    setwinHeight.grid(row=1, column=2, padx=10, pady=10) # sets the box in row 1 and column 2 so all the wight for user name can be in a line
    setwinHeight.insert(0,str(getwinHeight)) # Shows the current height of the window

    setwinSize = Button(root, text="Set Window Size", command= lambda: chagnewinSize(setwinWidth.get(),setwinHeight.get()), fg = textColour) # When the user wnats to chagne the of the window it takes The sizee in "setwinWidth" and "setwinHeight" is pass to "chagnewinSize(width,height)"
    setwinSize.grid(row=2, column=1, padx=10, pady=10, ) # sets the box in row 2 and column 1 

    changecolour = Button(root, text="Chagne Colours", command= winchangecolour, fg = textColour) # Open an meun of colour choice
    changecolour.grid(row=3, column=1, padx=10, pady=10, ) # sets the box in row 2 and column 1 
    
    back_button() # Button for going to back to main meun
    backButton.grid(row = 4, column=1) # Sets the button "backButton" on the lest row

def chagnewinSize(width,height):
    """ Tacks the width and the height givean by "open_setting", set the new window size"""
    size = str(width) + "x" + str(height) # Turns width and height into input that works for tkinter
    
    root.geometry(size) # Set new window size

def winchangecolour():
    """ A meun where player can change the colour for text and background"""
    global backButton, textColour

    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()

    colorBank = ["white", "black", "red",    "green", "blue", "cyan",    "yellow", "magenta", "gray"] # Colour choice
    
    for i in range(9): # Configure 8 columns and 8 rows to have weight of 1
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)
    
    root.title("Colour setting") # Sets the title of window to "Colour setting"

    textwinColoursetting = Label(root, text="Colour setting",font=24, fg = textColour) # sets a text "Colour setting"
    textwinColoursetting.grid(row = 1, column= 4, sticky="NESW") # sets the text "Colour setting" in the midly top

    textwinTextcolour = Label(root, text="Text colour", fg = textColour) # sets a text "Text colour"
    textwinTextcolour.grid(row = 2, column= 4, sticky="NESW") # sets the text "Text colour" in the midly and in row 2
    
    
    textWhite = Button(root, bg="white", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","white")) # Button for changing the text color to white
    textBlack = Button(root, bg="black", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","black")) # Button for changing the text color to black
    textRed = Button(root, bg="red", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","red")) # Button for changing the text color to red

    textGreen = Button(root, bg="green", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","green")) # Button for changing the text color to green
    textBlue = Button(root, bg="blue", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","blue")) # Button for changing the text color to blue
    textCyan = Button(root, bg="cyan", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","cyan")) # Button for changing the text color to cyan

    textYellow = Button(root, bg="yellow", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","yellow")) # Button for changing the text color to yellow
    textMagenta = Button(root, bg="magenta", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","magenta")) # Button for changing the text color to magenta
    textgray = Button(root, bg="gray", width=5, padx=2, pady=0, fg = textColour, command= lambda: chagneColour("text","gray")) # Button for changing the text color to gray


    textColourlist = [textWhite, textBlack, textRed, textGreen, textBlue, textCyan, textYellow, textMagenta, textgray] # List of button that are usd for chagning colour of text

    for i in range(9):
        textColourlist[i].grid(row=3, column=i) # sets the buttons in a line on row 3


    textwinBackgroundcolour = Label(root, text="Background colour", fg = textColour) # Sets a text "Background colour"
    textwinBackgroundcolour.grid(row = 4, column= 4, sticky="NESW") # Puts the text in the midly 
    
    
    bgWhite = Button(root, bg="white", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","white"), fg = textColour) # Button for changing the background color to white
    bgBlack = Button(root, bg="black", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","black"), fg = textColour) # Button for changing the background color to black
    bgRed = Button(root, bg="red", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","red"), fg = textColour) # Button for changing the background color to red

    bgGreen = Button(root, bg="green", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","green"), fg = textColour) # Button for changing the background color to green
    bgBlue = Button(root, bg="blue", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","blue"), fg = textColour) # Button for changing the background color to blue
    bgCyan = Button(root, bg="cyan", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","cyan"), fg = textColour) # Button for changing the background color to cyan

    bgYellow = Button(root, bg="yellow", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","yellow"), fg = textColour) # Button for changing the background color to yellow
    bgMagenta = Button(root, bg="magenta", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","magenta"), fg = textColour) # Button for changing the background color to magenta
    bggray = Button(root, bg="gray", width=5, padx=2, pady=0, command= lambda: chagneColour("bg","gray"), fg = textColour) # Button for changing the background color to gray

    bgColourlist = [bgWhite, bgBlack, bgRed, bgGreen, bgBlue, bgCyan, bgYellow, bgMagenta, bggray] # List of button that are usd for chagning colour of background

    for i in range(9):
        bgColourlist[i].grid(row=5, column=i) # sets the buttons in a line on row 5

    back_button() # Button for going to back to main meun
    backButton.grid(row = 6, column=4) # Sets the button "backButton" on the lest row

def chagneColour(type,colour):
    """Changes the colour given by "colour" and to the what is it beening applyed to by "type" """
    global textColour
    if type == "text":
        textColour = colour # sets the colour for text to "colour"
    elif type == "bg":
        root.config(bg=colour) # sets the colour for background to "colour"
        
root = Tk()
root.geometry("500x500")
#root.iconbitmap("laggames\logo.png")

open_main_menu()

root.mainloop()
