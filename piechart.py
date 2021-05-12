import matplotlib.pyplot as plt
import csv

x=[]
y=[]
with open('piechart.csv') as file:
    reader=csv.reader(file,delimiter=',')
    line_count = 0
    for row in reader:
        x.append(row[0])
        y.append(row[3])
del x[0]
del y[0]

for i in range(0,len(y)):
    y[i]=int(y[i])
    
print(x)
print(y)
plt.pie(y, labels = x,autopct='%1.1f%%')
plt.show()
