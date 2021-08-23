# 本代码笔记主要讲解列表相关的方法
stus = ['孙悟空','猪八戒','沙和尚']
print("原列表",stus)

# append() 列表尾部添加一个元素
stus.append("唐僧")
print("append后",stus)

# insert() 指定位置插入一个元素
stus.insert(2,"如来佛祖")
print("insert后",stus)

# extend() 使用新的序列扩展当前序列
stus.extend(["玉皇大帝","紫霞仙子"])
print("extend后",stus)

# clear() 清空序列
# stus.clear()
# print("clear后",stus)

# pop() 根据索引删除并返回指定元素
stu = stus.pop(1) # 不写索引则表示删除最后一个元素
print("pop result is",stu)

# remove() 删除指定值元素，如果有多个相同元素，只会删除第一个
stus.remove("唐僧")
print("remove后",stus)

# reverse() 反转列表
stus.reverse()
print("reverse后",stus)

# sort() 对列表元素进行排序
word_list = list("dafhgfjdshgsdjhsdjk")
print("排序前",word_list)
word_list.sort() # 默认是升序
print("排序后",word_list)
word_list.sort(reverse=True) # 降序排列设置reverse为True即可