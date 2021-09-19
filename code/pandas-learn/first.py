import pandas as pd
from pandas import DataFrame

# 打印pandas版本
# print(pd.__version__)

# 读取数据
# 以下两种读取数据的方式一样，如果是网址，pandas会自动将数据下载到内存
# df = pd.read_excel("https://www.gairuo.com/file/data/dataset/team.xlsx")
# 使用本地相对路径的方式读取
df = pd.read_excel("../../resources/Pandas/team.xlsx")  # type: DataFrame
print(type(df))
# 查看数据方法
print(df.head())  # 查看前5条数据，默认是5条，可以修改想要查看的条数
print(df.tail())  # 与上同，不过是查看尾部
print(df.sample())  # 随机查看5条

# 数据的一些基本属性和方法
print(df.shape)  # (100, 6) 查看行数和列数
print(df.info())  # 查看索引、数据类型和内存信息
print(df.describe())  # 查看数值型列的汇总统计
print(df.dtypes)  # 查看各字段类型
print(df.axes)  # 显示数据行和列名
print(df.columns)  # 列名

# 设置索引
df.set_index("name", inplace=True)  # 建立索引并生效；建立索引以后，pandas就会取消默认索引

# 数据选取
print(df['Q1'])
# df.Q1 # 效果同上，如果列名符合Python变量名要求，可使用
# 选择多列
print(df[['team', 'Q1']])
# df.loc[:,['team', 'Q1']] # 与上面的效果一致
# 选择行，用指定索引选取
print(df[df.index == "Liver"])
# 使用自然索引（行号）选择，使用方式类似列表的切片
print(df[0:3])
print(df[0:10:2])  # 前十行，每两行选取一次（即步长为2）
# 使用iloc方法，个人感觉没有前面的切片方式简单直观
print(df.iloc[:10, :])  # 前十行，所有列的数据
# loc和iloc的区别好像就是一个是使用指定索引，一个是使用默认行索引，传入的两个参数就是
# 指定行列
print(df.loc['Ben', 'Q1':'Q4'])  # 只看Ben的四个季度成绩
print(df.loc['Eorge':'Alexander', 'team':'Q4'])  # 指定行区间

# 单一条件
print(df[df.Q1 > 90])  # Q1列大于90的
print(df[df.team == 'C'])  # team列为'C'的
print(df[df.index == 'Oscar'])  # 指定索引即原数据中的name

# 组合条件
print(df[(df['Q1'] > 90) & (df['team'] == 'C')])  # and关系
print(df[df['team'] == 'C'].loc[df.Q1 > 90])  # 多重筛选

# 其他操作可以参考https://weread.qq.com/web/reader/0413285072599d76041aa6b
