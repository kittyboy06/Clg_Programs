import csv
import random

data = []
def generate_2d_data():
    for _ in range(20):
        col1 = random.randint(0, 100)  
        col2 = random.randint(0, 100)  
        data.append([col1, col2])
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
def generate_3d_data():
    for _ in range(20):
        col1 = random.randint(0, 100)  
        col2 = random.randint(0, 100)  
        col3 = random.randint(0, 100)  
        data.append([col1, col2, col3])
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
def generate_4d_data():
    for _ in range(20):
        col1 = random.randint(0, 100)  
        col2 = random.randint(0, 100)
        col3 = random.randint(0, 100)
        col4 = random.randint(0, 100)
        data.append([col1, col2, col3, col4])
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

print("1. Generate 2D data\n2. Generate 3D data\n3. Generate 4D data")
choice = int(input("Enter your choice (1, 2, or 3): "))
if choice == 1:
    generate_2d_data()
elif choice == 2:
    generate_3d_data()
elif choice == 3:
    generate_4d_data()