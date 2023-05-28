import pandas as pd

a = pd.DataFrame({
    "A": ["A1", "A2", "A3", "A4", "A5"],
    "B": ["B1", "B2", "B3", "B4", "B5"],
    "C": ["C1", "C2", "C3", "C4", "C5"],
    "D": ["D1", "D2", "D3", "D4", "D5"]
})
print(a)
# todo 随机采样 n采样数据条数 replace代表 无放回采样
res = a.sample(n=6, random_state=1,replace=True)
print(res)

# todo 按照比例采样
res = a.sample(frac=0.6,random_state=11,replace=False,axis=0)
print(res)
