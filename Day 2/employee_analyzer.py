import pandas as pb
def salary_level(x):
    if x > 60000:
        return "High"
    elif x > 40000:
        return "Medium"
    else:
        return "Low"
data=pb.read_csv("employe.csv")
print(data.head())
print(data.columns)
print(data.shape)
print(data['salary'].mean())
print(data['salary'].min())
print(data['salary'].max())
top=data.loc[data['salary'].idxmax()]
print(top['name'])
data.groupby('department')['salary'].mean()
data['Salary_Level']=data['salary'].apply(salary_level)
print(data)
print(data['Salary_Level'].value_counts())
print("\nSorted by salary:")
print(data.sort_values(by="salary", ascending=False))

data.to_csv("output.csv", index=False)