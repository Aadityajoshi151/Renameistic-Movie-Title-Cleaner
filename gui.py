from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import string
import re

def selectfiles():
    global dir_list
    dir_list = []
    files = filedialog.askopenfilenames(parent=root, title='Select File(s)')
    files = list(files)
    for i in files:
        temp = i.split("/")
        dir_list.append(temp[-1])
    root.directory = "/".join(temp[i] for i in range(0,len(temp)-1))

def selectfolders():
    global dir_list
    root.directory = filedialog.askdirectory()
    title.config(text=root.directory)
    dir_list = os.listdir(root.directory)

def reset():
    print("Reset Button Clicked!")

def display(finaltitle,finalquality,year,filesize,finalformat,flag):
    if finalformat == formats[0]:
        print(f"New Title: - {finaltitle}")
    elif finalformat == formats[1]:
        print(f"New Title: - {finaltitle} ({year[-1]})")
    elif finalformat == formats[2]:
        print(f"New Title: - {finaltitle} [{year[-1]}]")
    elif finalformat == formats[3]:
        if finalquality == "":
            print(f"New Title: - {finaltitle}")
        else:
            print(f"New Title: - {finaltitle} ({finalquality})")
    elif finalformat == formats[4]:
        if finalquality == "":
            print(f"New Title: - {finaltitle}")
        else:
            print(f"New Title: - {finaltitle} [{finalquality}]")
    elif finalformat == formats[5]:
        print(f"New Title: - {finaltitle} ({filesize})")
    elif finalformat == formats[6]:
        print(f"New Title: - {finaltitle} [{filesize}]")
    elif finalformat == formats[7]:
        if finalquality == "":
            print(f"New Title: - {finaltitle} ({year[-1]})")
        else:
            print(f"New Title: - {finaltitle} ({year[-1]}) [{finalquality}]")
    elif finalformat == formats[8]:
        if finalquality == "":
            print(f"New Title: - {finaltitle} [{year[-1]}]")
        else:
            print(f"New Title: - {finaltitle} [{year[-1]}] ({finalquality})")
    elif finalformat == formats[9]:
        if finalquality == "":
            print(f"New Title: - {finaltitle} [{filesize}]")
        else:
            print(f"New Title: - {finaltitle} ({finalquality}) [{filesize}]")
    elif finalformat == formats[10]:
        if finalquality == "":
            print(f"New Title: - {finaltitle} ({filesize})")
        else:    
            print(f"New Title: - {finaltitle} [{finalquality}] ({filesize})")
    elif finalformat == formats[11]:
        if finalquality == "":
            print("New Title: - "+finaltitle+" ("+year[-1]+") {"+filesize+"}")
        else:
            print("New Title: - "+finaltitle+" ("+year[-1]+") ["+finalquality+"] {"+filesize+"}")

def rename():
    global finalquality
    global filesize
    global flag
    qualities = ["480p","720p","1080p","2160p","DVDrip"]
    counter = 0
    for name in dir_list:
        finalquality = ""
        filesize = os.path.getsize(root.directory+"/"+name)
        print("Old Title: - "+name)
        flag = False
        try:
            for i in qualities:
                if name.lower().find(i.lower())>-1:
                    finalquality = i
                    name = name.replace(finalquality,"")
                    flag = True
                    break
            year = re.findall('([1-3][0-9]{3})', name)
            finaltitle = name[:name.find(year[-1])-1]
            finaltitle = finaltitle.replace("."," ")
            finaltitle = finaltitle.replace("_"," ")
            finaltitle = finaltitle.rstrip()
            finaltitle = string.capwords(finaltitle)
            counter+=1
            display(finaltitle,finalquality,year,filesize,finalformat,flag)
        except:
            continue
    if counter!=len(dir_list):
        messagebox.showinfo("Result",f"Successfully changed {counter}/{len(dir_list)} names.\nSome names were not changed due to lack of information in the title.")
    else:
        messagebox.showinfo("Result",f"Successfully changed {counter}/{len(dir_list)} names.")
def selectformat(event):
    global finalformat
    finalformat = selectedformat.get()
    if finalformat.find("Quality")>-1:
        messagebox.showinfo("Title","You have selected format which involves 'quality'. If 'quality' is not present in the title, it will be omitted.")

root = Tk()
selectedformat = StringVar()
dualaudiocheck = IntVar()
subfoldercheck = IntVar()

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


selectedformat.set("Select A Format")
root.title("Movie Renamer")
root.geometry("350x250")
root.resizable(False,False)
title = Label(root,text="Welcome To Movie Renamer",pady=10)
title.pack()
Button(root,text="Select File(s)",command=selectfiles).pack()
Button(root,text="Select Folder",command=selectfolders).pack()
formatdd = OptionMenu(root,selectedformat,*formats,command=selectformat)
formatdd.config(width=40,pady=5)
formatdd.pack(pady=5)
dualaudiocheckbox = Checkbutton(text = "Add Dual Audio Suffix (If Exists)", variable = dualaudiocheck,
                 onvalue = 1, offvalue = 0,)
subfoldercheckbox = Checkbutton(text = "Rename Files Inside Folder As Well", variable = subfoldercheck,
                 onvalue = 1, offvalue = 0,)
dualaudiocheckbox.pack()
subfoldercheckbox.pack()
Button(root,text="Rename",command=rename,width=7,height=3).pack(side=RIGHT,padx=10,pady=10)
Button(root,text="Reset",command=reset,width=6,height=3).pack(side=LEFT,padx=10,pady=10)
root.mainloop()