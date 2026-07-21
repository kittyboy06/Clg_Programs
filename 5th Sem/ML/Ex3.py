import pandas as pd
import numpy as np

data = {'Name': ['Arun', 'Bala', 'Charan', 'Divya','Eswar'],
        'Age': [20, 21, 19, 22, 20],
        'Marks': [85, 90, 78, 88, 95],
        'Attendance': [92, 85, 88, 95, 90]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nMarks column:\n", df['Marks'])
print("\nSummary statistics:\n", df.describe())
print("\nMean:\n", df.mean(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))