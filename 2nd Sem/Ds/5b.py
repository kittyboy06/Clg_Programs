import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
pathu = "D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\diabetes.csv"
pathp = "D:\\Clg\\Clg_Programs\\2nd Sem\\Ds\\1.csv"
d1 = pd.read_csv(pathu,header=0)
d2 = pd.read_csv(pathp,header=0)
cn = list(d1.columns)
print("Available columns: ",cn)
x,y = input("Enter two Values:").split()
v1,v2 = d1[x],d1[y]
v3,v4 = d2[x],d2[y]
print("Correlation Coefficient in Dataset 1:",v1.corr(v2))
print("Correlation Coefficient in Dataset 2:",v3.corr(v4))
x1,y1 = d1[[x]],d1[y]
x2,y2 = d2[[x]],d2[y]
x1_train,x1_test,y1_train,y1_test = train_test_split(x1,y1,test_size=0.2,random_state=42)
x2_train,x2_test,y2_train,y2_test = train_test_split(x2,y2,test_size=0.2,random_state=42)
model1 = LinearRegression()
model2 = LinearRegression()
model1.fit(x1_train,y1_train)
model2.fit(x2_train,y2_train)
y1_pred = model1.predict(x1_test)
y2_pred = model2.predict(x2_test)
print("Linear Regression For UCI")
print("R Squared Value for Dataset 1:", model1.score(x1_test,y1_test))
print("Mean Squared Error for Dataset 1:", mean_squared_error(y1_test, y1_pred))
print("Linear Regression For Pima")
print("R Squared Value for Dataset 2:", model2.score(x2_test,y2_test))
print("Mean Squared Error for Dataset 2:", mean_squared_error(y2_test, y2_pred))
print("Linear Regression")
print("Mean Squared Error:",mean_squared_error(y1_test,y1_pred))
print("R Squared Value:",model2.score(y2_test,y2_pred))
leature_Col = ["pregnancies","glucose","bloodpressure","skinthickness"]
w1,w2 = d1[leature_Col],d2[leature_Col]
z1,z2 = d1.outcome,d2.outcome
w1_train,w1_test,z1_train,z1_test = train_test_split(w1,z1,test_size=0.2,random_state=42)
w2_train,w2_test,z2_train,z2_test = train_test_split(w2,z2,test_size=0.2,random_state=42)
vci_md1 = LinearRegression()
pima_md1 = LinearRegression()
vci_md1.fit(w1_train,z1_train)
pima_md1.fit(w2_train,z2_train)
vci_md1.fit(w1_train,z1_train)
pima_md1.fit(w2_train,z2_train)
ypu = vci_md1.predict(w1_test)
ypp = pima_md1.predict(w2_test)
print("Logistic Regression:")
print("Accuracy:",accuracy_score(z1_test,ypu))
print("Precision:",precision_score(z1_test,ypp))
print()
print("Accuracy:",accuracy_score(z2_test,ypp))
print("Precision:",precision_score(z2_test,ypp))