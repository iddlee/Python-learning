from npc import NPC
class Player:
    def __init__(self):
        self.dangqian = []

    def add_npc(self,):
        id = input("请输入你要选择的队伍")
        if id == "1":
            self.dangqian.append(NPC.kexuan[0])
        elif id == "2":
            self.dangqian.append(NPC.kexuan[1])
        elif id == "3":
            self.dangqian.append(NPC.kexuan[2])
        else:
            print("没有此编号")

    def remove_npc(self):
        id = input("请输入你要选择的队伍")
        if id == "1":
            self.dangqian.pop(0)
        elif id == "2":
            self.dangqian.pop(1)
        elif id == "3":
            self.dangqian.pop(2)
        else:
            print("没有此编号")

    def show(self):
        print("当前列表有:")
        for i in self.dangqian:
            print(i)
