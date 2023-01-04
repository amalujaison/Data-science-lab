import sklearn
from sklearn import datasets, metrics, linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#load the data set
irisData = datasets.load_iris()
x = pd.read_csv('data.csv')
a = irisData.data
b = irisData.target

#split the dataset into train set and test set
a_train, a_test, b_train, b_test = train_test_split(a,b,test_size=30,random_state=42)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(a_train,b_train)

y_pred=regressor.predict(a_test)

#visualizing the values
plt.scatter(a_train,b_train,y_pred)
plt.plot(a_train)
plt.title('linear regression')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


