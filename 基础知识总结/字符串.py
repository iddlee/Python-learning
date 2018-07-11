# 查找：index  find  count
str1 = "Hello World"
print(str1.index("H"))  # 得到0，返回“H”的下标
print(str1.find("l"))  # 得到2，从左往右返回“l”的下标
print(str1.rfind("l"))  # 得到9，从右往左返回“l”的下标
print(str1.count("l"))  # 得到3，检测l在字符串中出现的次数

# 替换：replace
str1 = "Hello World"
print(str1.replace("Hello", "你好"))
# 得到 你好 World，将Hello替换成你好

# 截取（切片）：[:]包左不包右  [::]冒号后是步长
str1 = "Hello World"
print(str1[2:5])  #得到llo，截取从 2-5 之间的字符串
print(str1[:5])  #得到Hello，截取从 起始-5 之间的字符串
print(str1[2:])  #得到llo World，截取从 2-结束 之间的字符串
print(str1[:5:2])
#冒号后是步长，得到Hlo，以每2个一次，从 起始-5 之间的字符串

# 拼接：join   +
list1 = ['1', '2', '3']
str1 = "-".join(list1)
print(str1)
# 得到1-2-3，将列表中的1，2，3与-拼接到一起

# 拆分：split
str1 = "hello.world"
print(str1.split("."))
#得到['hello', 'world']，通过 . 将字符串拆分成两部分

# 获取长度：len
str1 = "Hello World"
print(len(str1))  #得到11，返回字符串的长度
