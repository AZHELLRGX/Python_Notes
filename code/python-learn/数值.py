# 在python中数值分为三种：整数、浮点数、复数
# 在python中所有的整数都是int类型
# 在python中的整数大小没有限制，可以是一个无限大的整数；这点与Java等静态语言很不同
# a = 9999999999999999999999999999 * 888888888888888
# print(a)

# 如果整数的长度过大，可以用下划线作为分割线
c = 123_456_789
print(c)

# 进制表示
# 二进制：0b开头
c = 0b10
print(c)
# 八进制：0o开头
c = 0o17
print(c)
# 十六进制：0x开头
c = 0xA
print(c)

# 在python中，所有的小数都是浮点数
f = 1.46
print(f)
# 对浮点数进行运算的时候，可能会得到一个不精确的结果
f = 0.1 + 0.2  # 0.30000000000000004
print(f)

# 复数此处先不讲解
