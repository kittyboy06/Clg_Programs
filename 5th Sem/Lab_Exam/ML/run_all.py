"""
Runner script to execute all 12 Lab Exam programs sequentially.
"""

import subprocess
import sys
import os

scripts = [
    "01_matrix_operations.py",
    "02_dataframe_operations.py",
    "03_linear_regression.py",
    "04_nonlinear_regression.py",
    "05_logistic_regression.py",
    "06_naive_bayes.py",
    "07_svm_classifier.py",
    "08_linear_vs_nonlinear_regression.py",
    "09_naive_bayes_vs_svm.py",
    "10_logistic_regression_vs_naive_bayes.py",
    "11_knn_classifier.py",
    "12_kmeans_clustering.py"
]

def main():
    print("=" * 60)
    print(" EXECUTING ALL 12 LAB EXAM PYTHON PROGRAMS ")
    print("=" * 60)

    # Use Agg backend so plots are generated and saved without blocking
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"

    passed = 0
    failed = 0

    for script in scripts:
        print(f"\n>>> Running {script} ...")
        res = subprocess.run([sys.executable, script], env=env)
        if res.returncode == 0:
            print(f"[OK] {script} finished successfully.")
            passed += 1
        else:
            print(f"[ERROR] {script} exited with error code {res.returncode}.")
            failed += 1

    print("\n" + "=" * 60)
    print(f" Summary: {passed}/{len(scripts)} Passed, {failed} Failed.")
    print("=" * 60)

if __name__ == "__main__":
    main()
