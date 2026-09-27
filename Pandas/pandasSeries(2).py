import pandas as pd

# Series is a 1D labeled array can hold any data type
# Single column in a spreadsheet

data=[100,102,104]
series = pd.Series(data)
print(series)

print("---------------------------------------------")

series = pd.Series(data, index=["Apartment 1","Apartment 2","Apartment 3"])
print(series)

series.loc["Apartment 3"]=300
print("Apartment 3 = ",series.loc["Apartment 3"])
print("Apartment 3 = ",series.iloc[2])

print("---------------------------------------------")
data=[100.1,102.2,104.3]
series = pd.Series(data)
print(series)
# Exercise-> try it with char , string and boolean


print("---------------------------------------------")
data=[100,102,104,200,202]
series = pd.Series(data, index=["a","b","c","d","e"])
print("Value > 200\n",series[series>=200])

print("---------------------------------------------")

calories ={
    "Day 1": 1750,
    "Day 2": 2250,
    "Day 3": 1700,
    "Day 4": 1800,
    "Day 5": 2000,
    "Day 6": 4000,
    "Day 7": 1950
}

series=pd.Series(calories)

#series.loc["Day 3"]+=500
print("Cheated on diet on: \n",series[series>2000])


