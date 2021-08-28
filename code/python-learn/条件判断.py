a = 3
if a > 2:
    print("a =", a)

# python的if语句如果想控制多行代码，则不能依靠类似Java的括号设计，而是依赖代码缩进
b = 2
if a > b:
    print("a =", a)
    print("b =", b)
print("if的控制到这里就已经结束了")

if a > 2:
    print("a =", a)
    if b > 2:
        print("b =", b)

# python有两种代码缩进方式，一种是tab键，一种是使用四个空格；官方推荐使用空格方式，这样代码风格较为统一
# sublime可以设置"translate_tabs_to_spaces": true, 来自动将Tab转换为空格

# input函数在调用的时候，程序会立即暂停，等待用户输入
i = input("please input some words:")  # input函数可以设置一段字符串作为输入提示
print("input is", i)  # 使用REPL自行，ctrl+b无效果

# if else语句
age = int(input("请输入年龄:"))  # input的返回值是字符串，需要转换类型
if age >= 18:
    print("可以继续访问")
else:
    print("未成年无法访问")

# if elif else  除了使用elif取代了else if语法外，基本没有其他的不同
if age >= 70:
    print("古稀")
elif age >= 60:
    print("花甲")
elif age >= 50:
    print("知天命")
elif age >= 40:
    print("不惑")
elif age >= 30:
    print("而立")
elif age >= 20:
    print("弱冠")
else:
    print("未成年")
