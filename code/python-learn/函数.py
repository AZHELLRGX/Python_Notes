# 函数也是一个对象
# 定义一个函数
def fn():
    print("this is the first function")


# 定义一个有功能的函数：求两个数的和
def plus(a, b):
    print(a, "+", b, "=", a + b)


# 可以给函数的形参指定默认值
def reduce(a, b=2):
    print(a, "-", b, "=", a - b)


# python中的不定长参数与Java的使用方式基本一致，语法如下所示
# 其实依赖于python支持的指定名称传递参数机制，不定长参数可以放在参数列表的任意位置
# 但是要求带*的参数后的所有参数，必须以关键字参数的形式传递
def plus_pro(a, b, *c):
    # *c其实是一个元组类型
    print(type(c))
    result = a + b
    for e in c:
        result += e
    print("all nums sum is", result)


print(fn)  # 函数对象 <function fn at 0x00000245533BF040>
print(type(fn))  # <class 'function'>
print(fn())  # 函数因为没有返回值，所以返回为None

plus(1, 2)
reduce(3)
# 可以不按照形参顺序输入参数，而按照形参名传入参数
reduce(b=4, a=10)
# 两种传参方式可以混用，但是容易产生混淆，不建议使用

# 在python中，函数在调用的时候，解析器不会检查实参的类型
# 所以实参可以传递任意类型的对象
# 但是编码过程中还是需要根据函数的功能需要传入指定类型的参数，避免函数运行过程中出现异常

# 调用带有不定长参数函数
plus_pro(1, 3, 5, 6, 7, 8, 9)


# 如果在形参的开头直接写一个*,则要求我们的所有的参数必须以关键字参数的形式传递
def fn2(*, a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


# fn2(a=3,b=4,c=5)

# *形参只能接收位置参数，而不能接收关键字参数
# def fn3(*a) :
#     print('a =',a)

# **形参可以接收其他的关键字参数，它会将这些参数统一保存到一个字典中
#   字典的key就是参数的名字，字典的value就是参数的值
# **形参只能有一个，并且必须写在所有参数的最后
def fn3(b, c, **a):
    print('a =', a, type(a))
    print('b =', b)
    print('c =', c)


# fn3(b=1,d=2,c=3,e=10,f=20)

# 参数的解包（拆包）
def fn4(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


# 创建一个元组
t = (10, 20, 30)

# 传递实参时，也可以在序列类型的参数前添加星号，这样他会自动将序列中的元素依次作为参数传递
# 这里要求序列中元素的个数必须和形参的个数的一致
# fn4(*t)

# 创建一个字典
d = {'a': 100, 'b': 200, 'c': 300}
# 通过 **来对一个字典进行解包操作
fn4(**d)


# python中函数的返回值也是根据return关键字来控制，可以返回任意类型的对象；
# 也可以类似scala一样返回一个函数
def add_one(a):
    return a + 1


def test_return():
    return add_one


print(test_return()(1))  # 有点scala的柯里化语法那种味道了，但是两者其实有很大的区别


# 文档字符串；函数说明
# 可以为形参指定类型说明，但是这个类型没有预检查性质
def test_doc_des_str(a: int, b: bool, c: str) -> int:
    """
    这里是函数意义说明
    :param a: 这里是参数a意义说明
    :param b: 这里是参数b意义说明
    :param c: 这里是参数c意义说明
    :return:
    """
    return 10


help(test_doc_des_str)
