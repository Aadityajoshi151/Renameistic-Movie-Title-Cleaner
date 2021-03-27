from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import re
import string
import pathlib

def combinename():
    if finalformat == formats[0]:
        return (f"{finaltitle}")
    elif finalformat == formats[1]:
        return (f"{finaltitle} ({year[-1]})")
    elif finalformat == formats[2]:
        return (f"{finaltitle} [{year[-1]}]")
    elif finalformat == formats[3]:
        if finalquality == "":
            return (f"{finaltitle}")
        else:
            return (f"{finaltitle} ({finalquality})")
    elif finalformat == formats[4]:
        if finalquality == "":
            return (f"{finaltitle}")
        else:
            return (f"{finaltitle} [{finalquality}]")
    elif finalformat == formats[5]:
        return (f"{finaltitle} ({filesize})")
    elif finalformat == formats[6]:
        return (f"{finaltitle} [{filesize}]")
    elif finalformat == formats[7]:
        if finalquality == "":
            return (f"{finaltitle} ({year[-1]})")
        else:
            return (f"{finaltitle} ({year[-1]}) [{finalquality}]")
    elif finalformat == formats[8]:
        if finalquality == "":
            return (f"{finaltitle} [{year[-1]}]")
        else:
            return (f"{finaltitle} [{year[-1]}] ({finalquality})")
    elif finalformat == formats[9]:
        if finalquality == "":
            return (f"{finaltitle} [{filesize}]")
        else:
            return (f"{finaltitle} ({finalquality}) [{filesize}]")
    elif finalformat == formats[10]:
        if finalquality == "":
            return (f"{finaltitle} ({filesize})")
        else:    
            return (f"{finaltitle} [{finalquality}] ({filesize})")
    elif finalformat == formats[11]:
        if finalquality == "":
            return (f"{finaltitle} ({year[-1]}) {{{filessize}}}")
        else:
            return (f"{finaltitle} ({year[-1]}) [{finalquality}] {{{filessize}}}")    
def browse():
    root.directory = filedialog.askdirectory()
    pathfield.insert(0,root.directory)
    for i in os.listdir(root.directory):
        displaybox.insert(END,i)
def rename():
    names = []
    global finalquality
    global filesize
    global flag
    global year
    global finaltitle
    qualities = ["480p","720p","1080p","2160p","DVDrip"]
    counter = 0
    for i in displaybox.curselection():
        names.append(displaybox.get(i))
    for name in names:
        temp = name
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
            winnername = combinename()
        except:
            continue
        print(winnername)
        if os.path.isdir(root.directory+"/"+temp):
            os.rename(root.directory+"/"+temp,root.directory+"/"+winnername)
        elif os.path.isfile(root.directory+"/"+temp):
            extension = pathlib.Path(temp).suffix
            os.rename(root.directory+"/"+temp,root.directory+"/"+winnername+extension)



def selectformat(event):
    global finalformat
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