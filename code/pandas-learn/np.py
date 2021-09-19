import numpy as np

np.array([1, 2, 3])
np.array((1, 2, 3))  # 同上
# array([1, 2, 3])

n = np.array(((1, 2), (1, 2)))
np.array(([1, 2], [1, 2]))  # 同上
'''
array([[1, 2],
        [1, 2]])
'''

# 常见的数据生成函数
np.arange(10)  # 10个，不包括10，步长为1
np.arange(3, 10, 0.1)  # 从3到9，步长为0.1
# 从2.0到3.0，生成均匀的5个值，不包括终值3.0
np.linspace(2.0, 3.0, num=5, endpoint=False)
# 返回一个6×4的随机数组，浮点型
np.random.randn(6, 4)
# 指定范围、指定形状的数组，整型
np.random.randint(3, 7, size=(2, 4))
# 创建值为0的数组
np.zeros(6)  # 6个浮点0.
np.zeros((5, 6), dtype=int)  # 5×6整型0
np.ones(4)  # 同上
np.empty(4)  # 同上
# 创建一份和目标结构相同的0值数组
np.zeros_like(np.arange(6))
np.ones_like(np.arange(6))  # 同上
np.empty_like(np.arange(6))  # 同上

# 数组信息
n.shape()  # 数组的形状，返回值是一个元组
n.shape = (4, 1)  # 改变形状
a = n.reshape((2, 2))  # 改变原数组的形状，创建一个新数组
n.dtype  # 数据类型
n.ndim  # 维度数
n.size  # 元素数
np.typeDict  # np的所有数据类型

# 统计计算
np.array([10, 20, 30, 40])[:3]  # 支持类似列表的切片
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
a + b  # array([11, 22, 33, 44])（矩阵相加）
a - 1  # array([9, 19, 29, 39])
4 * np.sin(a)

# 以下是一些数学函数的例子，还支持非常多的数学函数
a.max()  # 40
a.min()  # 10
a.sum()  # 100
a.std()  # 11.180339887498949
a.all()  # True
a.cumsum()  # array([10, 30, 60, 100])
b.sum(axis=1)  # 多维可以指定方向
