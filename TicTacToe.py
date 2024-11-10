from tkinter import * 

def winner():
    pass

def back_button(): #A back button function that goes in every screen to return to main menu
    back_button = Button(root, text="Back to Main Menu", command=open_main_menu)
    back_button.pack(padx=0, pady=20)

def easy_mode(): #Build the easy ai here
    pass
def medium_mode(): #Build medium ai here
    pass
def hard_mode(): #Build Hard ai here
    pass

def open_settings(): #do settings here (we will make alot of variables global here so they work outside the function)
    pass


def open_PvP_screen(): #this is the player vs player part
    
    for widget in root.winfo_children(): #put this at the start of every new screen so it deletes the old screen btw if your making a new screen
        widget.destroy()
    
    play1Name = Entry(root,textvariable="i am good")
    play1Name.pack()
    
    play1ready = Button(root,text="Ready!")
    play1ready.pack()

    play2Name = Entry(root,takefocus="i am good")
    play2Name.pack()

    play2ready = Button(root, text="Ready!")
    play2ready.pack()

    label = Label(root, text="Game Screen")
    label.pack()

    back_button()

def open_PvC_screen(): #do this after finishing the player vs player
    pass

def open_main_menu(): #This is a button to return to settings 

    for widget in root.winfo_children(): #put this at the start of every new screen so it deletes the old screen btw if your making a new screen
        widget.destroy()

    img = PhotoImage(file = "Preview.png")
    labelImg = Label(root, image=img)
    labelImg.pack()
    PvP_button = Button(root, text="Player vs Player", command=open_PvP_screen)
    PvP_button.pack()

    PvC_button = Button(root, text="Player vs Computer", command=open_PvC_screen)
    PvC_button.pack()

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")


open_main_menu()

root.mainloop()