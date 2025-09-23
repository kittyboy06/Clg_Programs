import csv
import random

# Generate data
data = []
for _ in range(20):
    col1 = random.randint(0, 100)  # Random integer between 0 and 100
    col2 = random.randint(0, 100)  # Random integer between 0 and 100
    data.append([col1, col2])

# Write to CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
