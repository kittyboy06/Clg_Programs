import matplotlib.pyplot as plt

# Read the data from the CSV file
x = [59, 36, 68, 14, 78, 80, 83, 17, 62, 63, 64, 4, 83, 66, 31, 97, 34, 74, 9, 62]
y = [85, 36, 1, 87, 7, 9, 5, 13, 86, 38, 89, 94, 6, 1, 89, 50, 10, 45, 14, 25]
plt.figure(figsize=(8, 5))
plt.scatter(x, y, marker='o', color='b', label='Dataset')
plt.title('Dataset Visualization')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.grid(True)
plt.show()