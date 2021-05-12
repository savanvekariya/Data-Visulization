import matplotlib.pyplot as plt 
import numpy as np
import csv
  
method=[]
val=[]
with open('solution_data.csv') as file:
    reader=csv.reader(file,delimiter=',')
    line_count = 0
    for row in reader:
        val.append(row[2])
        method.append(row[1])
del val[0]
del method[0]

print(len(val))
print(len(method))

for i in range(0, len(val)): 
    val[i] = float(val[i])

gen=[]
op=[]
sim=[]
tabu=[]

for i in range(0,len(val)):
    if(method[i]=='|genetic algorithm|'):
        gen.append(val[i])
    if(method[i]=='|optimal|'):
        op.append(val[i])
    if(method[i]=='|simulated annealing|'):
        sim.append(val[i])
    if(method[i]=='|tabu search|'):
        tabu.append(val[i])

my_dic={'genetic algorithm':gen,'optimal':op,'simulated annealing':sim,'tabu search':tabu}

#fig, ax = plt.subplots(nrows=1,ncols=2)
plt.subplot(1,2,1)
plt.boxplot(my_dic.values())
plt.title('Distribution')
#ax.boxplot(my_dic.values())
#ax.set_xticklabels(my_dic.keys())

#plt.title('Distribution of gaps')

# Creating plot

#fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.subplot(1,2,2)
plt.bar(method, val, color ='maroon', 
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")

plt.suptitle('ABCD')
# show plot 
plt.show() 
