import requests
import datetime
import os
import json


#Desafio 2

def jsonRequest():
    """This function makes a request and give the result in a json file in the folder 
    "searchjson"+year+month+day """
    category_ID= "MLA1000"
    site_ID= "MLA"
    ask=f'https://api.mercadolibre.com/sites/{site_ID}/search?category={category_ID}'
    r = requests.get(ask)
    search = r.json()
    currentDate = datetime.date.today()
    apiName= "search"
    theFormat="json"
    year = str(currentDate.year)
    month = f"{currentDate:%m}"
    day = f"{currentDate:%d}"
    path = apiName+theFormat+year+month+day
    if not os.path.isdir(path):
        os.makedirs(f"./{path}")
    path +="/data"+category_ID+".json"
    with open(path, 'w') as f:
        json.dump(search, f)

jsonRequest()