import numpy as np
import pandas as pd

#Desafio4
#CurrenciesClean.csv y Sales.parquet.
# Lo que te vamos a pedir es que agregues la tasa de conversión a
#  dólares teniendo en cuenta el día y el currencyId. 
#  Por ejemplo, debajo encontrarás la solución de alguien 
#  que optó por agregar como tasa de conversión la columna “dolar_to_local”.

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


salesWithRate = creatingSalesWithRate()
#¿Cuántos ítems hay?
#print(salesWithRate["item_id"].describe())
print("Hay ", len(salesWithRate["item_id"].value_counts()), " items diferentes.")
#2060
amountOfSales =salesWithRate.groupby(["item_id"]).agg({"sales":"sum"})
#¿Cuál es el ítem con más ventas? 
print("El item con mas ventas es: \n ",amountOfSales.sort_values(ascending=False, by= "sales").head(1))
#MPE438744458
#print(amountOfSales.max())
#90

