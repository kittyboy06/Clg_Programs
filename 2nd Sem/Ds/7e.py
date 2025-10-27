import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the UCI dataset into a DataFrame
path = 'D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)
cols = np.array(df.columns)

# Extract the desired variables for plotting
print("Variables available: \n", cols)
xvar, yvar, zvar = map(int, input("Enter the indices to choose the variables for histogram (separated by spaces): ").split())
#int(input("Enter the index to choose the variables for histogram: ").split())
#variable = data[cols[var]]
x = data[cols[xvar]]
y = data[cols[yvar]]
z = data[cols[zvar]]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel(cols[xvar])
ax.set_ylabel(cols[yvar])
ax.set_zlabel(cols[zvar])
ax.set_title('3D Plot')
plt.show()
