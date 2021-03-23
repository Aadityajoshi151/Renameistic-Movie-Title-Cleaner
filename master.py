import re
import string
import os 
def display(finaltitle,finalquality,year,filesize,choice,flag):
    if choice == 1:
        print(f"New Title: - {finaltitle}")
    elif choice ==2:
        print(f"New Title: - {finaltitle} ({year[-1]})")

qualities = ["480p","720p","1080p","2160p","DVDrip"]
didnotwork = []
counter = 0
finalquality = ""
print('''
Press 1 For The Format: - Moviename
Press 2 For The Format: - Moviename (Year)
Press 3 For The Format: - Moviename [Year]
Press 4 For The Format: - Moviename (Quality)
Press 5 For The Format: - Moviename [Quality]
Press 6 For The Format: - Moviename (Filesize)
Press 7 For The Format: - Moviename [Filesize]
Press 8 For The Format: - Moviename (Year) [Quality]
Press 9 For The Format: - Moviename [Year] (Quality)
Press 10 For The Format: - Moviename (Qualtiy) [Filesize]
Press 11 For The Format: - Moviename [Qualtiy] (Filesize)
Press 12 For The Format: - Moviename (Year) [Qualtity] {Filesize}
''')
choice = int(input())
dir_list = os.listdir("E://Github//Movie Renamer//Samples1")
for name in dir_list:
    filesize = os.path.getsize("E://Github//Movie Renamer//Samples1//"+name)
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
        # print("Final Quality: - "+finalquality)
        # print("Final Year: - "+str(year[-1]))
        finaltitle = name[:name.find(year[-1])-1]
        finaltitle = finaltitle.replace("."," ")
        finaltitle = finaltitle.replace("_"," ")
        finaltitle = finaltitle.rstrip()
        finaltitle = string.capwords(finaltitle)
        counter+=1
        if flag == True:
            display(finaltitle,finalquality,year,filesize,choice,flag)
            print("_"*80)           
        else:
            display(finaltitle,finalquality,year,filesize,choice,flag)
            #print("New Title: - "+finaltitle+" ("+year[-1]+")")
            print("_"*80)  
    except:
        didnotwork.append(name)
        continue
print(f"Successfully Changed {counter}/{len(dir_list)} Names")
print("The Following Names Were Not Changed Due Lack Of Enough Information:-")
for i in didnotwork: print(i)