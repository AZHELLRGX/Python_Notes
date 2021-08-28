# 字符串和其他语言差别不大，主要是讲解一下特例和基本函数的使用
# python的引号可以是单引号，也可以是双引号；但是注意不要混用
s = 'hello'
s = "hello,Mike"
print(s)

# 相同的引号不要相互嵌套
s = 'Lucy:"Hi,Mike!"'
print(s)

# 长字符串，保留字符串格式
s = '''
仰天大笑出门去，
我辈岂是蓬蒿人
'''
print(s)
# 以下这种写法只可以连接多行字符串，但是不能保留字符串格式
s = '\
举头望明月，\
低头思故乡\
'
print(s)

# python中，字符串只能和字符串进行拼接，不能和其他数值类型直接相加，这点与Java等语言不同
a = 1
# print("a = " + a) # 这种写法在python不支持
print("a =", a)  # 这种才是常用写法
# 也可以借助占位符
b = 'hello, %s' % 'Mike'
print(b)
b = 'hi,%s! \n你好，%s！' % ("Mike", "迈克")
print(b)
# s前面的数字表示最小字符数量，如果字符长度不够，则在前面补充空格
b = 'hi,%3s!' % "abcdada"
b = 'hi,%3.5s!' % "abcdada"  # 3.5表示长度在3到5之间
b = 'data is %.2f' % 123.456  # 更多的占位符相关的知识可以查阅相关资料
print(b)

# 格式化字符串
c = f'hello,{a},{b}'  # 这个用法与scala非常相似，scala中使用s格式化字符串
print(c)

# 字符串复制
c = 'hello' * 20  # 将hello自身相加20次
print(c)
