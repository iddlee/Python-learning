# 编写程序，生成包含1000个“0到100之间”的随机整数，并统计每个元素的出现次数

import random
list1 = []
for i in range(1, 1001):
    R_num = random.randint(0, 100)
    list1.append(R_num)
    # 将生成的随机数添加到列表里
print(list1)
for i in range(0, 101):
    cs = list1.count(i)
    print("数字%d出现%d次" % (i, cs))