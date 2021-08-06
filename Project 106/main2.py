import numpy as np
import plotly_express as px
import csv
with open('CoffeeVsSleep.csv') as csv_file:
    df = csv.DictReader(csv_file)
    plot_figure = px.scatter(df,title='Coffee intake(in ml) and sleep hours',x='Coffee in ml',y='sleep in hours')
    plot_figure.show()
def getDataSource(data_path):
    coffeeIntake = []
    sleepHours = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            coffeeIntake.append(float(row['Coffee in ml']))
            sleepHours.append(float(row['sleep in hours']))
    return {'x':coffeeIntake,'y':sleepHours}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between coffee intake and sleep hors is : ',correlation[0,1])
def Setup():
    data_path = 'CoffeeVsSleep.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
Setup()
