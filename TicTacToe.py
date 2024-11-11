from tkinter import * 

def winner():
    pass

def back_button(): 
    """A back button function that goes in every screen to return to main menu"""
    back_button = Button(root, text="Back to Main Menu", command=open_main_menu)
    back_button.place(relx=0.5, rely=0.5, anchor="center")


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
    global play1Name, play1ready, userName1, userName2, statusPlayer1, statusPlayer2
    
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
    
        titleText = Label(root, text = "X or O")
        titleText.pack()
    
        for i in range(2):
            root.columnconfigure(i,weight=1)

        pickPlayer = Label(root, text = "Who wnates to go first ")
        pickPlayer.pack()
        
    
    back_button()

    

def open_PvC_screen(): #do this after finishing the player vs player
    pass

def open_main_menu(): #This is a button to return to settings 

    for widget in root.winfo_children(): #put this at the start of every new screen so it deletes the old screen btw if your making a new screen
        widget.destroy()

    PvP_button = Button(root, text="Player vs Player", command=open_PvP_screen)
    PvP_button.place(relx=0.5, rely=0.33, anchor="center")

    PvC_button = Button(root, text="Player vs Computer", command=open_PvC_screen)
    PvC_button.place(relx=0.5, rely=0.4, anchor="center")

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
#root.iconbitmap("laggames\logo.png")

open_main_menu()

root.mainloop()