'''
编写程序：写一个存书的方法，当用户输入编号和书名，
将编号和书名存入到字典中，当用户输入over的时候就提示：书添加成功，本次录入完毕。
写一个查书的方法，用户输入一个编号就输出对应的书名，如果这个编号不存在就提示没有这本书。
'''
def save():
    while True:
        num = input("请输入编号：")
        if num == "over":
            print("书添加成功，本次录入完毕")
            break
        title = input("请输入书名：")
        book[num] = title
    print(book)

def search():
    while True:
        num = input("请输入你要查询书的编号：")
        if num not in book.keys():
            # if cha in shu.keys() == 0:
            print("这个编号不存在,没有这本书")
        else:
            print(book[num])
        break

book = {}
while True:
    print("**********************")
    print("1.存书\n2.查书\n请选择:")
    print("**********************")
    choice = input()
    if choice == "1":
        save()
    elif choice == "2":
        search()
