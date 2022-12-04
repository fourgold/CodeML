"""
读取每个班级的学生信息和成绩文件
    最终全校学生的信息和成绩合并到一张表中
    columns：学号、姓名、年级、班级、性别、年龄、语文、英语、数学
    基于这张表进行统计分析
        统计每个班级的平均年龄及各科的平均分
        统计每个学生的三科成绩的总分
        统计全校学生的男女比例
    画图：
        柱状图：各科平均分
        饼状图：男女比例
"""
import os
import pandas as pd

info = []
score = []
path = os.path.join(os.getcwd(), '6Case/school')
for path, names, files in os.walk(path):
    for file in files:
        print(names)
        if (file.__contains__("info")):
            info.append(pd.read_csv(os.path.join(path, file), sep=';'))
        else:
            score.append(pd.read_csv(os.path.join(path, file), sep=';'))

info = pd.concat(info, axis=0, ignore_index=True)
score = pd.concat(score, axis=0, ignore_index=True)
print(info.columns)
print(score.columns)
res = pd.merge(info, score, how='inner', left_on='学生学号', right_on='学号')
# res.columns = ['学号', '姓名', '年级', '班级', '性别', '年龄', '语文', '英语']
print(res)
res.groupby('学生')
