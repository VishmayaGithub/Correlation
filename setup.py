import numpy as np
import plotly.express as px
import csv

with open('data.csv') as f:
    reader = csv.DictReader(f)
    fig = px.scatter(reader,x='Marks In Percentage',y='Days Present')
    fig.show()

def data_reading(data):
    marks = []
    days = []
    with open(data) as csv_file:
        reading = csv.DictReader(csv_file)
        for row in reading:
            marks.append(float(row["Marks In Percentage"])) 
            days.append(float(row["Days Present"]))   

    return{"x" : marks , "y" : days}        

def correlation(datasource):
    cor = np.corrcoef(datasource["x"],datasource["y"])
    print('Correlation -->',cor[0,1])

def main():
    data = 'data.csv'
    blaj = data_reading(data)
    correlation(blaj) 

main()       