import tkinter
from tkinter import *
import mr_bk as mr


window=tkinter.Tk()
window.title("Movie Recommender")
label=tkinter.Label(window,text='Enter the name of the movie :',font=("Aerial Bold",20))
label.grid(column=1,row=0)
e=tkinter.Entry(window,width=50)
e.grid(column=1,row=1)
    
def create_window():
    l1=" "
    window1 = tkinter.Toplevel(window)
    label1=tkinter.Label(window1,text='the recommended movies are : ',font=("Aerial Bold",20))
    label1.grid(column=0,row=0)
    name=e.get()
    l1=mr.recommendations(name)
    output=tkinter.Text(window1,width=100,height=20)  #output box code
    output.grid(column=0,row=2)
    output.insert(END,l1)
    window1.geometry('820x200')
        
bt1 = Button(window, text="Search",command=create_window) 
bt1.grid(column=1,row=3)

window.geometry('400x250')
window.mainloop()