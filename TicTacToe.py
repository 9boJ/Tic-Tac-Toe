from tkinter import * 
from random import *

def winner():
    pass

def back_button(): 
    """A back button function that goes in every screen to return to main menu"""
    global backButton
    backButton = Button(root, text="Back to Main Menu", command=open_main_menu)
    backButton.place(relx=0.5, rely=0.5, anchor="center")


def easy_mode(): #Build the easy ai here
    pass
def medium_mode(): #Build medium ai here
    pass
def hard_mode(): #Build Hard ai here
    pass

def open_settings(): #do settings here (we will make alot of variables global here so they work outside the function)
    pass

def open_PvP_screen(): 
    """Makes a new screen when "Player vs Player" is cliked"""    
    global play1Name, play1ready, play2Name, play2ready, statusPlayer1, statusPlayer2

    #put this at the start of every new screen so it deletes the old screen btw if your making a new screen
    for widget in root.winfo_children(): # Remove all the current widgets on the screen
        widget.destroy()
    
    for i in range(3): # Configure 3 columns to have weight of 1
        root.grid_columnconfigure(i, weight=1)
    
    statusPlayer1 = FALSE # Status of Player 1 "Not ready"
    statusPlayer2 = FALSE # Status of Player 2 "Not ready"

    play1Name = Entry(root) # Input box for player 1's username
    play1Name.grid(row=0, column=0, padx=10, pady=10) # sets the box in row 0 and column 0 so all the wight for user name can be in a line 
    play1Name.insert(0,"Player 1") # Example username 
    
    play1ready = Button(root,text="Ready!", command= lambda: ready("Player 1",play1Name.get())) # When the user is ready the text in "play1Name" is pass to "reday()"
    play1ready.grid(row=0, column=1, padx=10, pady=10) # sets the "Ready !" button in row 0 and column 1 so all the wight for user name can be in a line

    play2Name = Entry(root,) # Input box for player 2's username
    play2Name.grid(row=0, column=2, padx=10, pady=10) # sets the box in row 0 and column 2 so all the wight for user name can be in a line
    play2Name.insert(0,"Player 2")# Example username

    play2ready = Button(root, text="Ready!", command= lambda: ready("Player 2",play2Name.get())) # When the user is ready the text in "play2Name" is pass to "reday()"
    play2ready.grid(row=0, column=3, padx=10, pady=10)

    back_button()

def ready(player,userName):
    """When a user clicks a "Ready" button, check which play is it and give thme a user name. After the username is given them the "Ready" 
        buttons and inputs are disabled.
    """
    global play1Name, play1ready, userName1, userName2, statusPlayer1, statusPlayer2, playerturn1, playerturn2, randomtrun
    
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

        pickPlayer = Label(root, text = "Who wants to go first") # Title that shows "Who wnates to go first"
        pickPlayer.grid(row=1, column=1, columnspan=1, padx=10, pady=10) # places the title in midly to the top
        
        # Player can picke who wnates to first or randomly
        playerturn1 = Button(root,text=userName1, command=lambda: trunXorO(userName1)) # Player 1 can go first
        playerturn1.grid(row=2, column=0, padx=10, pady=10) # places the button to the right 

        playerturn2 = Button(root,text=userName2, command=lambda: trunXorO(userName2)) # Player 1 can go first
        playerturn2.grid(row=2, column=2, padx=10, pady=10) # places the button to the left

        randomtrun = Button(root,text="Random",command=lambda: trunXorO("Random")) # who  go first can be random
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

    firstplayer = Label(root,text=f"{player} goes first")  # Shows which player is going firts 
    firstplayer.grid(row=5, column=1, padx=10, pady=10) # Places the button in the midly

    x = Button(root,text="X", command=lambda: PvP_Game(firstplayer.cget("text"),"X")) # Button if the player wants to be "X"
    x.grid(row=6, column=0, padx=10, pady=10) # Places the button in the midly but to the right

    o = Button(root,text="o", command=lambda: PvP_Game(firstplayer.cget("text"),"O")) # Button if the player wants to be "O"
    o.grid(row=6, column=2, padx=10, pady=10, ) # Places the button in the midly but to the left

    randomXorO = Button(root,text="Random",command=lambda: PvP_Game(firstplayer.cget("text"),"Random")) # Button if the player wants to be "X" or "O" randomly
    randomXorO.grid(row=7, column=1, padx=10, pady=10) # Places the button in the midly

