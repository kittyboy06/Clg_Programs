import pandas as pd
import requests

print("Reading iris dataset from URL...")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode('utf-8')
    lines = content.splitlines("\n")
    col_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
    iris_data = pd.DataFrame([line.split(',') for line in lines if line.strip()], columns=col_names)
    
    print(iris_data.head())
    print("Data Shape:", iris_data.shape)
    print("Data info:\n", iris_data.info())
    print("Descriptive Statistics:\n", iris_data.describe())