from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk      #for modern looking widgets
from titlecase import titlecase    #for final name in captial letters 
import os     #for renaming and opening/walking directories
import re     #for finding year (4-digit numbers)
import webbrowser   #for opening feedback form,portfolio and download page
import urllib.request   #for checking txt file for updates
import pathlib   #has the suffix() method used for finding extensions
    
def update():
    try:
        newversion = urllib.request.urlopen("https://raw.githubusercontent.com/Aadityajoshi151/Renameistic-Movie-Title-Cleaner/main/version.txt").read()
        #reading file from github
        newversion = newversion.decode('utf-8').split()[0]
        #removing the letter 'b' which is there as a prefix in file contents
        if currversion == newversion:
            messagebox.showinfo("Latest Version Detected","You are running the latest version. No update required.")
        else:
            ans = messagebox.askyesno("New Version Available","A newer version (v"+newversion+") is available for download. Would you like to download it now?")
            if ans:
                webbrowser.open_new("https://github.com/Aadityajoshi151/Renameistic-Movie-Title-Cleaner")
    except:
        messagebox.showerror("An Error Occurred","There was a problem connecting with the server. Please check your internet connection or try again later.")


def enterpressed(event=None):
    root.directory = pathfield.get()  #when enter key is pressed when textfield is active, its fetches its value
    populate()  #listbox is populated with the root directory contents

def combinename():  #The most important function of program
    #return f strings based on the user selected format
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
        #this does not return f string beacuse of the need of {} in the string itself.
        if finalquality == "":
            return (finaltitle+" ("+year[-1]+") {"+filesize+"}")
        else:
            return (finaltitle+" ("+year[-1]+") ["+finalquality+"] {"+filesize+"}")    

def populate():
    try:
        displaybox.delete(0,END)  #clears previous values from listbox
        for i in os.listdir(root.directory):
            if os.path.isdir(root.directory+"/"+i):
                displaybox.insert(END,"📁 "+i) #appends folder icon and puts folder in listbox
            elif os.path.isfile(root.directory+"/"+i):
                displaybox.insert(END,"📄 "+i) #appends file icon and puts file in listbox
        selectallbtn.config(state=ACTIVE)  #enables select-all button
    except:
        messagebox.showerror("Invalid Path","Please enter or select a valid path")

def browse():
    root.directory = filedialog.askdirectory()  #displays open folder dialog
    if not root.directory == "":  #dialog return string. if cancel button is clicked, this condition will be false
        pathfield.delete(0,END)   #clears the textfielf
        pathfield.insert(0,root.directory)  #puts the path of the directory selected in the textfield
        populate()

def openFeedbackForm():
    webbrowser.open_new("https://forms.gle/xYzrbwYoicHu5zHX6")

def copytoclip():
    root.clipboard_clear() 
    root.clipboard_append("\n".join(i for i in didnotwork))
    openFeedbackForm()
        
def selectall():
    displaybox.select_set(0,END)

def displaydidnotwork():
    root.bell()   #to make sound
    dnw = Toplevel()
    dnw.attributes("-toolwindow", True) #removes icon,minimize,mazimize buttons from window
    dnw.resizable("False","False")  
    newscrollframe = Frame(dnw)
    newyscroll = Scrollbar(newscrollframe,orient=VERTICAL) 
    lbl = Label(dnw,text=f"Renamed {counter}/{len(names)} files successfully.\n The following {len(names)-counter} files were not renamed due to lack of information in their title(s).\nYou can copy and submit these titles on feedback form to help the developer.")
    lbl.pack(padx=10,pady=10)
    newdisplaybox = Listbox(newscrollframe,width=60,selectmode=EXTENDED,yscrollcommand=newyscroll.set,height=5)
    newyscroll.config(command=newdisplaybox.yview)
    newyscroll.pack(side=RIGHT,fill=Y)
    newscrollframe.pack()
    newdisplaybox.pack()
    for x in didnotwork:
        newdisplaybox.insert(END,x)
    okbtn = ttk.Button(dnw,text="OK",command=dnw.destroy)
    okbtn.pack(padx=10,pady=10,side=RIGHT)
    testbtn = ttk.Button(dnw,text="Copy And Open Feedback Form",command=copytoclip)
    testbtn.pack(padx=10,pady=10,side=LEFT)

def easteregg(event=None):
    messagebox.showinfo("🎉🎉 Easter Egg 🎉🎉","CONGRATULATIONS from Aaditya Joshi (developer) on discovering this easter egg. It appears when you middle-click on the browse button.")

