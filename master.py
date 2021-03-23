import re
import string
import os 

qualities = ["480p","720p","1080p","2160p","dvdrip"]
didnotwork = []
counter = 0
dir_list = os.listdir("E://Github//Movie Renamer//Samples")
for name in dir_list:
    print("Old Title: - "+name)
    flag = False
    try:
        for i in qualities:
            if name.lower().find(i)>-1:
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
            print("New Title: - "+finaltitle+" ("+year[-1]+") ["+finalquality+"]")
            print("_"*80)           
        else:
            print("New Title: - "+finaltitle+" ("+year[-1]+")")
            print("_"*80)  
    except:
        didnotwork.append(name)
        continue
print(f"Successfully Changed {counter}/{len(dir_list)} Names")
print("The Following Names Were Not Changed Due Lack Of Enough Information:-")
for i in didnotwork: print(i)