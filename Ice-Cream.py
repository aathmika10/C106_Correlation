import plotly_express as px
import csv
import numpy as np

def getData(dataPath):
    iceCreamSales=[]
    Temperature=[]
    with open (dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Temperature.append(float(row["Temperature"]))
            iceCreamSales.append(float(row["Ice-cream Sales"]))
    return{"x":Temperature,"y":iceCreamSales}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation coefficient is ", correlation[0,1])

def setup():
    dataPath="Ice-Cream.csv"
    dataSource=getData(dataPath)
    findCorrelation(dataSource)

setup()