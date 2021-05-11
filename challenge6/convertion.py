import numpy as np
import pandas as pd



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

def createSalesPerIdPerLevel(dataFrame):
    """ """
    levels = ["level1","level2","level3","level4","level5","level6","level7"]
    salesResult=pd.DataFrame()
    for level in levels:
        salesPerLevel = pd.DataFrame()
        dataFrame.replace("", np.nan, inplace=True)
        sales = dataFrame[dataFrame[level].notnull()]
        salesPerLevel["level_id"] = sales[level]
        salesPerLevel["sales"] = sales["sales"]
        groupSalesPerLevel_id = salesPerLevel.groupby("level_id").agg({"sales":"sum"}) 
        groupSalesPerLevel_id = groupSalesPerLevel_id.reset_index()  
        groupSalesPerLevel_id["level"] = level 
        salesResult = pd.concat([salesResult,groupSalesPerLevel_id])
    return salesResult

def createSalesPerLevel(dataFrame):
    salesPerLevel = dataFrame.groupby("level").agg({"sales":"sum"})
    salesPerLevel = salesPerLevel.reset_index()
    return salesPerLevel 
        
#dataframe from challenge4
salesWithRate = creatingSalesWithRate()
#fisrt dataframe asked for on challenge 6
salesPerIdPerLevel = createSalesPerIdPerLevel(salesWithRate)
print("First dataframe asked for starts with something like:")
print(salesPerIdPerLevel.sort_values("sales",ascending=False).head())
#second dataframe 
salesPerLevel = createSalesPerLevel(salesPerIdPerLevel)
print("Second dataframe asked for")
print(salesPerLevel)




