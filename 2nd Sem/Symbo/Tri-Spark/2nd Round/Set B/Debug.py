import csv
import matplotlib.pyplot as plt

# Read the data from the CSV file
x = []
y = []
z = []
with open(r'C:\Users\PC-107\Desktop\Afsal\Clg_Programs\2nd Sem\Symbo\Tri-Spark\2nd Round\Set B\Debug.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

# Plot the data
plt.figure(figsize=(8, 5))
plt.scatter(x, y, z, marker='o', color='b', label='Dataset')
plt.title('Dataset Visualization')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.zlabel('Z Values')
plt.legend()
plt.grid(True)
plt.show()