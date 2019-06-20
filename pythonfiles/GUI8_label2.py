from tkinter import *
wd1=Tk()
wd1.title("Gyanvriksh")
wd1.configure(bg="#ffffff")
wd1.configure( height=400, width=350, bg="#ff00ff")
wd1.geometry("340x400+0+130")
wd1.resizable(width=False, height=False)
wd1.geometry("%dx%d+%d+%d" %(300,350,1024/2-300/2,600/2-350/2))
var1=StringVar()
l1=Label(wd1,textvariable=var1)
l1.pack()
l1['text']="Changes"
var1.set("welcome all")
