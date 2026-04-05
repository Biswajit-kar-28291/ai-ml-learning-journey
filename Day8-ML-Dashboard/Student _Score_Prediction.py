import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = pd.read_csv("student_data.csv")
# print(data)
print(data.head())
print(data.shape)

x=data[['hours','attendance', 'sleep']]
y=data['marks']

x_train,x_text,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_text)

pred=model.predict(pd.DataFrame([[2,50,7]],columns=('hours','attendance', 'sleep')))
print(pred)

print("r2:", r2_score(y_test,y_pred))

data.plot(kind='scatter', x='hours',y='marks')
plt.show()

data.plot(kind='scatter', x='attendance',y='marks')
plt.show()

data.plot(kind='scatter',x='sleep',y='marks')
plt.show()