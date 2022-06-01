import pandas as pd


columns = []
tables = []


df = pd.read_csv("Tables/students")

df = df[columns]

print(df.head())
