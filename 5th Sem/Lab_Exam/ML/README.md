# Python Machine Learning & Data Science Lab Exam Solutions (Set 25-26)

This repository contains clean, concise, and easy-to-understand Python programs covering all questions from the **Lab Exam Question Set (2025–2026)**.

All programs are kept **simple and short** (around 25–40 lines each), making them ideal for lab exams, viva preparation, and pair programming.

---

## 📁 Repository Structure

```
├── datasets/
│   ├── diabetes.csv                            # Binary classification (Diabetes diagnosis)
│   ├── heart_disease.csv                       # Binary classification (Heart disease diagnosis)
│   ├── house_prices.csv                        # Regression (Square feet to Price)
│   ├── iris.csv                                # Multi-class classification (Iris flower species)
│   ├── mall_customers.csv                      # Clustering (Income & Spending score)
│   └── generate_datasets.py                    # Script to regenerate datasets if needed
├── outputs/                                    # Generated performance plots and charts
├── 01_matrix_operations.py                     # Matrix addition, inverse, trace, rank, etc.
├── 02_dataframe_operations.py                  # Pandas DataFrame statistics, slicing & plot
├── 03_linear_regression.py                     # Simple Linear Regression (House prices)
├── 04_nonlinear_regression.py                  # Polynomial (Non-linear) Regression
├── 05_logistic_regression.py                   # Logistic Regression (Diabetes diagnosis)
├── 06_naive_bayes.py                           # Gaussian Naive Bayes (Iris species)
├── 07_svm_classifier.py                        # Support Vector Machine (Shows correct & wrong predictions)
├── 08_linear_vs_nonlinear_regression.py        # Comparative evaluation: Linear vs Non-linear
├── 09_naive_bayes_vs_svm.py                    # Comparative evaluation: Naive Bayes vs SVM
├── 10_logistic_regression_vs_naive_bayes.py    # Comparative evaluation: Logistic Regression vs Naive Bayes
├── 11_knn_classifier.py                        # k-Nearest Neighbors (Shows correct & wrong predictions)
├── 12_kmeans_clustering.py                     # K-Means Clustering (Customer segmentation)
├── run_all.py                                  # Sequentially run all 12 programs
├── requirements.txt                            # Required Python libraries
└── README.md                                   # Documentation
```

---

## 📋 Program Mapping & Lab Exam Questions

| No. | File | Lab Exam Question / Task | Dataset |
|:---:|:---|:---|:---|
| **1** | `01_matrix_operations.py` | Matrix operations: addition, subtraction, multiplication, inverse, transpose, min/max of rows/columns, min/max of matrix, trace, rank. | NumPy arrays |
| **2** | `02_dataframe_operations.py` | Create DataFrame with ≥ 5 rows and different datatypes, retrieve column, summarize statistics (`describe`), mean & std, min/max, plot graph. | Pandas DataFrame |
| **3** | `03_linear_regression.py` | Linear Regression for house price prediction (.CSV), compute MSE on test set, visualize performance. | `datasets/house_prices.csv` |
| **4** | `04_nonlinear_regression.py` | Non-linear (Polynomial) Regression for house price prediction (.CSV), compute MSE, visualize performance. | `datasets/house_prices.csv` |
| **5** | `05_logistic_regression.py` | Logistic Regression for diabetes diagnosis (.CSV), compute accuracy, confusion matrix, visualize performance. | `datasets/diabetes.csv` |
| **6** | `06_naive_bayes.py` | Naive Bayesian Classifier for iris species identification (.CSV), compute accuracy, confusion matrix, visualize performance. | `datasets/iris.csv` |
| **7** | `07_svm_classifier.py` | Support Vector Machine (SVM) to classify diabetes diagnosis, print both correct and wrong predictions, display confusion matrix, visualize. | `datasets/diabetes.csv` |
| **8** | `08_linear_vs_nonlinear_regression.py` | Evaluate and visualize performance of Linear vs Non-linear Regression algorithms on house price prediction dataset. | `datasets/house_prices.csv` |
| **9** | `09_naive_bayes_vs_svm.py` | Evaluate and visualize performance of Naive Bayes vs SVM algorithm on Iris dataset. | `datasets/iris.csv` |
| **10** | `10_logistic_regression_vs_naive_bayes.py` | Evaluate and visualize performance of Logistic Regression vs Naive Bayes on diabetes diagnosis dataset. | `datasets/diabetes.csv` |
| **11** | `11_knn_classifier.py` | k-Nearest Neighbors (k-NN) to classify Iris dataset, print both correct and wrong predictions, display confusion matrix, visualize. | `datasets/iris.csv` |
| **12** | `12_kmeans_clustering.py` | K-Means clustering on mall customers dataset, display cluster centers, visualize clusters and centroids. | `datasets/mall_customers.csv` |

---

## 🚀 Getting Started

### 1. Prerequisites & Installation

Clone the repository and install required packages:

```bash
git clone https://github.com/kittyboy06/ML-Lab-Exam-Solutions.git
cd ML-Lab-Exam-Solutions
pip install -r requirements.txt
```

### 2. Run Any Program

Run any individual script with Python:

```bash
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

### 3. Run All Programs

To run all 12 programs sequentially in batch:

```bash
python run_all.py
```

All generated visualization plots are automatically saved into the `outputs/` folder.
