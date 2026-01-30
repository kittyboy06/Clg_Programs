import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the UCI dataset into a DataFrame
path = 'D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)
cols = np.array(df.columns)

# Extract the desired variable for plotting
print("Variables available: \n", cols)
var = int(input("Enter the index to choose the variable for histogram: "))
variable = data[cols[var]]

# Plot the histogram
plt.hist(variable, bins=15, edgecolor='black', color='skyblue') # Adjust the number of bins as needed
plt.xlabel(cols[var])
plt.ylabel('Frequency')
plt.title('Histogram')

plt.show()
