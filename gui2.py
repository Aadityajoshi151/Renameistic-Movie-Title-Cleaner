from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

def browse():
    root.directory = filedialog.askdirectory()
    pathfield.insert(0,root.directory)
    for i in os.listdir(root.directory):
        displaybox.insert(END,i)
def rename():
    names = []
    for i in displaybox.curselection():
        names.append(displaybox.get(i))
    for i in names:
        if os.path.isfile(root.directory+"/"+i):
            print(i+" Is A File")
        elif os.path.isdir(root.directory+"/"+i):
            print(i+" Is A Folder")


root = Tk()
root.title("Movie Renamer")
root.geometry("400x400")
pathfield = Entry(root,width=60)
pathfield.pack(padx=10,pady=10)

browzebutton = Button(root,text="Browse",command=browse)
browzebutton.pack(padx=10,pady=10)

displaybox = Listbox(root,width=60,selectmode=EXTENDED)
displaybox.pack()

renamebutton = Button(root,text="Rename",padx=15,pady=15,command=rename)
renamebutton.pack(side=RIGHT,padx=10,pady=10)

root.mainloop()