def PvP_Game(player,xoro):
    """ The Game Tic Tac Toe """
    global userName1, userName2, playTurn, lst

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

    root.title("TicTacToe Player VS Player") # Add a title to the root "TicTacToe Player VS Player"
    root.geometry("500x500")  # Size of the window 

    for i in range(3): # Configure rows and columns to expand with the window
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)
    
    # Create buttons for row 1
    a1 = Button(root, command=lambda: clied(a1,0))
    b1 = Button(root, command=lambda: clied(b1,1))
    c1 = Button(root, command=lambda: clied(c1,2))

    buttonRowi= [a1,b1,c1] # Holdes the buttons that need to be placed 
    for i in range(3): # Place buttons in the grid with sticky directions for expansion
        buttonRowi[i].grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

    # Create buttons for row 2 
    a2 = Button(root, command=lambda: clied(a2,3))
    b2 = Button(root, command=lambda: clied(b2,4))
    c2 = Button(root, command=lambda: clied(c2,5))

    buttonRowii= [a2,b2,c2] # Holdes the buttons that need to be placed 
    for i in range(3): # Place buttons in the grid with sticky directions for expansion
        buttonRowii[i].grid(row=1, column=i, sticky="nsew", padx=5, pady=5)

    # Create buttons for row 3
    a3 = Button(root, command=lambda: clied(a3,6))
    b3 = Button(root, command=lambda: clied(b3,7))
    c3 = Button(root, command=lambda: clied(c3,8))

    buttonRowiii= [a3,b3,c3] # Holdes the buttons that need to be placed 
    for i in range(3): # Place buttons in the grid with sticky directions for expansion
        buttonRowiii[i].grid(row=2, column=i, sticky="nsew", padx=5, pady=5)
    
    showPlayer1 = Button(root, text=player1) # Shows the play name of user 1
    showPlayer1.grid(row=4, column=0, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 1
    showPlayer2 = Button(root, text=player2) # Shows the play name of user 2
    showPlayer2.grid(row=4, column=2, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 3

    showPlayer1Shap = Button(root, text=player1Shap) # Shows the play is "X" or "O" of user 1
    showPlayer1Shap.grid(row=5, column=0, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 1
    showPlayer2Shap = Button(root, text=player2Shap) # Shows the play is "X" or "O" of user 2
    showPlayer2Shap.grid(row=5, column=2, sticky="nsew", padx=5, pady=5) # Places the button at the bottom of row 1

    back_button() # Button that goes to main screen
    backButton.grid(row=5, column=1, sticky="nsew", padx=5, pady=5) # Places the button in the midly but lower

def clied(button,buttonId):
    """When one of box is cliked chagnes it the player turn and check for winer"""
    global playTurn, lst
    
    if playTurn == 1: # If the first paly is "X" it plces a "X" where the player cliked and disabled that box
        button.config(text="X", state = "disabled")
        playTurn = 0 # Chagnes the turn
    elif playTurn == 0: # If the first paly is "X" it plces a "O" where the player cliked and disabled that box
        button.config(text="O", state = "disabled")
        playTurn = 1 # Chagnes the turn
    
    lst[buttonId] = button.cget("text") # Keep the track of where the "X" and "O" are plcesd
    
    xoro = ["X","O"] # Shapes "X" or "O"
    for i in xoro: # Check for winer
        if lst[0] == i and lst[1] == i and lst[2] == i: # Check for winer in row 1 
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[3] == i and lst[4] == i and lst[5] == i: # Check for winer in row 2
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[6] == i and lst[7] == i and lst[8] == i: # Check for winer in row 3
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[0] == i and lst[4] == i and lst[8] == i: # Check for winer diagonal
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[6] == i and lst[4] == i and lst[2] == i: # Check for winer diagonal
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[0] == i and lst[3] == i and lst[6] == i: # Check for winer in column 1 
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[1] == i and lst[4] == i and lst[7] == i: # Check for winer in column 2
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

        if lst[2] == i and lst[5] == i and lst[8] == i: # Check for winer in column 3
            print("win")
            for widget in root.winfo_children(): # Remove all the current widgets on the screen
                widget.destroy()

def open_PvC_screen(): #do this after finishing the player vs player
    pass

def open_main_menu(): #This is a button to return to settings 

    for widget in root.winfo_children(): #put this at the start of every new screen so it deletes the old screen btw if your making a new screen
        widget.destroy()

    title_screen = Label(root, text="TIC TAC TOE", height=5, font=("arial", 18))
    title_screen.pack(fill="both", expand=True)

    buttonFrame = Frame(root)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=1)
    buttonFrame.columnconfigure(2, weight=1)

    PvP_button = Button(buttonFrame, text="Player vs Player", command=open_PvP_screen)
    PvP_button.grid(row=0, column=1, sticky="NESW")
    divider1 = Label(buttonFrame)
    divider1.grid(row=1, column=1, sticky="NESW")
    PvC_button = Button(buttonFrame, text="Player vs Computer", command=open_PvC_screen)
    PvC_button.grid(row=2, column=1, sticky="NESW")
    divider2 = Label(buttonFrame)
    divider2.grid(row=3, column=1, sticky="NESW")
    settingsBtn = Button(buttonFrame, text="Settings", command=open_settings)
    settingsBtn.grid(row=4, column=1, sticky="NESW")

    buttonFrame.pack(expand=True, fill="both")

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
#root.iconbitmap("laggames\logo.png")

open_main_menu()

root.mainloop()
