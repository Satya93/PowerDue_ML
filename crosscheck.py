from sklearn import linear_model, datasets
import numpy as np
from matplotlib import pyplot as plt

diab = datasets.load_diabetes()
diabX = diab.data[:,np.newaxis, 2]

data = [7, 7, 8, 12, 9, 7, 12, 17, 11, 13, 12, 17, 18, 20, 16, 23, 25, 20, 25, 22, 27, 25, 26, 25, 31, 29, 33, 28, 36, 32, 32, 37, 35, 43, 44, 43, 41, 39, 41, 46, 48, 46, 51, 48, 52, 46, 50, 53, 52, 54, 60, 53, 56, 56, 60, 61, 59, 58, 61, 69, 62, 62, 65, 64, 67, 74, 74, 69, 74, 75, 72, 79, 82, 81, 81, 79, 82, 87, 83, 80, 88, 86, 90, 90, 87, 91, 88, 91, 96, 98, 100, 93, 101, 99, 100, 98, 99, 99, 105, 105]
axis = range(0,len(data))
data = np.reshape(data,[-1,1])
axis = np.reshape(axis,[-1,1])

regr = linear_model.LinearRegression()
regr.fit(axis,data)
predict = regr.predict(data)

print regr.coef_
print regr.intercept_
print regr.score(predict,data)