# Program 07: Support Vector Machine (SVM) Classifier
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load dataset
df = pd.read_csv('datasets/diabetes.csv')
X = df.drop(columns=['Outcome'])
y = df['Outcome']

# 2. Split dataset and scale features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Train SVM model
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)
y_actual = y_test.values

# 5. Print both correct and wrong predictions
print("=== Prediction Analysis ===")
correct = []
wrong = []
for i in range(len(y_actual)):
    if y_actual[i] == y_pred[i]:
        correct.append(f"Sample {i}: Actual={y_actual[i]}, Predicted={y_pred[i]}")
    else:
        wrong.append(f"Sample {i}: Actual={y_actual[i]}, Predicted={y_pred[i]}")

print(f"\nCorrect Predictions ({len(correct)}):")
for item in correct[:5]:  # print first 5 as samples
    print(" ", item)
print(f" ... and {len(correct) - 5} more correct predictions.")

print(f"\nWrong Predictions ({len(wrong)}):")
for item in wrong:
    print(" ", item)

# 6. Accuracy and Confusion Matrix
acc = accuracy_score(y_actual, y_pred)
cm = confusion_matrix(y_actual, y_pred)
print(f"\nSVM Accuracy: {acc * 100:.2f}%")
print("Confusion Matrix:\n", cm)

# 7. Visualize performance evaluation
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'])
plt.title('Confusion Matrix - Support Vector Machine')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.tight_layout()
plt.savefig('outputs/07_svm_classifier.png')
print("\nPlot saved as outputs/07_svm_classifier.png")
plt.show()
