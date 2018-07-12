class NPC:
    kexuan = []
    def __init__(self, id, name, jianjie):
        self.name = name
        self.jianjie = jianjie
        self.id = id
        str = self.id+"   "+self.name+"   "+self.jianjie
        NPC.kexuan.append(str)
