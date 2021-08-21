a = 3
if a > 2:print("a =",a)

# python语句如果想控制多行代码，则不能依靠类似Java的括号设计，而是依赖代码缩进
b = 2
if a > b:
    print("a =",a)
    print("b =",b)
print("if的控制到这里就已经结束了")

if a > 2:
    print("a =",a)
    if b > 2:
        print("b =",b)

# python有两种代码缩进方式，一种是tab键，一种是使用四个空格；官方推荐使用空格方式，这样代码风格较为统一
# sumlime可以设置"translate_tabs_to_spaces": true, 来自动将Tab转换为空格