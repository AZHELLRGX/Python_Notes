# while语句与其他语言有一些差别，支持连接else语句
i = 0
while i < 10:
    i += 1
    print("i =", i)
else:
    print("循环结束，i =", i)

# print默认打印字符串后会在结尾加上\n，如果不想换行，就指定end参数
# print("******",end = '')

# 循环嵌套
i = 0
while i < 5:
    j = 0
    while j <= i:
        j += 1
        print("*", end='')
    print()
    i += 1

# python支持break与continue关键字；使用方法也与Java基本一致
