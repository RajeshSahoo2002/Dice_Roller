import random
import tkinter as tk

root=tk.Tk()
root.geometry("900x500")
root.title("Dice Roller-App")
textdata=tk.Label(root,text='',font=("Times New Roman",300),bg="orange")

def roll_the_dice():

    numcode=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    textdata.config(text=f'{random.choice(numcode)}{random.choice(numcode)}{random.choice(numcode)}')
    textdata.pack()

#Making The Button For Rolling The Dice
rollbutton=tk.Button(root,text="ROLL DICE",font=("Times New Roman",20,"bold"),height=2,width=10,bg="red",fg="white",command=roll_the_dice)
rollbutton.place(x=250,y=0)
rollbutton.pack()

#Ending The MainLoop
root.mainloop()