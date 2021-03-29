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
def populate():
    for i in os.listdir(root.directory):
        if os.path.isdir(root.directory+"/"+i):
            displaybox.insert(END,"📁 "+i)
        elif os.path.isfile(root.directory+"/"+i):
            displaybox.insert(END,"📄 "+i)

def browse():
    root.directory = filedialog.askdirectory()
    pathfield.insert(0,root.directory)
    populate()
    selectallbtn.config(state=ACTIVE)

def selectall():
    displaybox.select_set(0,END)


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
    print(names)
    for name in names:
        name=name.replace("📁 ","")
        name=name.replace("📄 ","")
        temp = name
        finalquality = ""
        filesize=0
        #FILE SIZE CODE BEGINS HERE
        if os.path.isdir(root.directory+"/"+temp):
            for ele in os.scandir(root.directory+"/"+temp):
                filesize+=os.path.getsize(ele)
        else:      
            filesize = os.path.getsize(root.directory+"/"+temp)
        print(filesize)
        n = 0
        power=2**10
        power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
        while filesize > power:
            filesize /= power
            n += 1
        filesize=str(str(round(filesize,1))+" "+str(power_labels[n])+"B")
        print(filesize)
        #FILE SIZE CODE ENDS HERE
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
            if subfoldercheck.get() == 1:
                commonextensions = [".mkv",".avi",".mp4",".wmv",".mov",".flv",]
                subfiles = {}          
                for j in os.listdir(root.directory+"/"+winnername):
                    if pathlib.Path(root.directory+"/"+winnername+"/"+j).suffix in commonextensions:
                        subfiles[j] = os.path.getsize(root.directory+"/"+winnername+"/"+j)
                os.rename(root.directory+"/"+winnername+"/"+max(subfiles, key=subfiles.get),root.directory+"/"+winnername+"/"+winnername+pathlib.Path(root.directory+"/"+winnername+"/"+j).suffix)
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
root.geometry("400x500")

scrollframe = Frame(root)
yscroll = Scrollbar(scrollframe,orient=VERTICAL)
xscroll = Scrollbar(scrollframe,orient=HORIZONTAL)

selectedformat = StringVar()
subfoldercheck = IntVar()
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

displaybox = Listbox(scrollframe,width=60,selectmode=EXTENDED,yscrollcommand=yscroll.set,xscrollcommand=xscroll.set)

yscroll.config(command=displaybox.yview)
yscroll.pack(side=RIGHT,fill=Y)
xscroll.config(command=displaybox.xview)
xscroll.pack(side=BOTTOM,fill=X)
scrollframe.pack()
displaybox.pack()

selectallbtn = Button(root,text="Select All",state=DISABLED,command=selectall)
selectallbtn.pack(padx=10,pady=10)

formatdd = OptionMenu(root,selectedformat,*formats,command=selectformat)
formatdd.config(width=40,pady=5)
formatdd.pack(pady=10)

subfoldercheckbox = Checkbutton(text = "Rename Video Files Inside Folder As Well (Only 1 Level)", variable = subfoldercheck,
                 onvalue = 1, offvalue = 0,)
subfoldercheckbox.pack()

renamebutton = Button(root,text="Rename",padx=15,pady=15,command=rename)
renamebutton.pack(side=RIGHT,padx=10,pady=10)

root.mainloop()