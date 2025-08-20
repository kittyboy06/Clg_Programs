import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score
pathu = "C:\\Users\\Admin\\Desktop\\Kittyboy\\Clg_Programs\\2nd Sem\\Ds\\1.csv"
pathp = "C:\\Users\\Admin\\Desktop\\Kittyboy\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv"
dd = pd.read_csv(pathu, header=0)
dd1 = pd.read_csv(pathp, header=0)
cn = list(dd.columns)
print("Available Columns:", cn)
x, y = input("Enter 2 values: ").split()
v1, v2 = dd[x], dd[y]
v3, v4 = dd1[x], dd1[y]
print("Correlation coefficient UCI:\t", v1.corr(v2))
print("Correlation coefficient PIMA:\t", v3.corr(v4))
x1, y1 = dd[[x]], dd[[y]]
x2, y2 = dd1[[x]], dd1[[y]]
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.2, random_state=42)
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size=0.2, random_state=42)
uci_md = LinearRegression()
pima_md = LinearRegression()
uci_md.fit(x1_train, y1_train)
pima_md.fit(x2_train, y2_train)
ypu = uci_md.predict(x1_test)
ypp = pima_md.predict(x2_test)
print("Linear Regression (UCI)")
print("Mean Squared:", mean_squared_error(y1_test, ypu))
print("R squared:", r2_score(y1_test, ypu))
print("\nLinear Regression (PIMA)")
print("Mean Squared:", mean_squared_error(y2_test, ypp))
print("R squared:", r2_score(y2_test, ypp))
Feature_col = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness"]
w1, w2 = dd[Feature_col], dd1[Feature_col]
z1, z2 = dd["Outcome"], dd1["Outcome"]
w1_train, w1_test, z1_train, z1_test = train_test_split(w1, z1, test_size=0.2, random_state=16)
w2_train, w2_test, z2_train, z2_test = train_test_split(w2, z2, test_size=0.4, random_state=16)
uci_md1 = LogisticRegression(max_iter=1000)
pima_md1 = LogisticRegression(max_iter=1000)
uci_md1.fit(w1_train, z1_train)
pima_md1.fit(w2_train, z2_train)
ypu1 = uci_md1.predict(w1_test)
ypp1 = pima_md1.predict(w2_test)
print("\nLogistic Regression (UCI):")
print("Accuracy:", accuracy_score(z1_test, ypu1))
print("Precision:", precision_score(z1_test, ypu1))
print("Recall value:", recall_score(z1_test, ypu1))
print("\nLogistic Regression (PIMA):")
print("Accuracy:", accuracy_score(z2_test, ypp1))
print("Precision:", precision_score(z2_test, ypp1))
print("Recall value:", recall_score(z2_test, ypp1))