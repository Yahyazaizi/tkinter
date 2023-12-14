import tkinter as tk


from time import strftime



def update_time():

    time=strftime('%H:%M:%S %p')

    lb1.config(text=time)

    lb1.after(1988, update_time)


root=tk. Tk()

root.title("Digital clock")

lb1=tk. Label(root, font=('LCD Solid', 50, 'bold'), background='black', foreground="green")

lb1.pack(anchor="center")

update_time()

root.mainloop()