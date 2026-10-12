# Machine Learning Lab Exam - Complete Program Guide (Short & Exam-Ready)

---

## Experiment 1: Matrix Operations using NumPy
**Aim:** To perform matrix addition, subtraction, multiplication, inversion, transpose, row/column/matrix min & max, trace, and rank using NumPy.

### Algorithm:
1. Import `numpy as np`.
2. Define two 3x3 matrices `A` and `B`.
3. Compute and print addition (`A + B`), subtraction (`A - B`), and matrix multiplication (`A @ B`).
4. Compute inverse using `np.linalg.inv(A)` and transpose using `A.T`.
5. Compute row-wise min/max (`axis=1`), column-wise min/max (`axis=0`), and matrix-level min/max.
6. Compute trace using `np.trace(A)` and rank using `np.linalg.matrix_rank(A)`.

### Code (`01_matrix_operations.py`):
```python
import numpy as np

A = np.array([[4, 7, 2], [3, 6, 1], [2, 5, 8]])
B = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Multiplication:\n", A @ B)
print("Inverse of A:\n", np.linalg.inv(A))
print("Transpose of A:\n", A.T)
print("Row Min:", A.min(axis=1), "| Row Max:", A.max(axis=1))
print("Col Min:", A.min(axis=0), "| Col Max:", A.max(axis=0))
print("Matrix Min:", A.min(), "| Matrix Max:", A.max())
print("Trace of A:", np.trace(A))
print("Rank of A:", np.linalg.matrix_rank(A))
```

---

## Experiment 2: DataFrame Operations using Pandas
**Aim:** To create a DataFrame with at least 5 observations and multiple data types, retrieve columns, compute summary statistics, mean, standard deviation, min/max, and plot a graph.

### Algorithm:
1. Import `pandas as pd` and `matplotlib.pyplot as plt`.
2. Construct a dictionary with >= 5 records across different datatypes (string, integer, float, boolean) and convert to `pd.DataFrame`.
3. Retrieve a specific column using indexing (e.g., `df['Salary']`).
4. Display summary statistics with `df.describe()`, mean with `.mean()`, std with `.std()`, and min/max.
5. Plot a bar graph using `plt.bar()` and display with `plt.show()`.

### Code (`02_dataframe_operations.py`):
```python
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
```

---

## Experiment 3: Simple Linear Regression
**Aim:** To implement Linear Regression on house price dataset, compute Mean Squared Error (MSE), and visualize the regression line against actual data.

### Algorithm:
1. Load dataset using `pd.read_csv()`.
2. Separate feature `X` (`SquareFeet`) and target `y` (`Price`).
3. Split data into train and test sets using `train_test_split()`.
4. Train `LinearRegression().fit(X_train, y_train)` and predict on test set.
5. Compute and print MSE using `mean_squared_error(y_test, y_pred)`.
6. Plot test scatter points and regression line using `plt.scatter()` and `plt.plot()`.

### Code (`03_linear_regression.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('datasets/house_prices.csv')
X, y = df[['SquareFeet']], df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.title('Linear Regression - House Prices')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.show()
```

---

## Experiment 4: Non-linear (Polynomial) Regression
**Aim:** To implement Non-linear Regression using polynomial features on house prices dataset, compute MSE, and visualize the curve fit.

### Algorithm:
1. Load dataset and split into train and test sets.
2. Initialize `PolynomialFeatures(degree=2)`.
3. Fit `LinearRegression` on transformed training features `poly.fit_transform(X_train)`.
4. Predict on transformed test set `poly.transform(X_test)` and compute MSE.
5. Sort test data indices and plot non-linear curve.

### Code (`04_nonlinear_regression.py`):
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('datasets/house_prices.csv')
X, y = df[['SquareFeet']], df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

poly = PolynomialFeatures(degree=2)
model = LinearRegression().fit(poly.fit_transform(X_train), y_train)
y_pred = model.predict(poly.transform(X_test))

print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))

# Sort test inputs to display smooth non-linear curve
idx = np.argsort(X_test.values.flatten())
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test.values[idx], y_pred[idx], color='red', label='Polynomial Fit')
plt.title('Non-linear Regression - House Prices')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.show()
```

---

## Experiment 5: Logistic Regression Classifier
**Aim:** To implement Logistic Regression for diabetes diagnosis, compute classification accuracy, display confusion matrix, and visualize heatmap.

