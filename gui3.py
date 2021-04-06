from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
import re
import webbrowser
import urllib.request
from titlecase import titlecase
import pathlib

def testfunc():
    print("Modern GUI")

root = Tk()
global currversion
currversion = "1.0"
root.title("Movie Renamer "+currversion)
root.geometry("500x500")

scrollframe = Frame(root)
yscroll = ttk.Scrollbar(scrollframe,orient=VERTICAL)
xscroll = ttk.Scrollbar(scrollframe,orient=HORIZONTAL)

pathfield = ttk.Entry(root,width=60)
pathfield.grid(row=0,column=0, padx=10,pady=10)
pathfield.bind("<Return>",testfunc)

browzebutton = ttk.Button(root,text="Browse",command=testfunc)
browzebutton.grid(row=0,column=1,padx=10,pady=10)

displaybox = Listbox(scrollframe,width=60,selectmode=EXTENDED,yscrollcommand=yscroll.set,xscrollcommand=xscroll.set)


root.mainloop()