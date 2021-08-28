# python中可以使用range来生成一个自然数序列
# range函数可以指定三个参数
# 1、起始位置（可以省略，默认是0）
# 2、结束位置
# 3、步长（可以省略，默认是1）
r = range(5)
print(list(r))

r = range(0, 10, 2)
print(list(r))

r = range(10, 0, -1)

print(list(r))

# range可以搭配for循环语句实现指定次数的循环
for i in range(7):
    print(i, end='\t')
else:
    print("循环结束")