### Algorithm:
1. Load dataset `diabetes.csv`.
2. Extract features `X` and target `y` (`Outcome`).
3. Split into train and test sets (80-20 split).
4. Train `LogisticRegression(max_iter=1000).fit(X_train, y_train)`.
5. Predict test samples, compute `accuracy_score` and `confusion_matrix`.
6. Visualize confusion matrix using `sns.heatmap()`.

### Code (`05_logistic_regression.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/diabetes.csv')
X, y = df.drop(columns=['Outcome']), df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Logistic Regression Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
```

---

## Experiment 6: Naive Bayes Classifier
**Aim:** To implement Gaussian Naive Bayes classifier on the Iris dataset, compute accuracy, display confusion matrix, and visualize performance.

### Algorithm:
1. Load `iris.csv` and separate features `X` and target `y` (`species`).
2. Split data into train and test partitions.
3. Train `GaussianNB().fit(X_train, y_train)`.
4. Compute accuracy using `accuracy_score()` and confusion matrix with `confusion_matrix()`.
5. Visualize confusion matrix heatmap with class labels using Seaborn.

### Code (`06_naive_bayes.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/iris.csv')
X, y = df.drop(columns=['species']), df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB().fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=model.classes_, yticklabels=model.classes_)
plt.title('Naive Bayes Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
```

---

## Experiment 7: Support Vector Machine (SVM) Classifier
**Aim:** To implement SVM algorithm on diabetes dataset, print both correct and wrong predictions, display confusion matrix, and visualize heatmap.

### Algorithm:
1. Load diabetes dataset, split into train and test sets.
2. Train `SVC(kernel='linear').fit(X_train, y_train)`.
3. Predict test labels.
4. Extract and print correct predictions (`a == p`) and wrong predictions (`a != p`) using list comprehension.
5. Compute accuracy, confusion matrix, and plot heatmap.

### Code (`07_svm_classifier.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/diabetes.csv')
X, y = df.drop(columns=['Outcome']), df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear').fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print correct and wrong predictions
print("Correct Predictions (first 5):", [(a, p) for a, p in zip(y_test, y_pred) if a == p][:5])
print("Wrong Predictions:", [(a, p) for a, p in zip(y_test, y_pred) if a != p])

print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges')
plt.title('SVM Classifier Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
```

---

## Experiment 8: Linear vs Non-linear Regression Comparison
**Aim:** To evaluate and visualize the comparative performance of Linear and Non-linear Regression algorithms on house price prediction.

### Algorithm:
1. Load dataset, split into train and test sets.
2. Fit standard Linear Regression and compute MSE.
3. Fit Polynomial Regression (degree 2) and compute MSE.
4. Print both MSE values for numerical comparison.
5. Plot scatter data along with both fitted regression curves on a single plot.

### Code (`08_linear_vs_nonlinear_regression.py`):
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('datasets/house_prices.csv')
X, y = df[['SquareFeet']], df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Linear Regression
lr = LinearRegression().fit(X_train, y_train)
y_lr = lr.predict(X_test)

# 2. Non-linear (Polynomial) Regression
poly = PolynomialFeatures(degree=2)
nlr = LinearRegression().fit(poly.fit_transform(X_train), y_train)
y_nlr = nlr.predict(poly.transform(X_test))

print("Linear Regression MSE:", mean_squared_error(y_test, y_lr))
print("Non-linear Regression MSE:", mean_squared_error(y_test, y_nlr))

# 3. Visualization
idx = np.argsort(X_test.values.flatten())
plt.scatter(X_test, y_test, color='gray', label='Actual Data')
plt.plot(X_test, y_lr, color='blue', label='Linear')
plt.plot(X_test.values[idx], y_nlr[idx], color='red', label='Non-linear (Degree 2)')
plt.title('Linear vs Non-linear Regression')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.show()
```

---

## Experiment 9: Naive Bayes vs SVM Comparison
**Aim:** To evaluate and visualize the performance of Naive Bayes and Support Vector Machine on Iris dataset using side-by-side confusion matrices.

### Algorithm:
1. Load `iris.csv` and train-test split.
2. Train `GaussianNB()` and `SVC(kernel='linear')`.
3. Predict test labels for both models and print respective accuracies.
4. Create a 1x2 subplot with `plt.subplots(1, 2)`.
5. Plot confusion matrices side-by-side using Seaborn.

### Code (`09_naive_bayes_vs_svm.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/iris.csv')
X, y = df.drop(columns=['species']), df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_pred = GaussianNB().fit(X_train, y_train).predict(X_test)
svm_pred = SVC(kernel='linear').fit(X_train, y_train).predict(X_test)

print(f"Naive Bayes Accuracy: {accuracy_score(y_test, nb_pred) * 100:.2f}%")
print(f"SVM Accuracy:         {accuracy_score(y_test, svm_pred) * 100:.2f}%")

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.heatmap(confusion_matrix(y_test, nb_pred), annot=True, fmt='d', cmap='Greens', ax=axes[0])
sns.heatmap(confusion_matrix(y_test, svm_pred), annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[0].set_title('Naive Bayes')
axes[1].set_title('SVM')
plt.tight_layout()
plt.show()
```

---

## Experiment 10: Logistic Regression vs Naive Bayes Comparison
**Aim:** To evaluate and compare the classification performance of Logistic Regression and Naive Bayes on diabetes diagnosis.

### Algorithm:
1. Load `diabetes.csv` and split into train and test sets.
2. Fit `LogisticRegression(max_iter=1000)` and predict.
3. Fit `GaussianNB()` and predict.
4. Calculate and compare test accuracy.
5. Display side-by-side confusion matrices using subplots.

### Code (`10_logistic_regression_vs_naive_bayes.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/diabetes.csv')
X, y = df.drop(columns=['Outcome']), df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_pred = LogisticRegression(max_iter=1000).fit(X_train, y_train).predict(X_test)
nb_pred = GaussianNB().fit(X_train, y_train).predict(X_test)

print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_pred) * 100:.2f}%")
print(f"Naive Bayes Accuracy:         {accuracy_score(y_test, nb_pred) * 100:.2f}%")

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, fmt='d', cmap='Blues', ax=axes[0])
sns.heatmap(confusion_matrix(y_test, nb_pred), annot=True, fmt='d', cmap='Greens', ax=axes[1])
axes[0].set_title('Logistic Regression')
axes[1].set_title('Naive Bayes')
plt.tight_layout()
plt.show()
```

---

## Experiment 11: k-Nearest Neighbors (k-NN) Classifier
**Aim:** To implement k-Nearest Neighbors on Iris dataset, classify test samples, and print both correct and wrong predictions.

### Algorithm:
1. Load dataset `iris.csv` and train-test split.
2. Train `KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)`.
3. Predict test samples.
4. Print correct and wrong predictions via list comprehension.
5. Print accuracy and visualize confusion matrix heatmap.

### Code (`11_knn_classifier.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('datasets/iris.csv')
X, y = df.drop(columns=['species']), df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print correct and wrong predictions
print("Correct Predictions (first 5):", [(a, p) for a, p in zip(y_test, y_pred) if a == p][:5])
print("Wrong Predictions:", [(a, p) for a, p in zip(y_test, y_pred) if a != p])

print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=model.classes_, yticklabels=model.classes_)
plt.title('k-NN Confusion Matrix (k=3)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
```

---

## Experiment 12: K-Means Clustering
**Aim:** To implement K-Means clustering on the Mall Customers dataset, determine cluster centroids, and visualize cluster groupings.

### Algorithm:
1. Load `mall_customers.csv`.
2. Extract clustering features (`Annual_Income_k$`, `Spending_Score`).
3. Apply `KMeans(n_clusters=5, random_state=42)` using `.fit_predict(X)`.
4. Display cluster centers (`kmeans.cluster_centers_`) and cluster distribution counts.
5. Scatter plot the customer clusters using cluster colors, and mark centroids with prominent markers.

### Code (`12_kmeans_clustering.py`):
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('datasets/mall_customers.csv')
X = df[['Annual_Income_k$', 'Spending_Score']]

kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print("Cluster Centers:\n", kmeans.cluster_centers_)
print("\nCluster Distribution:\n", df['Cluster'].value_counts().sort_index())

# Visualize clusters and centroids
plt.scatter(X['Annual_Income_k$'], X['Spending_Score'], c=df['Cluster'], cmap='rainbow', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', marker='X', label='Centroids')
plt.title('K-Means Clustering (k=5)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
```
