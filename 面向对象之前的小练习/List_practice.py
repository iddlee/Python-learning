'''编写程序，用户输入一个列表和2个整数作为下标，
然后使用切片获取并输出列表中介于2个下标之间的元素组成的子列表。
例如用户输入[1, 2, 3, 4, 5, 6]和2,5，程序输出[3, 4, 5, 6]
'''

entry = input("请输入列表：")
list1 = entry.split(",")
entry2 = input("请输入两个整数：")
list_xb = entry2.split(",")
subscript = list1[int(list_xb[0]):int(list_xb[1])]  # 取下标，从list_xb中，取第1个和第二个数字的范围
bianli = []
for i in subscript:
    j = int(i)
    bianli.append(j)
print(bianli)