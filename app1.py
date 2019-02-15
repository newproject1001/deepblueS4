from tkinter import filedialog

from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

top = Tk()
top.geometry("400x300")

global database
database=[('ashraful','12345'),('junaid','54321')]

global filename

def registration():
    global database
    database=[('ashraful','12345'),('junaid','54321')]

def app():
    global un
    global ps
    l=Label(top,text="Admin Login")
    l.place(x = 10,y = 80)
    
    l=Label(top,text="Username")
    l.place(x = 80,y = 80)

    un = Entry(top,width=20)
    un.place(x = 180,y = 80)

    l=Label(top,text="Password")
    l.place(x = 80,y = 120)

    ps = Entry(top,width=20)
    ps.place(x = 180,y = 120)

    lg = Button(top, text = "Login",command=login)
    lg.place(x = 200,y = 180)

  
def login():
    if (un.get(),ps.get()) in database:
        top1 = Tk()
        top1.geometry("300x300")
        l=Label(top1,text="choose file for visualisation")
        l.place(x = 80,y = 120)
        fo = Button(top1, text = "open file",command=openfile)
        fo.place(x = 130,y = 150)

        pp = Button(top1, text = "line plot",command=line_plot)
        pp.place(x = 200,y = 200)

        lp = Button(top1, text = "point plot",command=point_plot)
        lp.place(x = 50,y = 200)
        
    else:
        popupmsg()

def openfile():
    global filename
    global rfile
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    rfile = pd.read_excel(filename)
    
def line_plot():
    time=rfile['time']
    light_value=rfile['Light_Problem']
    smell_value=rfile['Dirty_Smells']
    water_value=rfile['Water_Isuue']
    print(time)

def point_plot():
    time=rfile['time']
    light_value=rfile['Light_Problem']
    smell_value=rfile['Dirty_Smells']
    water_value=rfile['Water_Isuue']
    

def popupmsg():
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text='username and password wrong')
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    


app()
top.mainloop()
