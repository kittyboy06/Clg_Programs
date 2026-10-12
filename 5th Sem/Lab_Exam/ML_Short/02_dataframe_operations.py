import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 25, 22, 28, 24],
    'Salary': [50000.0, 75000.0, 68000.0, 82000.0, 52000.0],
    'FullTime': [True, True, False, True, False]
})

print("DataFrame:\n", df)
print("\nRetrieved Column (Salary):\n", df['Salary'])
print("\nSummary Statistics:\n", df.describe())
print("\nMean:\n", df[['Age', 'Salary']].mean())
print("\nStd Dev:\n", df[['Age', 'Salary']].std())
print(f"\nSalary - Min: {df['Salary'].min()}, Max: {df['Salary'].max()}")

plt.bar(df['Name'], df['Salary'])
plt.title('Employee Salary')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()
