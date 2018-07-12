# 字典（dict）标志:{}
# 增加：根据键增加[]    update(合并)
dict1 = {1: "a", 2: "b", 3: "c"}
dict1[4] = "Hello"
print(dict1)
# 得到{1: 'a', 2: 'b', 3: 'c', 4: 'Hello'}，根据键添加值

dict1 = {1: "a"}
dict2 = {2: "b"}
dict1.update(dict2)
print(dict1)
# 得到{1: 'a', 2: 'b'}，将dict2的内容合并到dict1中

# 删除：pop   clear
dict1 = {1: "a", 2: "b", 3: "c"}
dict1.pop(2)
print(dict1)
# 得到{1: 'a', 3: 'c'}，根据键删除值

dict1 = {1: "a", 2: "b", 3: "c"}
dict1.clear()
print(dict1)
# 得到{}，清空

# 修改：[]
dict1 = {1: "a", 2: "b", 3: "c"}
dict1[2] = "Hello"
print(dict1)
# 得到{1: 'a', 2: 'hello', 3: 'c'}，根据键修改值

# 查找：[]   get
dict1 = {1: "a", 2: "b", 3: "c"}
print(dict1.get(3))
# 得到c，通过get（键）得到对应的值

# 遍历：遍历键   遍历值   遍历键值对items
dict1 = {1: "a", 2: "b", 3: "c"}
for i in dict1:
    print(i)  #默认得到键
    print(dict1[i])  # 通过遍历得到的键，再得到值
'''
输出得到：1
          a
          2
          b
          3
          c
'''

dict1 = {1: "a", 2: "b", 3: "c"}
for i in dict1.keys():  # key就是直接遍历字典的键
    print(i)
'''
输出得到：1
          2
          3
'''

dict1 = {1: "a", 2: "b", 3: "c"}
for i in dict1.values():  # values是直接遍历字典的值
    print(i)
'''
输出得到：a
          b
          c
'''

dict1 = {1: "a", 2: "b", 3: "c"}
for i in dict1.items():
    print(i)  # 通过items可以一次性拿到键和值
'''
输出得到：
        (1, 'a')
        (2, 'b')
        (3, 'c')
'''
