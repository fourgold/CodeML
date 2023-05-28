import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import matplotlib as mpt
import sys
import joblib
import warnings

warnings.filterwarnings("ignore")

# 加载数据
data = pd.read_csv('datas/boston_housing.data', sep='\s+', header=None)  # \s+表示空格分隔



# 获取特征属性X和目标属性Y
X, Y = data.iloc[0:7, :-1], data.iloc[0:7, -1]  # loc根据行的标签 iloc根据列的标签
print(X)

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=20)

# 特征工程
'''
PolynomialFeatures ####多项式扩展
degree=2,扩展的阶数
interaction_only=False,是否只保留交互项
include_bias=True，是否需要偏置项 函数的截距
'''
poly = PolynomialFeatures(degree=3, interaction_only=True, include_bias=False)
"""
fit
fit_transform ==> fit+transform
transform
"""
poly.fit(x_train)  # fit之后能把参数保存下来,当模型使
x_train_poly = poly.transform(x_train)
print(x_train_poly)
