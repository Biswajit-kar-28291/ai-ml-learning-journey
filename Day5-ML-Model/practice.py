import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv')

print(data["hours"])
print(data["marks"])

x=data[['hours']]
y=data['marks']

model=LinearRegression()
model.fit(x,y)

pred=model.predict([[5]])
print('predict vauel is:',pred)

print(model.predict([[2]]))
print(model.predict([[7]]))
print(model.coef_)   # slope
print(model.intercept_)  # intercept