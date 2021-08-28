# python使用[]来创建列表，列表可以包含任意的对象
my_list = [10, 'hello', True, None, [1, 2, 'world']]
print(my_list)

# 列表是有序的，数据的顺序就是插入顺序；可以通过index获取列表中的元素
print(my_list[3])
# 越界异常信息为：IndexError: list index out of range
print(len(my_list))  # 列表的大小
print(len(my_list[1]))  # 列表存储的元素的长度
# python的索引可以是负数，表示倒数获取元素
print(my_list[-3])

# 切片 ： 从现有列表中获取一个子列表
# 切片的区间是左闭右开区间
print(my_list[1:3])
# 和Java不同的是，切片是一个新的对象，而不是类似Java的subList会影响原对象
# 如果省略结束位置的索引，则一直切片到原列表的结尾
print(my_list[1:])
# 如果省略开始位置的索引，则从第一个元素开始截取
print(my_list[:2])
# 创建列表的副本，即原列表的深拷贝
print(my_list[:])

# 切片的时候，还可以指定步长
# 语法： 列表[起始:结束:步长]
print(my_list[0:4:2])
# 步长不能是0，但可以是负数

# 通用操作
new_list = my_list + [6, 7, 9]  # 使用+连接两个列表
print(new_list)
new_list = my_list * 2  # 使用*复制自身
print(new_list)
# 使用in和not in判断元素是否存在于列表中
print("hello" in my_list)
print("world" not in my_list[4])
# 使用max()和min()获取列表中的最大值和最小值
num_list = [10, 8, 19, 2]
print(max(num_list))
print(min(num_list))
# index()与count()方法
print(num_list.index(19))  # 元素必须存在与列表，否则会抛出not in的异常
print(num_list.count(8))  # 统计指定元素在列表中存在的次数

# 列表中的元素可以改变
num_list[2] = 9
print(num_list)
# 删除列表中的元素
del num_list[2]
print(num_list)

# 通过切片修改列表
# 在给切片进行赋值时候，只能使用序列（列表或者字符串）
num_list[0:2] = [11, 19]
print(num_list)
num_list[0:0] = [20]  # 在起始位置插入元素
print(num_list)
# 也可以支持步长和del操作
del num_list[0:2]
# num_list[0:2] = [] # 上面的操作与此操作相同
print(num_list)
