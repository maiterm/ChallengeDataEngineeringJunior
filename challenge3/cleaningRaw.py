import numpy as np
import pandas as pd

#Desafio3
# En la siguiente carpeta: inputEjemplos vas a encontrar un archivo llamado 
# CurrenciesRaw el cual no tiene encabezados y tiene campos erróneos. Lo que te solicitamos:
# Eliminar las columnas que no tienen valores y/o están en cero.
# Eliminar los campos que se encuentran repetidos
# Eliminar la hora
# Darle nombre significativos a los campos.
# Redondear los campos a dos decimales.
# Guardarlo como un CSV.

def clean_file(fileToClean):
    """This function receives a csv file and generate a new cleaned one called "NewCurrenciesRaw.csv"  """
    data = pd.read_csv(fileToClean,sep='\t',header=None)
    #names=["country","datetrack","hour","country1","currency","datetrack1","dollarToLocal","no","localToDollar","nouo","site"])

    #drop duplicates columns
    data = data.T.drop_duplicates().T
    #delete 0, "", o Nan columns 
    data.replace(0, np.nan, inplace=True)
    data.replace("", np.nan, inplace=True)
    data.dropna(how='all', axis=1, inplace=True)
    #delete hour
    data.drop(2,axis="columns",inplace=True)
    #round off the numbers to two decimal places
    data = data.round(2)
    #name the columns
    data.rename(columns={0:"country",1:"datetrack",4:"currency",6:"dollarToLocal",8:"localToDollar",10:"site"},inplace=True)
    print(data.head())

    #save as csv 
    data.to_csv("NewCurrenciesRaw.csv",index=False)


clean_file("currenciesRaw.csv")
