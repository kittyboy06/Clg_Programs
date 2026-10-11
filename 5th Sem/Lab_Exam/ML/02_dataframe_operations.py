# Program 02: DataFrame Operations using Pandas
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create DataFrame with >= 5 observations and different data types
data = {
    'EmpID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [50000.0, 75000.0, 68000.0, 82000.0, 52000.0, 71000.0],
    'Experience_Years': [2, 5, 4, 7, 2, 4],
    'Is_FullTime': [True, True, False, True, False, True]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Retrieve a particular column
print("\nRetrieved 'Salary' Column:\n", df['Salary'])

# 3. Summarize and observe statistics
print("\nDataFrame Summary & Statistics:\n", df.describe())

# 4. Mean and Standard Deviation of numeric columns
print("\nMean of Numeric Columns:\n", df[['Salary', 'Experience_Years']].mean())
print("\nStandard Deviation of Numeric Columns:\n", df[['Salary', 'Experience_Years']].std())

# 5. Maximum and Minimum of a particular column
print("\nSalary - Maximum:", df['Salary'].max())
print("Salary - Minimum:", df['Salary'].min())

# 6. Plot a graph for any column
plt.figure(figsize=(6, 4))
plt.bar(df['Name'], df['Salary'], color='skyblue', edgecolor='black')
plt.title('Employee Salary Distribution')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('outputs/02_dataframe_plot.png')
print("\nGraph saved as outputs/02_dataframe_plot.png")
plt.show()
