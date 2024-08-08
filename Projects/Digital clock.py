import tkinter as tk #tkinter for graphcal interface
from time import strftime

root=tk.Tk() #root to display the elements
root.title("Digital Clock")

def time():
  string= strftime("%I:%M:%S %p \n %D") # Here %I= hour, %M= minite, %S= second, %p= AM/PM, %D= dd/mm/yy
  label.config(text=string)
  label.after(1000,time)

label= tk.Label(root, font=('Arial', 30, 'bold'),background='black', foreground='white')
label.pack(anchor='center') #pack method to arange element in window

time()

root.mainloop() #mainloop to run tkinter in loop
