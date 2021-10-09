import csv
import numpy as np

def getDataSource(data_path):
    marks=[]
    dp=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            dp.append(float(row['Days Present']))
    return {'x':dp,'y':marks}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print('The correlation of marks in percentage and days present is: ',correlation[0,1])

def main():
    data_path='Student Marks vs Days Present.csv'
    data_source=getDataSource(data_path)
    findCorrelation(data_source)

main()