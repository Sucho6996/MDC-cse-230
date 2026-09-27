import pandas as pd

# DataFrame = 2D Tabular Data Structure with rows and cols

data = {
    "Name": ["Alex", "Bob", "Charlie"],
    "Age" : [30,35,50],
    "Exp" : [6,11,25],
    "Salary" : [25000,30000,65000] 
}

df = pd.DataFrame(data, index=[1,2,3])
print(df)
print("------------------------------------------------")

print("\n\nDetails of Emp 2\n",df.loc[2]) #try .iloc()
print("------------------------------------------------")

# Add new column
df["Department"]=["Marketing","Sales","IT"]
print(df)
print("------------------------------------------------")

# Add a new Row
newRow=pd.DataFrame([{
    "Name": "Sandy",
    "Age":28,
    "Exp": 5,
    "Salary": 45000,
    "Department": "HR"
}],
index=[4])
df = pd.concat([df, newRow])
print(df)
print("------------------------------------------------")

# Add new Rows
newRows=pd.DataFrame([
    {
        "Name": "Sandy",
        "Age":28,
        "Exp": 5,
        "Salary": 45000,
        "Department": "HR"
    },
    {
        "Name": "Amit",
        "Age":29,
        "Exp": 6,
        "Salary": 55000,
        "Department": "IT"
    },
    {
        "Name": "Andy",
        "Age":29,
        "Exp": 6,
        "Salary": 55000,
        "Department": "IT"
    }
],
index=[5,6,7])
df = pd.concat([df, newRows])
print(df)
print("------------------------------------------------")
