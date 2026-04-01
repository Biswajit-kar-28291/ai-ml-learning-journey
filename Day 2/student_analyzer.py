import pandas as pd

df = pd.read_csv("data.csv")

#Original Data
print("original data")
print(df)

#first 5 row
print("This is first five row of data ")
print(df.head())

# column name
print("Printing column name:")
print(df.columns)

# Shape data
print("Printing shape of all data.csv")
print(df.shape)

# Avarage data
print("Avarage of all data:")
print(df['Marks'].mean())

# add pass fail

df["Result"]=df['Marks'].apply(lambda x: "pass" if x>40  else "fail")

# print updated value
print("updated data")
print(df)

# top student information
top=df.loc[df['Marks'].idxmax()]
print(f"{top['Name']} is topper.\nAnd he/she scored {top['Marks']}.\nObviously he/she is {top['Result']}")

# pass fail count
print(df["Result"].value_counts())