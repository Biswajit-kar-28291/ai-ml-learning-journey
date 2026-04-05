import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data=pd.read_csv("house_data.csv")
# print(data)

x=data[['area','bedrooms','age']]
y=data['price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("x train")
print(X_train)
print("x test")

print(X_test)
print("ytrain")

print(y_train)
print("y test")

print(y_test)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)


print("Accuracy:", r2_score(y_test, y_pred))

pred = model.predict(pd.DataFrame([[1500,3,10]], columns=['area','bedrooms','age']))
print("Predicted Price:", pred)
print("coeff",model.coef_)
print("intersept",model.intercept_)     