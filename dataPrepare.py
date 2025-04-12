import pandas as pd

df = pd.read_csv('/home/kesin/.kaggle/malicious_phish.csv')

null_values = df.isnull().sum()
print("Null Values in Each Column:\n", null_values)

shape = df.shape
print("\nShape of the Dataset:", shape)

dataset_info = df.info()