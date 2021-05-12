import matplotlib.pyplot as plt
import csv
x=[]
y=[]
a=[]
b=[]
with open('scatter_data.csv') as file:
    reader=csv.reader(file,delimiter=',')
    line_count = 0
    for row in reader:
        x.append(row[0])
        y.append(row[1])
del x[0]
del y[0]


for i in range(0,len(x)):
    a.append(x[i])

a.sort()

for i in range(0,len(x)):
    idx=x.index(a[i])
    b.append(y[idx])

for i in range(0,len(a)):
    a[i]=float(a[i])
    b[i]=float(b[i])
    
print(a)
print(b)

plt.scatter(a,b,label="observation",color="green",marker="^")

mn=float(min(a))
mx=float(max(a))

x_values = [mn, mx]
y_values = [max(b), max(b)]
print(x_values)
print(y_values)
plt.plot(x_values, y_values, color='red', marker='None', linestyle='dashed',label='extream x points')

plt.xlabel('x[inches]')
plt.ylabel('y[inches]')
plt.title('Weight Mesurements')
plt.legend()
plt.show()




