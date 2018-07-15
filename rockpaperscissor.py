from tkinter import *
from random import randint
from tkinter.ttk import *
from tkinter import messagebox
# Display window at the center

window=Tk()
width_my_window=500
height_my_window=300
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x_cordinate=(screen_width/2)-(width_my_window/2)
y_cordinate=(screen_height/2)-(height_my_window/2)
window.geometry("%dx%d+%d+%d" %(width_my_window,height_my_window,x_cordinate,y_cordinate))
window.title("Welcome to game world")
window.configure(background="sky blue")

#code of game

selected = IntVar()
rad1 = Radiobutton(window,text='rock' , value= 1, variable=selected)
rad2 = Radiobutton(window,text='Paper', value= 2, variable=selected)
rad3 = Radiobutton(window,text='scissor', value= 3, variable=selected)

def clicked():
    computer=randint(1,3)
    a=selected.get()
    if (a == computer):
        messagebox.showinfo("Result", "Computer choosed SAME as you\nIT'S A DRAW!!!")
    elif a == 1 and computer== 3:
        messagebox.showinfo("Result", "Computer choosed SCISSOR\nYOU WIN HUARRY!!!") 
    elif a== 1 and computer==2:
        messagebox.showinfo("Result", "Computer choosed PAPER\nOpps!!YOU LOSE!!!")
    elif a== 2 and computer== 1:
        messagebox.showinfo("Result", "Computer choosed ROCK\nYOU WIN HUARRY!!!")
    elif a== 2 and computer== 3:
        messagebox.showinfo("Result", "Computer choosed SCISSOR\nOpps!!YOU LOSE!!!")
    elif a== 3 and computer== 2:
        messagebox.showinfo("Result", "Computer choosed PAPER\nYOU WIN HUARRY!!!")
    elif a== 3 and computer== 1:
        messagebox.showinfo("Result", "Computer choosed ROCK\nOpps!YOU LOSE!!!")
def end():
    window.destroy()
    
btn2 = Button(window, text="end game", command=end)
btn = Button(window, text="try your luck", command=clicked)
rad1.pack( side=LEFT,fill=X,padx=30)
rad2.pack( side=LEFT,fill=X,padx=30)
rad3.pack( side=LEFT,fill=X,padx=30)
btn2.pack(side=BOTTOM,anchor="sw",fill=X,padx=30)
btn.pack(side=BOTTOM,anchor="nw",fill=X,padx=30)
window.mainloop()
