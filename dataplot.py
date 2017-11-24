import matplotlib.pyplot as plt
import csv
x = []
y = []

with open('/home/dipu/Desktop/example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[1]))
        y.append((row[10]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('date')
plt.ylabel('Load')
plt.xticks(rotation = 90)
plt.title('Performance Analyser')
plt.legend()
plt.show()
