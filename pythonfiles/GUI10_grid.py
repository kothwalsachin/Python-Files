#06-03-19
from tkinter import *
wd1=Tk()
wd1.title("Gyanvriksh")
wd1.configure(bg="#ffffff")
wd1.configure( height=400, width=350, bg="#ff00ff")
wd1.geometry("340x300+260+130")
l1=Label(wd1,text="Python",font="verdane 26 bold italic",fg="red")
l1.grid(row=0,column=0)
l2=Label(wd1,text="Java",font="verdane 20 bold italic",fg="red")
#l2.pack()
l2.grid(row=3,column=3)
wd1.mainloop() #It will be inside the loop only in shell we can't see next
#prompt 
