# 一般来讲，高阶函数就是针对函数式编程的特殊语法
# 高阶函数一般有两个特点：
# 1、接收一个或多个函数作为参数
# 2、将函数作为返回值返回

# 定义一个函数，可以将指定列表中所有的偶数，保存到一个新的列表中返回
def fn(lst, f):
    """
    将指定列表中所有的偶数，保存到一个新的列表中
    :param f: 过滤功能函数
    :param lst: 需要进行筛选的列表
    :return: 返回一个只有偶数的新列表
    """

    # 创建一个新列表
    new_list = []

    # 对列表进行筛选
    for n in lst:
        if f(n):
            new_list.append(n)

    # 返回新列表
    return new_list


# 过滤偶数
def fn1(i):
    return i % 2 == 0


# 过滤大于5的数
def fn2(i):
    return i > 5


o_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fn(o_list, fn1))
print(fn(o_list, fn2))

# 可以使用lambda表达式来实现匿名函数
# 语法： lambda 参数列表:返回值
print(fn(o_list, lambda i: i % 2 != 0))


# python自带了很多函数，比如filter以及map等函数，在这些函数中都可以使用匿名函数来简化编码

# filter()
# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
# 参数：
#  1.函数，根据该函数来过滤序列（可迭代的结构）
#  2.需要过滤的序列（可迭代的结构）
# 返回值：
#   过滤后的新序列（可迭代的结构）

def fn5(a, b):
    return a + b


# (lambda a,b : a + b)(10,20)
# 也可以将匿名函数赋值给一个变量，一般不会这么做
# fn6 = lambda a, b: a + b
# print(fn6(10,30))

r = filter(lambda i: i > 5, o_list)
# print(list(r))

# map()
# map()函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回

result = map(lambda i: i ** 2, o_list)

print(list(result))

# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数 ， key
#   key需要一个函数作为参数，当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
str_list = ['hi', 'hello', 'c', 'bullshit', 'shit']
str_list.sort(key=len)  # 其实就是按照字符串的长度排序了
print(str_list)
mix_list = [2, 5, '1', 3, '6', '4']
mix_list.sort(key=int)
print(mix_list)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意的序列进行排序
#   并且使用sorted()排序不会影响原来的对象，而是返回一个新对象

# l = "123765816742634781"

print('排序前:', mix_list)
print(sorted(mix_list, key=int))
print('排序后:', mix_list)
