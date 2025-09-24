import csv
import matplotlib.pyplot as plt

# Read the data from the CSV file
x = []
y = []
with open(r'D:\Clg\Clg_Programs\2nd Sem\Symbo\Tri-Spark\2nd Round\Demo\plot1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if present
    for row in reader:
        x.append(float(row[0]))  # First column
        y.append(float(row[1]))  # Second column

# Plot the data
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='b', label='Dataset')
plt.title('Dataset Visualization')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.grid(True)
plt.show()