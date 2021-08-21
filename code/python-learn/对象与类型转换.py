# python也是一门面向对象语言，一切都是对象

# 查看对象的内存地址
a = 'hello'
print(id(a))

# 类型转换其实是将对象转换为了另外一个对象，原对象不变
# python存在四个类型转换函数，int(),float(),str(),bool()
# 类型转换函数是将其他类型的对象转换为当前类型
a = True
print(a)
b = int(a)
print(b)
# 由于python是弱类型语言，虽然存在类型推断，但是变量的类型却是可以改变的