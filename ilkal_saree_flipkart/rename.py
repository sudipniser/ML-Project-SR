import os 
i=0
for file in os.listdir()[:-1]:
    os.rename(file,f"{int(file[:-4])+357}.jpg")
    i+=1


