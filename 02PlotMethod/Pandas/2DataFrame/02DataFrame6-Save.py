import pandas as pd

a = pd.DataFrame({
    "A": ["A1", "A2", "A3", "A4", "A5"],
    "B": ["B1", "B2", "B3", "B4", "B5"],
    "C": ["C1", "C2", "C3", "C4", "C5"],
    "D": ["D1", "D2", "D3", "D4", "D5"]
})
print(a)
# todo 随机采样 n采样数据条数 replace代表 无放回采样
res = a.sample(n=6, random_state=1, replace=True)
print(res)

# todo 按照比例采样
res = a.sample(frac=0.6, random_state=11, replace=False, axis=0)
print(res)

for line in a.values:
    print(line)

# with open("./a.txt", "w", encoding="utf-8") as file:
#     file.write(a)

# toCsv() 方式
# todo 直接写入 将数据保存为CSV
a.to_csv("./a.txt", index=False, header=False, sep=',')

# todo 读入数据 names指定列名
b = pd.read_csv('../a.txt', sep=',', index_col=None, header=None, names=['A', 'B', 'C', 'D'])
print(b.shape)
print(b)

# todo 存入Excel
a.to_excel('./a.xlsx',sheet_name='aaa',index=False)
res = pd.read_excel('a.xlsx',sheet_name='aaa')

# todo 存入JSON
a.to_json('a.json')
res = pd.read_json('../a.json')
print(res)

