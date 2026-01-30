import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
rainfall_mm = [5.2, 0.0, 3.1, 7.8, 2.4, 0.0, 4.5]

# Calculate statistics
total = sum(rainfall_mm)               # Error 1: wrong variable name
minimum = min(rainfall_mm)         # Error 2: undefined function
maximum = max(rainfall_mm)
average = total / len(rainfall_mm)  # Error 3: .count is incorrect

print("Days:", days)
print("Rainfall (mm):", rainfall_mm)
print("Total:", total)
print("Minimum:", minimum)
print("Maximum:", maximum)           # Error 4: wrong variable name
print("Average:", average)               # Error 5: wrong variable name

# Plotting
plt.scatter(days, rainfall_mm, marker='^', color='green')  # Error 6: wrong argument name
plt.plot(days, rainfall_mm, linestyle='-', color='green', label='Rainfall')
plt.title("Weekly Rainfall")
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.grid(True)
plt.show()