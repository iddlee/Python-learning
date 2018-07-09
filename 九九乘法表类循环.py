# *****
#  ****
#   ***
#    **
#     *
a = 1       # 一共有多少行
while a <= 5:
    c = 0   # 一行有多少空格
    while c < a:
        print(" ", end="")
        c += 1
    b = 5   # 一行有多少个*
    while b >= a:
        print("*", end="")
        b -= 1
    print()
    a += 1

# *
# **
# ***
# ****
# *****

j = 1  # j = 1
while j <= 5:  # 1 <= 5
    i = 1  # i = 1
    while i <= j:  # 1 = 1
        print("*", end="")  # *
        i += 1  # i = 2
    print()
    j += 1

# *****
# ****
# ***
# **
# *
a = 1
while a <= 5:
    b = 5
    while b >= a:
        print("*", end="")
        b -= 1
    print()
    a += 1

# *****
# *****
# *****
# *****
# *****

a = 1
while a <= 5:
    b = 5
    while b >= 1:
        print("*", end="")
        b -= 1
    print()
    a += 1

#  九九乘法表
b = 1
while b <= 9:  # 总共多少行
    a = 1
    while a <= b:  # 总共多少列
        print("%d * %d = %d" % (a, b, a * b), end="\t")
        a += 1
    print()
    b += 1
'''
# 1.先分析行

a = 1
while a <= b:
    print("%d * %d = %d" % (a, b, a * b), end="\t")
    a += 1

# 2.再分析列
b= 1
while b <=9:

#3.再将行放在列里
'''