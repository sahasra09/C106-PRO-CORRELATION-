import csv
import numpy as np

def getDataSource(data_path):
    hours=[]
    coffee=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            hours.append(float(row['sleep in hours']))
    return {'x':coffee,'y':hours}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print('The correlation of coffee and hours of sleep: ',correlation[0,1])

def main():
    data_path='cups of coffee vs hours of sleep.csv'
    data_source=getDataSource(data_path)
    findCorrelation(data_source)

main()