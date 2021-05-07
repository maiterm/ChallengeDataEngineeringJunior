import numpy as np
import pandas as pd

#desafio 8 

def generateLastDaysPaths(date, days):
    """It receives a string with the date and an int with the amount of last days, and 
    return a list of paths with that dates"""
    dateNumpy =np.datetime64( date[0:4]+"-"+date[4:6]+"-"+date[6:])+ np.timedelta64(1,'D')
    firstDate = dateNumpy -  np.timedelta64(days,'D')
    dates =np.arange(start=firstDate,stop=dateNumpy ,step=np.timedelta64(1,'D'))
    dates = pd.to_datetime(dates)
    path = "https://importantdata@location/"
    paths = [path+str(datei.year)+"/"+str(datei.month)+"/"+str(datei.day)+"/" for datei in dates ]
    return paths

#printing the list as the example
LastDaysPaths = generateLastDaysPaths("20210410", 10)
for i in range(10):
    print(LastDaysPaths[i])