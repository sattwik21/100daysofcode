import random
import tkinter

root= tkinter.Tk()
root.geometry("800x500")

label= tkinter.Label(root,font=("Helvetica",350),)

def roll():
  dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
  label.configure(text=f'{random.choice(dice)}')
  label.pack()

def roll_start():
  dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', '\u2680', '\u2680', '\u2680', '\u2680']
  label.configure(text=f'{random.choice(dice)}')
  label.pack()

def roll_end():
  dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', '\u2685', '\u2685', '\u2685', '\u2685']
  label.configure(text=f'{random.choice(dice)}')
  label.pack()


b1= tkinter.Button(root,text="Roll the Dice",command=roll, foreground='blue')
b1.place(x = 350, y = 10)

b2= tkinter.Button(root,text="Roll for 1",command=roll_start, foreground='red')
b2.place(x = 150, y = 10)

b2= tkinter.Button(root,text="Roll for 6",command=roll_end, foreground='green')
b2.place(x = 550, y = 10)


root.mainloop()