# Machine Learning Lab Exam - Shortened & Exam-Ready Solutions

This directory contains **ultra-short, exam-optimized versions** of all 12 Machine Learning lab exam programs.

---

## ⚡ Key Improvements & Exam Optimizations

| Program | Topic / Algorithm | Original Lines | Short Lines | Reduction |
|:---:|:---|:---:|:---:|:---:|
| **01** | NumPy Matrix Operations | 35 | **15** | **57%** |
| **02** | Pandas DataFrame Operations | 41 | **20** | **51%** |
| **03** | Linear Regression | 41 | **21** | **49%** |
| **04** | Non-linear (Polynomial) Regression | 51 | **25** | **51%** |
| **05** | Logistic Regression | 39 | **23** | **41%** |
| **06** | Naive Bayes Classifier | 40 | **23** | **43%** |
| **07** | Support Vector Machine (SVM) | 64 | **25** | **61%** |
| **08** | Linear vs Non-linear Comparison | 59 | **29** | **51%** |
| **09** | Naive Bayes vs SVM Comparison | 54 | **25** | **54%** |
| **10** | Logistic Regression vs Naive Bayes | 54 | **25** | **54%** |
| **11** | k-Nearest Neighbors (k-NN) | 64 | **25** | **61%** |
| **12** | K-Means Clustering | 46 | **21** | **54%** |
| **Total** | **All 12 Programs** | **534** | **267** | **~50% average reduction** |

### How these programs are made exam-friendly:
1. **Chained fitting:** `model = LinearRegression().fit(X_train, y_train)` saves initialization boilerplate.
2. **Concise correct/wrong prediction printing:** Uses list comprehension instead of 20+ line iterative loops.
3. **Streamlined imports:** Groups related imports logically.
4. **Direct plotting:** Clean, essential visualization commands without dozens of decorative matplotlib styling parameters.
5. **No loss in question requirements:** Every metric (MSE, accuracy, confusion matrix, min/max, trace, rank, correct/wrong samples) strictly meets the syllabus.

---

## 📁 Directory Structure

```
ML_Short/
├── datasets/                                   # Standalone dataset copies
│   ├── diabetes.csv
│   ├── heart_disease.csv
│   ├── house_prices.csv
│   ├── iris.csv
│   └── mall_customers.csv
├── 01_matrix_operations.py                     # 15 lines
├── 02_dataframe_operations.py                  # 20 lines
├── 03_linear_regression.py                     # 21 lines
├── 04_nonlinear_regression.py                  # 25 lines
├── 05_logistic_regression.py                   # 23 lines
├── 06_naive_bayes.py                           # 23 lines
├── 07_svm_classifier.py                        # 25 lines
├── 08_linear_vs_nonlinear_regression.py        # 29 lines
├── 09_naive_bayes_vs_svm.py                    # 25 lines
├── 10_logistic_regression_vs_naive_bayes.py    # 25 lines
├── 11_knn_classifier.py                        # 25 lines
├── 12_kmeans_clustering.py                     # 21 lines
├── Programs.md                                 # Full lab manual (Aim, Algorithm, Code)
└── README.md                                   # This summary
```

---

## 🚀 How to Run

From inside the `ML_Short` directory:

```bash
cd "5th Sem/Lab_Exam/ML_Short"

# Run any program individually
python 01_matrix_operations.py
python 02_dataframe_operations.py
python 03_linear_regression.py
python 04_nonlinear_regression.py
python 05_logistic_regression.py
python 06_naive_bayes.py
python 07_svm_classifier.py
python 08_linear_vs_nonlinear_regression.py
python 09_naive_bayes_vs_svm.py
python 10_logistic_regression_vs_naive_bayes.py
python 11_knn_classifier.py
python 12_kmeans_clustering.py
```
