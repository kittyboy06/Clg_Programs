import csv
import matplotlib.pyplot as plt

x = []
with open(r'C:\Users\PC-107\Desktop\Afsal\Clg_Programs\2nd Sem\Symbo\Tri-Spark\2nd Round\Set A\filler.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if present
    for row in reader:
        x.append(float(row[0]))

plt.hist(__, bins=10, color='___', edgecolor = '_____')
plt.title('Dataset Visualization')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()