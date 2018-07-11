# 列表（list）标志：[]
# 增加：append  insert   extend
list1 = [0, 1, 2, 3]
list1.append(4)
print(list1)
# 得到[0, 1, 2, 3, 4]，在尾部添加一个元素，只能添加一个
list1 = [0, 1, 2, 3]
list1.extend(["a", "b"])
print(list1)
# 得到[0, 1, 2, 3, 'a', 'b']，在尾部添加多个元素（数据）
list1 = [0, 1, 2, 3]
list1.insert(2, "a")
print(list1)
# 得到[0, 1, 'a', 2, 3]，在指定位置添加元素

# 删除：remove （根据元素）  pop（根据下标，默认从最后一个） clear
list1 = ["a", "b", "c", "d"]
list1.pop()
print(list1)
# 得到['a', 'b', 'c']，默认删除最后一个
list1 = ["a", "b", "c", "d"]
list1.pop(2)
print(list1)
# 得到['a', 'b', 'd']，根据下标去删除，删除指定位置元素，在索引范围内
list1 = ["a", "b", "c", "d"]
list1.remove("b")
print(list1)
# 得到['a', 'c', 'd']，删除指定元素
list1 = ["a", "b", "c", "d"]
list1.clear()
print(list1)
# 得到[]，清空列表

# 修改：[]
list1 = ["a", "b", "c", "d"]
list1[2] = "w"
print(list1)
# 得到['a', 'b', 'w', 'd']，根据下标修改数据

# 查找：len   index   count
list1 = ["a", "b", "c", "d"]
print(len(list1))
# 得到4，输出列表中元素的个数
print(list1.index("b"))
# 得到1，查询指定元素的下标
list1 = ["a", "b", "c", "c", "d",]
print(list1.count("c"))
# 得到2，查询某个元素出现的次数

# 排序：sort 默认是升序   reverse倒序
list1 = [10, 5, 2, 4, 1]
list1.reverse()
# 得到[1, 4, 2, 5, 10]，倒序输出，按照输入的顺序的倒叙
print(list1)
list1.sort()
# 得到[1, 2, 4, 5, 10]，升序输出（从小到大）
print(list)

# 遍历：while   for   迭代器
# for循环
list1 = ["a", "b", "c"]
for i in list1:
    print(i)

# while循环
list1 = ["a", "b", "c"]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# 迭代器
list1 = ["a", "b", "c"]
list2 = iter(list1)
print(next(list2))
print(next(list2))
print(next(list2))
'''
得到:a，
     b
     c
'''
