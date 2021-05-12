import csv
x=[]
y=[]
with open('scatter_data.csv') as file:
    reader=csv.reader(file,delimiter=',')
    line_count = 0
    for row in reader:
        x.append(row[0])
        y.append(row[1])
del y[0]
del x[0]

,color='red',linestyle='dashed'
