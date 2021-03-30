import re
import string
import os 
from pandas import *

def display(finaltitle,finalquality,year,filesize,choice,flag):
    if choice == 1:
        print(f"New Title: - {finaltitle}")
    elif choice == 2:
        print(f"New Title: - {finaltitle} ({year[-1]})")
    elif choice == 3:
        print(f"New Title: - {finaltitle} [{year[-1]}]")
    elif choice == 4:
        if finalquality == "":
            print(f"New Title: - {finaltitle}")
        else:
            print(f"New Title: - {finaltitle} ({finalquality})")
    elif choice == 5:
        if finalquality == "":
            print(f"New Title: - {finaltitle}")
        else:
            print(f"New Title: - {finaltitle} [{finalquality}]")
    elif choice == 6:
        print(f"New Title: - {finaltitle} ({filesize})")
    elif choice == 7:
        print(f"New Title: - {finaltitle} [{filesize}]")
    elif choice == 8:
        if finalquality == "":
            print(f"New Title: - {finaltitle} ({year[-1]})")
        else:
            print(f"New Title: - {finaltitle} ({year[-1]}) [{finalquality}]")
    elif choice == 9:
        if finalquality == "":
            print(f"New Title: - {finaltitle} [{year[-1]}]")
        else:
            print(f"New Title: - {finaltitle} [{year[-1]}] ({finalquality})")
    elif choice == 10:
        if finalquality == "":
            print(f"New Title: - {finaltitle} [{filesize}]")
        else:
            print(f"New Title: - {finaltitle} ({finalquality}) [{filesize}]")
    elif choice == 11:
        if finalquality == "":
            print(f"New Title: - {finaltitle} ({filesize})")
        else:    
            print(f"New Title: - {finaltitle} [{finalquality}] ({filesize})")
    elif choice == 12:
        if finalquality == "":
            print("New Title: - "+finaltitle+" ("+year[-1]+") {"+filesize+"}")
        else:
            print("New Title: - "+finaltitle+" ("+year[-1]+") ["+finalquality+"] {"+filesize+"}")
qualities = ["480p","720p","1080p","2160p","DVDrip"]
didnotwork = []
counter = 0

# print('''
# Press 1 For The Format: - Moviename
# Press 2 For The Format: - Moviename (Year)
# Press 3 For The Format: - Moviename [Year]
# Press 4 For The Format: - Moviename (Quality)
# Press 5 For The Format: - Moviename [Quality]
# Press 6 For The Format: - Moviename (Filesize)
# Press 7 For The Format: - Moviename [Filesize]
# Press 8 For The Format: - Moviename (Year) [Quality]
# Press 9 For The Format: - Moviename [Year] (Quality)
# Press 10 For The Format: - Moviename (Qualtiy) [Filesize]
# Press 11 For The Format: - Moviename [Qualtiy] (Filesize)
# Press 12 For The Format: - Moviename (Year) [Qualtity] {Filesize}
# ''')
choice = 8
with open("100Test.txt", 'r') as file_handle:
    # read file content into list
    dir_list = file_handle.readlines()
dir_list = [line.strip() for line in dir_list]

for name in dir_list:
    finalquality = ""
    filesize = ""
    counter+=1
    #filesize = os.path.getsize("E://Github//Movie Renamer//Samples1//"+name)
    print("Count: - "+str(counter))
    print("Old Title: - "+name)
    flag = False
    try:
        for i in qualities:
            if name.lower().find(i.lower())>-1:
                finalquality = i
                name = name.replace(finalquality,"")
                flag = True
                break
        # print("Name:- "+name)
        year = re.findall('([1-3][0-9]{3})', name)
        while True:
            if int(year[-1]) < 1880:
                del year[-1]
            else:
                break
        # print("Final Quality: - "+finalquality)
        # print("Final Year: - "+str(year[-1]))
        finaltitle = name[:name.find(year[-1])-1]
        finaltitle = finaltitle.replace("."," ")
        finaltitle = finaltitle.replace("_"," ")
        finaltitle = finaltitle.rstrip()
        finaltitle = string.capwords(finaltitle)
        #counter+=1
        # if flag == True:
        #     
        #     print("_"*80)           
        # else:
        #     display(finaltitle,finalquality,year,filesize,choice,flag)
        #     #print("New Title: - "+finaltitle+" ("+year[-1]+")")
        #     print("_"*80)  
        display(finaltitle,finalquality,year,filesize,choice,flag)
        print("_"*80)
        getch = input()
        os.system('cls')
    except:
        print("Did Not Work On This!")
        continue