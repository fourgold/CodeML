import pandas as pd
import matplotlib.pyplot as plt

# 梯度下降法对数据预测波士顿房价  数据集：datas/boston_housing.data
# 加载数据
data = pd.read_csv('datas/boston_housing.data', sep='\s+', header=None)  # \s+表示空格分隔
print(data)
# 获取特征属性X和目标属性Y 不要索引
X, Y = data.iloc[:, 5], data.iloc[:, -1]  # loc根据行的标签 iloc根据列的标签


def costFunc(b, w, X, Y):
    """
    最小二乘法计算 损失函数
    :param b: 斜率
    :param w: 截距
    :param X: 数据集
    :param Y: 数据集
    :return: 代价值
    """
    totalError = 0
    for i in range(0, len(X)):
        totalError += (Y[i] - (w * X[i] + b)) ** 2
    return totalError / float(len(X)) / 2.0


def gradientDescent(b, w, X, Y, lr, epochs):
    """
    梯度下降法
    :param b: 斜率
    :param w: 截距
    :param X: 数据集
    :param Y: 数据集
    :param lr: 学习率
    :param epochs: 迭代次数
    :return: 斜率 截距
    """
    m = float(len(X))  # 数据集长度
    for i in range(epochs):
        b_grad = 0
        w_grad = 0
        for j in range(0, len(X)):
            b_grad += (1 / m) * ((w * X[j] + b) - Y[j])  # 斜率
            w_grad += (1 / m) * ((w * X[j] + b) - Y[j]) * X[j]  # 截距
        b = b - (lr * b_grad)
        w = w - (lr * w_grad)
        plt.scatter(X, Y)
        if i % 5 == 0:
            print("epochs:", i)
            print("cost:", costFunc(b, w, X, Y))
            plt.plot(X, w * X + b)
            plt.show()
            print(costFunc(1, 1, X, Y))
    return b, w


if __name__ == '__main__':
    print(X)
    print(X + 1)
    print(type(X))
    print(Y)
    gradientDescent(0, 0, X, Y, 0.01, 200)
    # 画图
    plt.scatter(X, Y)
    print(costFunc(1, 0.1, X, Y))

    # 画图 X Y=X+1
    plt.plot(X, X + 1)
    plt.show()
    pass
