#07-03-19:
from tkinter import *
wd1=Tk()
wd1.title("Gyanvriksh")
wd1.configure(bg="#ffffff")
wd1.configure( height=400, width=350, bg="#ff00ff")
wd1.geometry("340x400+0+130")
wd1.geometry("340x300+260+130")#geometry(heightxwidth+x+y)

#gmimage=PhotoImage(file="C:\Users\Anjalelu\Downloads\image.jpg")
#L1=Label(wd1,image="gmimage")
#L1.pack()"""

wd1.resizable(width=False, height=False)
print(wd1.winfo_screenwidth()) #Gives width of our system screen
print(wd1.winfo_screenheight()) #Gives heigth of our system screen
wd1.geometry("%dx%d+%d+%d" %(350,380,1024/2,600/2))
wd1.geometry("%dx%d+%d+%d" %(300,350,1024/2-300/2,600/2-350/2))

#l1=Label(wd1, text="welcome to GUI")
l1=Label(wd1,text="welcome",font="verdane 26 bold italic",fg="red",
         relief="solid",borderwidth=3,height=5,width=13,anchor='w',padx=26,
         pady=5,justify="right")
l1.pack()

#relief='raised'(or)'flat'(or)'raised'(or)'sunken'(or)'solid'(or)'groove'
