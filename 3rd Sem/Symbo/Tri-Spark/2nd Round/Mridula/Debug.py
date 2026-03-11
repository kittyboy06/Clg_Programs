# Fillers Program – Students Marks Visualization

import matplotlib.pyplot as plt
import statistics

students = ["Arun", "Bala", "Chitra", "Deepa", "Eshan"]
marks1 = [85, 78, 92, 60, 75]
marks2 = [80, 82, 88, 70, 65]
marks3 = [90, 76, 85, 55, 72]

totals = []
averages = []
grades = []

for i in range(len(students)):
    total = marks3[i] + marks1[i] + marks2[i]
    totals.append(total)

    avg = total / 3              
    averages.append(avg)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"
    grades.append(grade)

print("Students:", students)
print("Totals:", totals)
print("Averages:", averages)
print("Grades:", grades)

# Plotting
plt.figure(figsize=(10,6))
plt.bar(averages, students, color="skyblue", label="Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Students")
plt.title("Student Average Marks")
plt.legend()
plt.grid(False)                                             
plt.show()