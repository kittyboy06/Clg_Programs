import pandas as pd
data = pd.read_csv("D:\\Clg\\Clg_Programs\\2nd Sem\\SEM EXAM\\DS\\iris.csv",header=0)
cn = list(data.columns)
print("Available columns:", cn)
x = input("Enter the first column name for correlation:")
y = input("Enter the second column name for correlation:")
correlation = data[x].corr(data[y])
print(f"Correlation between {x} and {y}: {correlation}")