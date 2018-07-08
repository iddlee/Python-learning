from npc import NPC
from player import Player
import sys

n = NPC("1", "阿尔萨斯", "使用霜之哀伤的怒火攻击敌人")
n1 = NPC("2", "吉安娜", "使用奥术法术远程打击敌人")
n2 = NPC("3", "乌瑟尔", "使用圣光的力量治愈盟友")
print("可选npc列表")
for i in NPC.kexuan:
    print(i)

p = Player()
while True:
    print("1.添加  2.删除  3.完成")
    bh = input("请输入编号")
    if bh == "1":
        p.add_npc()
        p.show()
    elif bh == "2":
        p.remove_npc()
        p.show()
    elif bh == "3":
        sys.exit()
