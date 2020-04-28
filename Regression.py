import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
print(boston.DESCR)

dataset = boston.data
for name, index in enumerate(boston.feature_names):
    print(name, index)

data = dataset[:,12].reshape((-1, 1))
np.shape(dataset)

target = boston.target.reshape((-1, 1))
np.shape(target)

plt.scatter(data, target, color='orange')
plt.xlabel("Lower Income")
plt.ylabel("House cost")
plt.show()

from sklearn.linear_model import LinearRegression
Lr = LinearRegression()
Lr.fit(data, target)
pred = Lr.predict(data)

plt.scatter(data, target, color='orange')
plt.plot(data, pred, color='black')
plt.xlabel("Lower Income")
plt.ylabel("House cost")
plt.show()


from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

mod = make_pipeline(PolynomialFeatures(10), Lr)
mod.fit(data, target)
pred = mod.predict(data)
plt.scatter(data, target, color='orange')
plt.plot(data, pred, color='black')
plt.xlabel("Lower Income")
plt.ylabel("House cost")
plt.show()


from sklearn.metrics import r2_score
r2_score(pred, target)
