import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

df = pd.read_excel("../../resources/Pandas/team.xlsx")  # type: DataFrame

df['Q1'].plot()  # Q1成绩的折线分布
plt.show()
# 设置索引
df.set_index("name", inplace=True)  # 建立索引并生效；建立索引以后，pandas就会取消默认索引
df.loc['Ben', 'Q1':'Q4'].plot.bar()  # 柱状图
plt.show()
df.loc['Ben', 'Q1':'Q4'].plot.barh()  # 横向柱状图
plt.show()

# 各Team四个季度总成绩趋势
# T可以理解为横纵坐标抽翻转【transform】
df.groupby('team').sum().T.plot()
plt.show()

# 各组人数对比
df.groupby('team').count().Q1.plot.pie()
plt.show()
