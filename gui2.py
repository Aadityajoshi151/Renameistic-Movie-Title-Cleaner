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

def selectformat(event):
    finalformat = selectedformat.get()
    if finalformat.find("Quality")>-1:
        messagebox.showinfo("Title","You have selected format which involves 'quality'. If 'quality' is not present in the title, it will be omitted.")


root = Tk()
root.title("Movie Renamer")
root.geometry("400x400")

selectedformat = StringVar()
selectedformat.set("Select A Format")
formats = [
"Movie Name",
"Movie Name (Year)",
"Movie Name [Year]",
"Movie Name (Quality)",
"Movie Name [Quality]",
"Movie Name (Filesize)",
"Movie Name [Filesize]",
"Movie Name (Year) [Quality]",
"Movie Name [Year] (Quality)",
"Movie Name (Quality) [Filesize]",
"Movie Name [Quality] (Filesize)",
"Movie Name (Year) [Quality] {Filesize}"
]
pathfield = Entry(root,width=60)
pathfield.pack(padx=10,pady=10)

browzebutton = Button(root,text="Browse",command=browse)
browzebutton.pack(padx=10,pady=10)

displaybox = Listbox(root,width=60,selectmode=EXTENDED)
displaybox.pack()

formatdd = OptionMenu(root,selectedformat,*formats,command=selectformat)
formatdd.config(width=40,pady=5)
formatdd.pack(pady=10)

renamebutton = Button(root,text="Rename",padx=15,pady=15,command=rename)
renamebutton.pack(side=RIGHT,padx=10,pady=10)

root.mainloop()