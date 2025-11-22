import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
diabetes_uci = pd.read_csv("D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\1.csv")
diabetes_pima = pd.read_csv("D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv")
X1, Y1 = diabetes_uci[['Glucose', 'BMI', 'BloodPressure']], diabetes_uci['Outcome']
X2, Y2 = diabetes_pima[['Glucose', 'BMI', 'BloodPressure']], diabetes_pima['Outcome']
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X1, Y1, test_size=0.2, random_state=42)
X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X2, Y2, test_size=0.2, random_state=42)
model_uci = LinearRegression()
model_pima = LinearRegression()
model_uci.fit(X_train1, Y_train1)
model_pima.fit(X_train2, Y_train2)
Y_pred_uci = model_uci.predict(X_test1)
Y_pred_pima = model_pima.predict(X_test2)
mse_uci = mean_squared_error(Y_test1, Y_pred_uci)
r2_uci = r2_score(Y_test1, Y_pred_uci)
mse_pima = mean_squared_error(Y_test2, Y_pred_pima)
r2_pima = r2_score(Y_test2, Y_pred_pima)
print("Linear Regression Evaluation Metrics for UCI Diabetes Dataset:")
print("Mean Squared Error (MSE):", mse_uci)
print("R-squared:", r2_uci)
print("Linear Regression Evaluation Metrics for Pima Diabetes Dataset:")
print("Mean Squared Error (MSE):", mse_pima)
print("R-squared:", r2_pima)
evaluation_table = pd.DataFrame({
    'Dataset': ['UCI', 'PIMA'],
    'MSE': [mse_uci, mse_pima],
    'R-squared': [r2_uci, r2_pima]
})
print(evaluation_table)
datasets = ['UCI', 'PIMA']
mse_scores = [mse_uci, mse_pima]
r2_scores = [r2_uci, r2_pima]
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(datasets, mse_scores, color='red')
plt.xlabel('Dataset')
plt.ylabel('Mean Squared Error')
plt.title('Comparison of MSE Scores')
plt.subplot(1, 2, 2)
plt.bar(datasets, r2_scores, color='green')
plt.xlabel('Dataset')
plt.ylabel('R-squared')
plt.title('Comparison of R-squared Scores')
plt.tight_layout()
plt.show()