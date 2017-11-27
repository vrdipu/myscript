import matplotlib.pyplot as plt
import csv
x = []
y = []

with open('/home/dipu/Desktop/example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[1]))
        y.append(int(row[0]))

plt.bar(x,y, label='Loaded from file!')
plt.xlabel('Filesystem')
plt.ylabel('Usage')
plt.xticks(rotation = 90)
plt.title('Performance Analyser')
plt.legend()
plt.show()





# df -Ph |awk '{print $5,","$6}' |tr "%" " "
