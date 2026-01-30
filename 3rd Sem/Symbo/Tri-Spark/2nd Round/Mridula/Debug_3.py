import matplotlib.pyplot as plt
import statistics

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature_celsius = [30, 32, 31, 29, 35, 36, 34]

temperature_fahrenheit = []

for c in temperature_celsius:
    f = c * 9/5 + 32
    temperature_fahrenheit.append(f)

highest = max(temperature_celsius)
lowest = min(temperature_celsius)
avg_temp = sum(temperature_celsius)/len(temperature_celsius)

print("Days:", days)
print("Celsius:", temperature_celsius)
print("Fahrenheit:", temperature_fahrenheit)
print("Highest (C):", highest)
print("Lowest (C):", lowest)
print("Average (C):", avg_temp)

plt.plot(days, temperature_celsius, marker="o", linestyle="-", color="red", label="Celsius")
plt.plot(days, temperature_fahrenheit, marker="s", linestyle="--", color="blue", label="Fahrenheit")

plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Weekly Temperature Report")
plt.legend()  
plt.grid(True)
plt.show()