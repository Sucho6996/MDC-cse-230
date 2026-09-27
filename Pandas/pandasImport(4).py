import pandas as pd

df = pd.read_csv("Pandas\\pandas_practice_employees.csv")
print(df)
print("-------------------------------------------------------------")

df= pd.read_json("Pandas\\pandas_practice_employees.json")
print(df)
