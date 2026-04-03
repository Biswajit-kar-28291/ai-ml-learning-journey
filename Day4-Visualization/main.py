import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("sales_data.csv")
print("All data: ", data)

data["total_sale"]=data['price']*data['quantity']
print("After adding total_sale coloumn: ")
print(data)

print("Total revenue is:", data["total_sale"].sum())

print("Avarage sale is:", data['total_sale'].mean())

data.groupby("category")['total_sale'].sum().plot(kind="bar")
plt.title('Catagory\'s total sale')
plt.show()

data.groupby("city")['total_sale'].sum().plot(kind="bar")
plt.title("city\'s total sale")
plt.show()

data.groupby("date")['total_sale'].sum().plot(kind="line")
plt.title("day wise total sale")
plt.show()

data.groupby("category")["total_sale"].sum().plot(kind="pie", autopct='%1.1f%%')
plt.title('Catagory\'s total sale')
plt.show()