import tkinter as tk

def back_button(): #A back button function that goes in every screen to return to main menu
    back_button = tk.Button(root, text="Back to Main Menu", command=open_main_menu)
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

    for widget in root.winfo_children():
        widget.destroy()
    
    label = tk.Label(root, text="Game Screen")
    label.pack()

    back_button()

def open_PvC_screen():
    pass

def open_main_menu(): #This is a button to return to settings 

    for widget in root.winfo_children():
        widget.destroy()

    PvP_button = tk.Button(root, text="Player vs Player", command=open_PvP_screen)
    PvP_button.pack(pady=100)

    PvC_button = tk.Button(root, text="Player vs Computer", command=open_PvC_screen)
    PvC_button.pack(padx=0, pady=100)
    '''I am having trouble placing the button in the cords I want so I give up and will leave this for another time'''
    PvC_button.place(x=250)


root = tk.Tk()
root.geometry("600x500")
root.title("Tic Tac Toe")

open_main_menu()

root.mainloop()