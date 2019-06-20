from tkinter import *
wd1=Tk()
wd1.title("Gyanvriksh")
wd1.configure( height=400, width=350, bg="#ffff00")
wd1.geometry("340x400+0+130")
wd1.resizable(width=False, height=False)
print(wd1.winfo_screenwidth())
print(wd1.winfo_screenheight())
wd1.geometry("%dx%d+%d+%d" %(300,350,1024/2-300/2,600/2-350/2))
l1=Label(wd1,text="welcome to GUI",font="verdane 26 bold italic",fg="red")
l1.pack()

def f1():
    L2=Label(wd1,text="Python")
    L2.pack()
B1=Button(wd1,text="submit",bd=8,bg="green",command=f1,width=5,height=1)
B1.pack()
