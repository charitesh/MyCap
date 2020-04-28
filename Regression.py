import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression


boston=load_boston()
print(boston.DESCR)

dataset=boston.data
for name,index in enumerate(boston.feature_names):
    print(name,index)

data=dataset[:,12].reshape((-1,1))
print(data,np.shape(data))
target=boston.target.reshape((-1,1))
print(target,np.shape(target))

plt.scatter(data,target,color='blue')
plt.xlabel("Lower Income")
plt.ylabel("Cost")
plt.show()
lr=LinearRegression()
lr.fit(data,target)
pred=lr.predict(data)
print(pred)

plt.scatter(data,target,color='red')
plt.plot(data,pred,color='black')
plt.xlabel("Lower Income")
plt.ylabel("Cost")
plt.show()
bias = lr.intercept_
coeff = lr.coef_
print(bias)
print(coeff)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
model=make_pipeline(PolynomialFeatures(1),lr)
model.fit(data,target)
pred=model.predict(data)
plt.scatter(data,target,color='red')
plt.plot(data,pred,color='black')
plt.xlabel("Lower Income")
plt.ylabel("Cost")
plt.show()

from sklearn.metrics import r2_score
r2_score(pred,target)
