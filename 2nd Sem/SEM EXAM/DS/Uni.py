import pandas as pd
from scipy.stats import skew, kurtosis
data =  pd.read_csv("D:\\Clg\\Clg_Programs\\2nd Sem\\SEM EXAM\\DS\\iris.csv")
print("Descriptive Statistics:\n", data.describe(), "\n")
x = input("Enter the column name:")
print("Average:", data[x].mean())
print("Frequency Distribution:\n", data[x].value_counts(), "\n")
print("Mean:", data[x].mean())
print("Median:", data[x].median())
print("Mode:", data[x].mode()[0])
print("Variance:", data[x].var())
print("Standard Deviation:", data[x].std())
print("Skewness:", skew(data[x]))
print("Kurtosis:", kurtosis(data[x]))