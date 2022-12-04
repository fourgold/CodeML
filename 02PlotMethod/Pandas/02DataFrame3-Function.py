import pandas as pd

"""
apply函数
    操作行列函数
    将每一行或者每一列的数据 取出 操作
"""
data = [{'name': '张三', 'age': 15, 'num': 1, 'members': [1, 2, 3]}
    , {'name': '李四', 'age': 16, 'num': 2, 'members': [1, 2, 3]}
    , {'name': '王五', 'age': 3, 'num': 3, 'members': [1, 2, 3]}]
df01 = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df01)
print("\n测试")

df02 = df01.apply(func=lambda x: pd.Series([x[0], x[1] + 1, x[2]], index=['name', 'age', 'num']), axis=1)
print(df02)
print(df01)


def func01(x):
    x[1] += 1


# todo applyMap 对每一个元素
def func06(x):
    if isinstance(x, list):
        x[0] = 999
    print(x)


df01.applymap(func=func06)  # 基本类型属于不可变对象 string int
print(df01)

series01 = pd.Series([1, 2, 3, 4, 5])
print(series01.max())
print(series01.min())  # mean median

df01 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['c1', 'c2', 'c3'])
print(df01)
print(df01.min(axis=1))  # 沿着轴计算

# 环比 同比
print(df01.pct_change())
# 协方差  无偏估计 期望
print(df01.cov())

# todo 分组数据处理
data = [{'name': '张三', 'age': 15, 'num': 1, 'members': [1, 2, 3]}
    , {'name': '李四', 'age': 16, 'num': 2, 'members': [1, 2, 3]}
    , {'name': '王五', 'age': 3, 'num': 3, 'members': [1, 2, 3]}]
df01 = pd.DataFrame(data, ['a', 'b', 'c'])
res = df01.groupby("age")
print(res)
print(res.groups)
print(type(res))
print(res.get_group(15))
print(type(res.get_group(15)))
for a, b in res:
    print(a)
    print(b)
res2 = df01.groupby(["age", "num"])
print(res2.groups)
