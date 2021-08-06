import csv
import plotly_express as px
import numpy as np

with open('MarksVsDays.csv') as csv_file:
    df = csv.DictReader(csv_file)
    plot_figure = px.scatter(df,title='Correlation of attendance and marks',x='Days Present',y='Marks In Percentage')
    plot_figure.show()
def getDataSource(data_path):
    daysPresent = []
    marksAsPercent = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            daysPresent.append(float(row['Days Present']))
            marksAsPercent.append(float(row['Marks In Percentage']))
    return {'x':daysPresent,'y':marksAsPercent}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between the days present and marks : ',correlation[0,1])
def Setup():
    data_path = 'MarksVsDays.csv'
    dataSource =  getDataSource(data_path)
    findCorrelation(dataSource)
Setup()