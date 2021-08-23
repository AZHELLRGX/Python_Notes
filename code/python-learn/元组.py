# 元组 tuple
# 元组是一个不可变的序列
# 元组的操作方式和列表基本是一致的

# 使用()创建元组
my_tuple = (1,2,3,4,5)
print(my_tuple)

# 当元组不是空元组的时候，()可以省略，但是至少有一个,
my_tuple = 1, # 这种写法也是没有问题的
my_tuple = 1,2,3,4,5
print(my_tuple)

# 元组的解包：将元组中的每一个元素都赋值给一个变量
# 解包的时候，前面的变量个数与元素中的元素个数必须一致
a,b,c,d,e = my_tuple
print("a =",a)
print("b =",b)
print("c =",c)
print("d =",d)
print("e =",e)
# 当然可以使用*来表示list，将解包最后剩下的元素一起封装为一个列表
a,b,c,*d = my_tuple
print("a =",a)
print("b =",b)
print("c =",c)
print("d =",d)
# *可以出现在任意位置，但是不能出现多个
