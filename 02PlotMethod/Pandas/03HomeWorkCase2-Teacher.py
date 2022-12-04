import os
import pandas as pd

school_dir = os.path.join(os.getcwd(), "6Case/school")
# print(school_dir)
grade_dirs = os.listdir(school_dir)
# print(grade_dirs)
df_school = pd.DataFrame()
for grade_name in grade_dirs:
    grade_dir = os.path.join(school_dir, grade_name)
    # print(grade_dir)
    class_dirs = os.listdir(grade_dir)
    # print(class_dirs)
    for class_name in class_dirs:
        info_file = os.path.join(grade_dir, class_name, "student_info.txt")
        # print(info_file)
        df_info = pd.read_csv(info_file, sep=";")
        # print(df_info)
        score_file = os.path.join(grade_dir, class_name, "student_score.txt")
        df_score = pd.read_csv(score_file, sep=";")
        # 合并学生信息表和成绩表 merge
        df_info_score = pd.merge(df_info, df_score, left_on="学生学号", right_on="学号", how="inner")
        # print(grade_name, class_name)
        # print(df_info_score)
        df_info_score["年级"] = pd.Series(grade_name, index=df_info_score.index)
        df_info_score["班级"] = pd.Series(class_name, index=df_info_score.index)
        # print("--------------------------------")
        # print(df_info_score)
        df_school = pd.concat([df_school, df_info_score], axis=0, join="outer", ignore_index=True)
print(df_school)
"""
axis
inplace: True 表示在原对象上进行操作，改变了原对象，返回值为None
         False 修改后返回一个新的对象，原对象没有被修改
"""
df_school.drop("学号",inplace=True,axis=1)
# df_school_new = df_school.drop("学号",inplace=False,axis=1)
print("----------------------------")
print(df_school)
# print(df_school_new)