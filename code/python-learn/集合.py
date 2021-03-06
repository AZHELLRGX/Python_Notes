# 集合只能存放不可变对象
# 集合中存储的对象是无序的
# 不能存在重复的元素
# 类似Java的Set

s = {10, 3, 5, 1, 2, 1, 2, 3, 1, 1, 1, 1}  # <class 'set'>
# s = {[1,2,3],[4,6,7]} TypeError: unhashable type: 'list'
# 使用 set() 函数来创建集合
s = set()  # 空集合
# 可以通过set()来将序列和字典转换为集合
s = set([1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5]) # 但是其实不太推荐这种写法
s = set('hello')
s = set({'a': 1, 'b': 2, 'c': 3})  # 使用set()将字典转换为集合时，只会包含字典中的键
# 类似Java中 HashSet就是HashMap的键的实现方式


# 创建集合
s = {'a', 'b', 1, 2, 3, 1}

# 使用in和not in来检查集合中的元素
# print('c' in s)

# 使用len()来获取集合中元素的数量
# print(len(s))

# add() 向集合中添加元素
s.add(10)
s.add(30)

# update() 将一个集合中的元素添加到当前集合中
# update()可以传递序列、元组或字典作为参数，字典只会使用键
s2 = set('hello')
s.update(s2)
s.update((10, 20, 30, 40, 50))
s.update({10: 'ab', 20: 'bc', 100: 'cd', 1000: 'ef'})

# {1, 2, 3, 100, 40, 'o', 10, 1000, 'a', 'h', 'b', 'l', 20, 50, 'e', 30}
# pop()随机删除并返回一个集合中的元素
# result = s.pop()

# remove()删除集合中的指定元素
s.remove(100)
s.remove(1000)

# clear()清空集合
# s.clear()

# copy()对集合进行浅复制

# print(result)
print(s, type(s))

# 下面是关于集合的运算
s = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# 取交集
result = s & s2
print('交集结果 =', result)
# 取并集
result = s | s2
print('并集结果 =', result)
# 取差集
result = s - s2
print('差集结果1 =', result)
result = s2 - s
print('差集结果2 =', result)
# 异或集 获取只在一个集合中存在的元素
result = s ^ s2
print('异或集结果2 =', result)  # 好像就是前面两个差集的并集

# 检查一个集合是否是另外一个元素的子集
# 如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合是a集合超集
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

result = a <= b  # True
result = {1, 2, 3} <= {1, 2, 3}  # True # 也就是说集合本身是自己的子集
result = {1, 2, 3, 4, 5} <= {1, 2, 3}  # False

# < 检查一个集合是否是另一个集合的真子集
# 如果超集b中含有子集a中所有元素，并且b中还有a中没有的元素，则b就是a的真超集，a是b的真子集
result = {1, 2, 3} < {1, 2, 3}  # False
result = {1, 2, 3} < {1, 2, 3, 4, 5}  # True

# >= 检查一个集合是否是另一个的超集
# > 检查一个集合是否是另一个的真超集
print('result =', result)