def rename():
    global names
    names = []   #has selected names from the listbox
    global finalquality
    global filesize
    global flag  #for finding if quality is present or not
    global year
    global finaltitle
    global didnotwork
    global counter
    qualities = ["480p","720p","1080p","2160p","DVDrip","CAMRip","DVDSCR","HDRip"]
    didnotwork = []
    counter = 0
    for i in displaybox.curselection():  #selected names from listbox are append in names[]
        names.append(displaybox.get(i))
    if names:  #if names[] is has something
        for name in names:
            name=name.replace("📁 ","")  #removes folder icon
            name=name.replace("📄 ","")  #removes file icon
            temp = name
            finalquality = ""
            filesize=0
            #FILE SIZE CODE BEGINS HERE
            if os.path.isdir(root.directory+"/"+temp):  #folder-size calculation
                for path, dirs, files in os.walk(root.directory+"/"+temp):
                    for f in files:
                        fp = os.path.join(path, f)
                        filesize += os.stat(fp).st_size
            else:      
                filesize = os.path.getsize(root.directory+"/"+temp)  #file size is simply returned
            n = 0
            power=2**10
            power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
            while filesize > power:
                filesize /= power
                n += 1
            filesize=str(str(round(filesize,1))+" "+str(power_labels[n])+"B")
            #FILE SIZE CODE ENDS HERE
            flag = False
            try:
                for i in qualities:
                    if name.lower().find(i.lower())>-1:
                        finalquality = i
                        name = name.replace(finalquality,"")  #removes finalquality from title so no confusion occurs when year is calculated
                        flag = True
                        break
                #Finding out if folder is individual or collection
                if re.search("\d{4}-\d{4}", name): #A Collection example (2005-2010)
                    year = re.findall("\d{4}-\d{4}", name)
                else:
                    year = re.findall('([1-3][0-9]{3})', name) #Individual example (2013)
                    while True:
                        if int(year[-1]) < 1880:
                            del year[-1]
                        else:
                            break
                finaltitle = name[:name.find(year[-1])-1]  #everything before year is the title
                finaltitle = finaltitle.replace("."," ")
                finaltitle = finaltitle.replace("_"," ")
                finaltitle = finaltitle.rstrip()
                #removing [anything] prefix from title if present
                if re.search("[\[].*?[\]]",finaltitle.split(" ")[0]):   
                    finaltitle =finaltitle.split(" ", 1)[1]
                
                finaltitle = titlecase(finaltitle)  #title is converted in captial letters
                counter+=1
                winnername = combinename()  #combinename returns the appropriate string based on selected format
            except:
                didnotwork.append(name)
                continue
            if os.path.isdir(root.directory+"/"+temp):  #if it was a folder
                os.rename(root.directory+"/"+temp,root.directory+"/"+winnername)
                if subfoldercheck.get() == 1:  #if sub-file chekbox is checked
                    try:
                        commonextensions = [".mkv",".avi",".mp4",".wmv",".mov",".flv",]
                        subfiles = {}          
                        for j in os.listdir(root.directory+"/"+winnername):
                            if pathlib.Path(root.directory+"/"+winnername+"/"+j).suffix in commonextensions:
                                subfiles[j] = os.path.getsize(root.directory+"/"+winnername+"/"+j)
                        subextension = pathlib.Path(root.directory+"/"+winnername+"/"+max(subfiles, key=subfiles.get)).suffix
                        os.rename(root.directory+"/"+winnername+"/"+max(subfiles, key=subfiles.get),root.directory+"/"+winnername+"/"+winnername+subextension)
                        #the biggest file with a video extension is renamed same as the folder
                    except:
                        pass   #if the folder contains more folders so sub-renaming does not occur
            elif os.path.isfile(root.directory+"/"+temp):
                extension = pathlib.Path(temp).suffix
                os.rename(root.directory+"/"+temp,root.directory+"/"+winnername+extension)
        populate()  #the newly renamed titles appear in the listbox
        if counter == len(names):  #all titles were renamed
            messagebox.showinfo("Result","Renaming Successful")
        else:   #some of the titles were not renamed
            displaydidnotwork()
    else:
        messagebox.showerror("No Item Selected","Please select at least 1 item from the list")


def selectformat(event):
    global finalformat
    finalformat = selectedformat.get()  #fetches selected format from dropdown
    renamebutton.config(state=ACTIVE)   #enables rename button
    if finalformat.find("Quality")>-1:  #if 'quality' is present
        messagebox.showinfo("Quality","You have selected format which involves 'quality'. If 'quality' is not present in the title, it will be omitted.")


root = Tk()
global currversion
currversion = "1.0"  #current version
root.title("Renameistic "+currversion)  #title bar
root.geometry("400x450")  #size
root.resizable("False","False") #non-resizable window
root.iconbitmap(default="icon.ico") #icon

extras = Menu(root)
root.config(menu=extras)
extrasmenu = Menu(extras,tearoff=False)  #removes dotted line from menu
extras.add_cascade(label="Help",menu=extrasmenu)
# extrasmenu.add_command(label = "📜 Instructions")
# extrasmenu.add_separator()
extrasmenu.add_command(label = "🌐 Check for Updates",command=update)
extrasmenu.add_command(label = "📮 Feedback",command=openFeedbackForm)
extrasmenu.add_separator()
extrasmenu.add_command(label = "👦 About",command=lambda: webbrowser.open_new("https://aadityajoshi151.github.io/"))

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



pathfield = ttk.Entry(root,width=60)
pathfield.pack(padx=10,pady=10)
pathfield.bind("<Return>",enterpressed)

browzebutton = ttk.Button(root,text="Browse",command=browse)
browzebutton.pack(padx=10,pady=10)
browzebutton.bind("<Button-2>",easteregg)

displaybox = Listbox(scrollframe,width=60,selectmode=EXTENDED,yscrollcommand=yscroll.set,xscrollcommand=xscroll.set)

yscroll.config(command=displaybox.yview)
yscroll.pack(side=RIGHT,fill=Y)
xscroll.config(command=displaybox.xview)
xscroll.pack(side=BOTTOM,fill=X)
scrollframe.pack()
displaybox.pack()

selectallbtn = ttk.Button(root,text="Select All",state=DISABLED,command=selectall)
selectallbtn.pack(padx=10,pady=10)

formatdd = OptionMenu(root,selectedformat,*formats,command=selectformat)
formatdd.config(width=40,pady=5)
formatdd.pack(pady=10)

subfoldercheckbox = ttk.Checkbutton(text = "Rename Video Files Inside Folder As Well (Only 1 Level)", variable = subfoldercheck,
                 onvalue = 1, offvalue = 0,)
subfoldercheckbox.pack()

renamebutton = ttk.Button(root,text="Rename",command=rename,state=DISABLED)
renamebutton.pack(side=RIGHT,padx=10,pady=10)

root.mainloop()