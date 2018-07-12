# 1)✔	创建一个汽车类（Car）有油量和时速2个属性
# 2)✔	写一个显示方法（show）在此方法中输出新车上路，输出当前时速为：+时速，油量为：+油量
# 3)✔	写一个转弯方法（zhuan），在这个方法中将时速固定到20，油量-1 ，调用show方法
# 4)✔	写一个直行的方法（zhi），在这个方法中时速+=10，油量-1，调用show方法
# 5)✔	写一个停车方法，输出：停车
# 6)✔	创建测试类，创建主函数，在主函数中创建一辆车

# 1)✔	创建一个汽车类（Car）有油量和时速2个属性
class Car:


    def __init__(self):
        self.oil = 100
        self.speed = 20
        print("新车上路")

# 2)✔	写一个显示方法（show）在此方法中输出新车上路，输出当前时速为：+时速，油量为：+油量
    def show(self):
        print("当前车速为%d，油量为%d" % (self.speed, self.oil))

# 3)✔	写一个转弯方法（zhuan），在这个方法中将时速固定到20，油量-1 ，调用show方法
    def zhuan(self):
        print("汽车转弯")
        self.speed = 20
        self.oil -= 1
        self.show()

# 4)✔	写一个直行的方法（zhi），在这个方法中时速+=10，油量-1，调用show方法
    def zhi(self):
        print("汽车直行加速")
        self.speed += 10
        self.oil -= 1
        self.show()

# 5)✔	写一个停车方法，输出：停车
    # def stop(self):
    #     print("停车")

    def __del__(self):
        print("停车")


