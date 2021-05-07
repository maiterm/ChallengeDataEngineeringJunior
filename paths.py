#Desafio 7
# El objetivo del desafío es que podamos ver el desarrollo de una función.
# La cual, recibiendo un conjunto de strings devuelva una Lista de elementos 
# que agrupe desde el primer día del mes hasta la fecha ingresada como parámetros inclusive. 
#Por lo tanto, el objetivo será generar una función Path que devuelva paths 
#hasta el día solicitado. El formato de la url es ficticio.


def generateMonthlyPathList(year, month, day):
    """ It recieves three strings, and returns a list of paths from 
    the first day of the month to the parameter day"""
    path = "https://importantdata@location/"
    paths = [path+year+"/"+month+"/"+str(day_i)+"/" for day_i in range(1,int(day)+1) ]
    return paths

#printing the list as the example
for i in range(17):
    print(generateMonthlyPathList("2021", "05", "17")[i])