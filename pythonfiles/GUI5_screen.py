#06-03-19
from tkinter import *
wd1=Tk()
wd1.title("Gyanvriksh")
wd1.configure(bg="#ffffff")
wd1.configure( height=400, width=350, bg="#ff00ff")
wd1.geometry("340x400+0+130")
wd1.geometry("340x300+260+130")#geometry(heightxwidth+x+y)
wd1.resizable(width=False, height=False)
print(wd1.winfo_screenwidth()) #Gives width of our system screen
print(wd1.winfo_screenheight()) #Gives heigth of our system screen
wd1.geometry("%dx%d+%d+%d" %(350,380,1024/2,600/2))
wd1.geometry("%dx%d+%d+%d" %(300,350,1024/2-300/2,600/2-350/2))
#wd1.geometry("whxww+x/2+y/2")
#wd1.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
