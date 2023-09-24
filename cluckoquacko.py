#A version of Tic-Tac-Toe but with chickens and ducks!
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Cluck-Quack-O!') 

#chicken starts the game
cluck = True #chicken is clicked
count = 0

#disable buttons after game
def disablebuttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

#check winner
def checkwinner():
    global winner 
    winner = False

    #TO CHECK IF CHICKEN IS WINNING
    #if row 1 wins
    if b1["text"] == "🐔" and b2["text"] == "🐔" and b3["text"] == "🐔":
        b1.config(bg = "green")
        b2.config(bg = "green")
        b3.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()

    #if row 2 wins
    elif b4["text"] == "🐔" and b5["text"] == "🐔" and b6["text"] == "🐔":
        b4.config(bg = "green")
        b5.config(bg = "green")
        b6.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()

    #if row 3 wins
    elif b7["text"] == "🐔" and b8["text"] == "🐔" and b9["text"] == "🐔":
        b7.config(bg = "green")
        b8.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()

    #if column 1 wins
    elif b1["text"] == "🐔" and b4["text"] == "🐔" and b7["text"] == "🐔":
        b1.config(bg = "green")
        b4.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()
    
    #if column 2 wins
    elif b2["text"] == "🐔" and b5["text"] == "🐔" and b8["text"] == "🐔":
        b2.config(bg = "green")
        b5.config(bg = "green")
        b8.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()
    
    #if column 3 wins
    elif b3["text"] == "🐔" and b6["text"] == "🐔" and b9["text"] == "🐔":
        b3.config(bg = "green")
        b6.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()
    
    #if diagonal 1 wins (\)
    elif b1["text"] == "🐔" and b5["text"] == "🐔" and b9["text"] == "🐔":
        b1.config(bg = "green")
        b5.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()
    
    #if diagonal 2 wins (/)
    elif b3["text"] == "🐔" and b5["text"] == "🐔" and b7["text"] == "🐔":
        b3.config(bg = "green")
        b5.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "CLUCK CLUCK CLUCK! Winner Winner Chicken Dinner!🐔")
        disablebuttons()

    #TO CHECK IF DUCK IS WINNING
    #if row 1 wins
    elif b1["text"] == "🐤" and b2["text"] == "🐤" and b3["text"] == "🐤":
        b1.config(bg = "green")
        b2.config(bg = "green")
        b3.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤")
        disablebuttons()

    #if row 2 wins
    elif b4["text"] == "🐤" and b5["text"] == "🐤" and b6["text"] == "🐤":
        b4.config(bg = "green")
        b5.config(bg = "green")
        b6.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤")
        disablebuttons()

    #if row 3 wins
    elif b7["text"] == "🐤" and b8["text"] == "🐤" and b9["text"] == "🐤":
        b7.config(bg = "green")
        b8.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤!🐤")
        disablebuttons()

    #if column 1 wins
    elif b1["text"] == "🐤" and b4["text"] == "🐤" and b7["text"] == "🐤":
        b1.config(bg = "green")
        b4.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤!🐤")
        disablebuttons()
    
    #if column 2 wins
    elif b2["text"] == "🐤" and b5["text"] == "🐤" and b8["text"] == "🐤":
        b2.config(bg = "green")
        b5.config(bg = "green")
        b8.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤!🐤")
        disablebuttons()
    
    #if column 3 wins
    elif b3["text"] == "🐤" and b6["text"] == "🐤" and b9["text"] == "🐤":
        b3.config(bg = "green")
        b6.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤!🐤")
        disablebuttons()
    
    #if diagonal 1 wins (\)
    elif b1["text"] == "🐤" and b5["text"] == "🐤" and b9["text"] == "🐤":
        b1.config(bg = "green")
        b5.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤!🐤")
        disablebuttons()
    
    #if diagonal 2 wins (/)
    elif b3["text"] == "🐤" and b5["text"] == "🐤" and b7["text"] == "🐤":
        b3.config(bg = "green")
        b5.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("WINNER!", "QUACK QUACK QUACK! You win, you lucky duck!🐤!🐤")
        disablebuttons()
    #check for tie
    if count == 9 and winner == False:
        messagebox.showinfo("Cluck-Quack!", "Cluck-Quack! It's a tie :(")

#when button is clicked
def clickbutton(btn):
    global cluck, count

    if btn["text"] == "" and cluck == True: 
        btn["text"] = "🐔"
        cluck = False
        count +=1
        checkwinner()
    elif btn["text"] == "" and cluck == False:
        btn["text"] = "🐤"
        cluck = True
        count +=1
        checkwinner()
    else:
        if btn["text"] == "🐔": #when button has chicken
            messagebox.showwarning("WARNING", "Clucked already, choose another!")
        if btn["text"] == "🐤": #when button has duck
             messagebox.showwarning("WARNING", "Quacked already, choose another!")

    

#build buttons
b1 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b1))
b2 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b2))
b3 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b3))
b4 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b4))
b5 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b5))
b6 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b6))
b7 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b7))
b8 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b8))
b9 = Button(root, text = "", font = ("Arial", 25), bg = "yellow", height = 4, width = 8, command = lambda: clickbutton(b9))

#add to grid
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)
b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)
b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)


root.mainloop()
#referred codemy.com videos 

