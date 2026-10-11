"""
Dataset Generator Script
Generates sample datasets for all lab exam programs:
1. iris.csv
2. house_prices.csv
3. diabetes.csv
4. heart_disease.csv
5. mall_customers.csv
"""

import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

os.makedirs('datasets', exist_ok=True)

# 1. Iris Dataset
iris = load_iris(as_frame=True)
df_iris = iris.frame
df_iris['species'] = df_iris['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
df_iris.drop(columns=['target'], inplace=True)
df_iris.columns = [c.replace(' (cm)', '').replace(' ', '_') for c in df_iris.columns]
df_iris.to_csv('datasets/iris.csv', index=False)
print("Created datasets/iris.csv:", df_iris.shape)

# 2. House Prices Dataset
np.random.seed(42)
n_houses = 200
sqft = np.random.uniform(600, 3500, n_houses)
bedrooms = np.random.choice([1, 2, 3, 4, 5], size=n_houses, p=[0.1, 0.25, 0.4, 0.2, 0.05])
bathrooms = np.clip(np.round(bedrooms * 0.75 + np.random.normal(0, 0.5, n_houses)), 1, 4).astype(int)
age = np.random.uniform(0, 40, n_houses)
distance_to_city = np.random.uniform(1, 30, n_houses)
price = (
    50000 
    + 180 * sqft 
    + 0.02 * (sqft ** 1.8) 
    + 25000 * bedrooms 
    + 15000 * bathrooms 
    - 1200 * age 
    - 2500 * distance_to_city 
    + np.random.normal(0, 25000, n_houses)
)
price = np.round(np.clip(price, 80000, 1200000), -2)

df_house = pd.DataFrame({
    'SquareFeet': np.round(sqft, 1),
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'Age': np.round(age, 1),
    'DistanceToCity_km': np.round(distance_to_city, 1),
    'Price': price
})
df_house.to_csv('datasets/house_prices.csv', index=False)
print("Created datasets/house_prices.csv:", df_house.shape)

# 3. Diabetes Dataset
np.random.seed(42)
n_patients = 250
pregnancies = np.random.choice(range(12), size=n_patients, p=[0.2, 0.15, 0.15, 0.15, 0.1, 0.1, 0.05, 0.04, 0.02, 0.02, 0.01, 0.01])
glucose = np.random.normal(120, 30, n_patients).clip(50, 200)
blood_pressure = np.random.normal(72, 12, n_patients).clip(40, 120)
skin_thickness = np.random.normal(25, 10, n_patients).clip(10, 60)
insulin = np.random.normal(100, 60, n_patients).clip(15, 400)
bmi = np.random.normal(32, 6, n_patients).clip(18, 55)
dpf = np.random.exponential(0.4, n_patients).clip(0.08, 2.4)
age_diab = np.random.uniform(21, 70, n_patients)
logits = -7.5 + 0.035 * glucose + 0.05 * bmi + 0.03 * age_diab + 0.8 * dpf + 0.1 * pregnancies
prob = 1 / (1 + np.exp(-logits))
outcome = (np.random.uniform(0, 1, n_patients) < prob).astype(int)

df_diabetes = pd.DataFrame({
    'Pregnancies': pregnancies,
    'Glucose': np.round(glucose, 1),
    'BloodPressure': np.round(blood_pressure, 1),
    'SkinThickness': np.round(skin_thickness, 1),
    'Insulin': np.round(insulin, 1),
    'BMI': np.round(bmi, 1),
    'DiabetesPedigreeFunction': np.round(dpf, 3),
    'Age': np.round(age_diab).astype(int),
    'Outcome': outcome
})
df_diabetes.to_csv('datasets/diabetes.csv', index=False)
print("Created datasets/diabetes.csv:", df_diabetes.shape)

# 4. Heart Disease Dataset
np.random.seed(42)
n_heart = 250
age_heart = np.random.randint(29, 77, n_heart)
sex = np.random.choice([0, 1], size=n_heart, p=[0.35, 0.65])
cp = np.random.choice([0, 1, 2, 3], size=n_heart, p=[0.48, 0.17, 0.28, 0.07])
trestbps = np.random.normal(131, 17, n_heart).clip(94, 200).astype(int)
chol = np.random.normal(246, 51, n_heart).clip(126, 450).astype(int)
fbs = (np.random.uniform(0, 1, n_heart) < 0.15).astype(int)
restecg = np.random.choice([0, 1, 2], size=n_heart, p=[0.49, 0.48, 0.03])
thalach = (200 - 0.8 * age_heart + np.random.normal(0, 15, n_heart)).clip(71, 202).astype(int)
exang = np.random.choice([0, 1], size=n_heart, p=[0.68, 0.32])
oldpeak = np.random.exponential(1.0, n_heart).clip(0, 6.2).round(1)
z = -2.0 + 0.04 * age_heart + 0.6 * sex + 0.8 * cp - 0.02 * thalach + 1.2 * exang + 0.7 * oldpeak
prob_heart = 1 / (1 + np.exp(-z))
target_heart = (np.random.uniform(0, 1, n_heart) < prob_heart).astype(int)

df_heart = pd.DataFrame({
    'age': age_heart,
    'sex': sex,
    'chest_pain_type': cp,
    'resting_bp': trestbps,
    'cholesterol': chol,
    'fasting_blood_sugar': fbs,
    'resting_ecg': restecg,
    'max_heart_rate': thalach,
    'exercise_angina': exang,
    'st_depression': oldpeak,
    'target': target_heart
})
df_heart.to_csv('datasets/heart_disease.csv', index=False)
print("Created datasets/heart_disease.csv:", df_heart.shape)

# 5. Mall Customers Dataset
np.random.seed(42)
n_cust = 200
cluster_centers = [
    (25, 80), (25, 20), (55, 50), (85, 85), (85, 15)
]
incomes, spendings = [], []
for i in range(n_cust):
    cx, cy = cluster_centers[i % 5]
    incomes.append(int(np.clip(np.random.normal(cx, 8), 15, 135)))
    spendings.append(int(np.clip(np.random.normal(cy, 10), 1, 99)))

df_mall = pd.DataFrame({
    'CustomerID': range(1, n_cust + 1),
    'Gender': np.random.choice(['Male', 'Female'], size=n_cust, p=[0.44, 0.56]),
    'Age': np.random.randint(18, 70, n_cust),
    'Annual_Income_k$': incomes,
    'Spending_Score': spendings
})
df_mall.to_csv('datasets/mall_customers.csv', index=False)
print("Created datasets/mall_customers.csv:", df_mall.shape)
