import pandas as pd
import numpy as np

data = [
    {"name": "张三", "age": 15, "num": "001", "score": 80},
    {"name": "张五", "age": 16, "num": "002", "score": 20},
    {"name": "张六", "age": 16, "num": "001", "score": 80},
    {"name": "李四", "age": 17, "num": "002", "score": 50},
    {"name": "张飞", "age": 17, "num": "001", "score": 80},
    {"name": "刘备", "age": 17, "num": "002", "score": 90},
    {"name": "关羽", "age": 18, "num": "001", "score": 80},
    {"name": "曹操", "age": 18, "num": "001", "score": 70},
    {"name": "马超", "age": 18, "num": "003", "score": 80},
    {"name": "孙权", "age": 19, "num": "003", "score": 20},
    {"name": "孙策", "age": 19, "num": "003", "score": 80},
    {"name": "于禁", "age": 19, "num": "003", "score": 60},
]

df = pd.DataFrame(data)
print(df)

# todo 1.分组 groupby()
res = df.groupby(['age', 'num'])  # .agg(np.mean)
for k, v in res:
    print("=====")
    print('k',k)
    print('v',v)
    print(type(v))

print(res.get_group((15, '001')))  # 查询

# todo 2.连接操作 merge() left/right how(inner left right outer 表示表合并时的类型) on 指定列名用于连接，指定的列名必须两个表中都有的
# 如果没有设置的情况下，使用共同拥有的相同列名
left = pd.DataFrame({"id": [1, 2, 3, 4], "name": ["张三", "李四", "王五", "赵六"], "grade": [7, 7, 8, 9]})
right = pd.DataFrame({"id": [1, 2, 3, 4], "class": ["三", "四", "五", "六"], "age": [17, 71, 18, 19]})
df = pd.merge(left, right, how="inner", on="id")  # lefton righton 分别指定关联健值对
print(df)

# todo 3.concat 合并表
a = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [3, 4, 5, 6]
})
b = pd.DataFrame({
    "A": [5, 5, 5, 4],
    "B": [3, 4, 5, 6]
})
df = pd.concat([a, b], axis=1, ignore_index=False)  # 忽略索引 axis=0  行拼接 横向是左右拼接 拼接按照索引拼接
print(df)
print(df.loc[:, 'A'])
