import numpy as np
import pandas as pd

#Desafio5
# Con el dataframe resultante en el desafío anterior 
# crear un campo llamado “row_key” el cual está compuesto 
# de la siguiente manera: date + category_id

def creatingSalesWithRate():
    """This function open a sales.parquet file and convines it 
    with the localToDolar of the file currenciesClean of the same currency and the day to 
    return a df with the sales and the exchange rates """
    #load the files in df
    sales = pd.read_parquet("sales.parquet",engine="pyarrow")
    currencies = pd.read_csv("currenciesClean.csv")

    #change the dtype of the column to join  
    sales["date"] = pd.to_numeric(sales["date"], downcast= "integer") 

    #rename as the name are used in the sales file
    currencies.rename(columns ={"datetrack":"date","currencyID":"currency_id","localToDolar":"local_to_dolar"}, inplace=True)
    #choosing the columns that we are intrested in 
    currencies = currencies[["currency_id","date","local_to_dolar"]]

    #join
    result=sales.merge(currencies,left_on=["currency_id","date"], right_on=["currency_id","date"] ,how="left")
    return result



def newRowKey(dataFrame):
    """It creates a new column row_key that concatenates date and category_id"""
    #The dtype are needed as string
    dataFrame["date"] = dataFrame["date"].astype(str)
    dataFrame["category_id"] = dataFrame["category_id"].astype(str)
    #now they can be united 
    dataFrame["row_key"] = dataFrame["date"] +"-"+dataFrame["category_id"]
    return dataFrame


salesWithRate = creatingSalesWithRate()
salesWithRowKey = newRowKey(salesWithRate)
print(salesWithRowKey.head())

