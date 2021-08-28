# 字典属于一种新的数据结构，称为映射(mapping)
# 字典的作用和列表类似，都是用来存储对象的容器
# 列表存储数据的性能很好，查询数据的性能很差

# 使用{}创建字典
d = {} # 创建一个空字典

# 创建一个有数据的字典
# 字典的值可以是任意对象
# 字典的key可以是任意的不可变对象
# 与Java的Map相同，字典的key也是不允许相同的；如果出现重复的，后面的数据会替换前面的数据
d = {'name':'张益达','age':25,'gender':'男'}
print(d,type(d))

# 直接使用key来获取值
# 但是获取一个不存在的key会直接报错 KeyError
print(d['name'])  

# 也可以使用dict()创建字典（key都是字符串）
dic = dict(name='张益达',age=18,height=1.81)
print(dic)

# 可以将只包含双值子序列转换为字典
dic = dict([('name','张益达'),('age',18)])
print(dic)

# 使用len()检查字典中键值对的个数
print(len(dic))

# 使用in或者not in判断键知否包含在字典中
print('name' in dic)

# 还可以使用get来获取元素
print(dic.get("age1")) # 当元素不存在的时候不会报错，会返回一个None
# 还可以指定默认值
print(dic.get("age1",19))

# 修改字典中元素
dic['name'] = '张大炮'
dic['address'] = '爱情公寓' # 当key在原来的字典中不存在的时候，会视为新增元素

# setdefault(key[, default]) 可以用来向字典中添加key-value，只有在key不存在的时候生效
# 其实类似Java的putIfAbsent方法
dic.setdefault('name','吕子乔')
dic.setdefault('hello','你好')
print(dic)

# update([other]) 使用来自 other 的键/值对更新字典，覆盖原有的键。 返回 None。
d = {'a':1,'b':'python','c':18.9}
d2 = {'a':'hello','b':2,'f':['ab','bc']}
d.update(d2)
print(d)

# del删除元素
del d['a'] # key不存在也会 抛出KeyError异常
print(d)

# popitem() 随机删除字典中的键值对，但是一般删除的就是最后一个
# 返回值就是包含两个元素的元组，分别是key和value
# 删除一个空字典的时候，会抛出字典为空的异常
t = dic.popitem()
print(dic)
print(t)

# pop(key[, default])
# 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError。
# 返回值是value
d = {'a':1,'b':'python','c':18.9}
value = d.pop('f',(1,2))
print(value)

# clear()用来清空字典

# copy() 浅复制（拷贝）字典
# 只会简单的复制原对象内部的值，但是如果值是一个可变对象，这个可变对象不会被复制

# 下面是遍历字典的几个方法
d = {'name':'曾小贤','age':18,'gender':'男'}
# 通过遍历keys()来获取所有的键
# for k in d.keys() :
#     print(k , d[k])

# values()
# 该方法会返回一个序列，序列中保存有字典的左右的值
# for v in d.values():
#     print(v)

# items()
# 该方法会返回字典中所有的项
# 它会返回一个序列，序列中包含有双值子序列
# 双值分别是，字典中的key和value
# print(d.items())
for k,v in d.items() :
    print(k , '=' , v)