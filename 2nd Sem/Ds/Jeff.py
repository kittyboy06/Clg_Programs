import pandas as pd
import numpy as np
from scipy.stats import skew , kurtosis
path1 = "D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv"
path2 = "D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\1.csv"
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)
print("Desctiptive Analysis",data1.describe())
print("Desctiptive Analysis2",data2.describe())
x = input("Enter a Column name")
print("Average:")
print("UCI:",data1.mean())
print("Pima:",data2.mean())
print("Median:")
print("Pima:",data2.median())
print("Skewness:")
print("UCI:",data1.skew())
print("Pima:",data2.skew())
print("Kurtosis:")
print("UCI:",data1.kurtosis())
print("Pima:",data2.kurtosis())