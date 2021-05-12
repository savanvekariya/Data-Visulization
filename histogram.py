import matplotlib.pyplot as plt
import csv


grades=[0,60,70,80,90,100]

marks=[]
with open('student_grades1.csv') as file:
    reader=csv.reader(file,delimiter=',')
    line_count = 0
    for row in reader:
        marks.append(row[1])
       
del marks[0]
for i in range(0, len(marks)): 
    marks[i] = float(marks[i])
    
print(marks)

plt.hist(marks,bins=grades,rwidth=0.8,label='a')

plt.yticks(range(0,50,5))
plt.xticks([0,60,70,80,90,100])



plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Count')
plt.show()
