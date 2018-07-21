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
photo=PhotoImage(file="rock.png")
photo1=PhotoImage(file="paper.png")
photo2=PhotoImage(file="cut.png)
rad1 = Radiobutton(window,image=photo ,text='rock' , value= 1, variable=selected)
label=Label(window,text='rock')                 
rad2 = Radiobutton(window,image=photo1 ,text='Paper', value= 2, variable=selected)
label1=Label(window,text='paper')                  
rad3 = Radiobutton(window,image=photo2 ,text='scissor', value= 3, variable=selected)
label2=Label(window,text='scissor')
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
rad1.pack( side=LEFT,fill=X,padx=10)
label.pack(side=LEFT,fill=Y,padx=0)
rad2.pack( side=LEFT,fill=X,padx=10)
label1.pack(side=LEFT,fill=Y,padx=0)
rad3.pack( side=LEFT,fill=X,padx=10)
label2.pack(side=LEFT,fill=Y,padx=0)
btn2.pack(side=BOTTOM,anchor="sw",fill=X,padx=10)
btn.pack(side=BOTTOM,anchor="nw",fill=X,padx=10)
window.mainloop()
