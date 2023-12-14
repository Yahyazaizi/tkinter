from tkinter import *

import random


secret = random.randint(1, 100)

def check_guess():
   guess = int(number.get())
   if guess == secret:

         result_label.config(text="i won !:")

   elif  guess < secret:

     result_label.config(text="add a number!") 
   else:

       result_label.config(text="decrease a number!")



window =Tk()

window.title("guess the nunber !")

Label(window, text="guess a number betweenand 1 and 100").pack()

number=Entry(window)

number.pack()

Button (window, text="check !" ,command=check_guess).pack()


result_label=Label (window, text="")

result_label.pack()

window.mainloop()