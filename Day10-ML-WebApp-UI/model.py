import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")

x=data[['hours', 'attendance','sleep']]
y=data['marks']

model =LinearRegression()
model.fit(x,y)

def predict_marks(hours,attendance,sleep):
    return model.predict(pd.DataFrame([[hours,attendance,sleep]], columns=['hours','attendance','sleep']))[0]

# print(predict_marks(5,80,8))