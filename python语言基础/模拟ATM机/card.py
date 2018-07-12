'''
卡：Card
    属性：卡号，密码，余额，是否锁定 （True锁定了False未锁定）
    行为：
'''
class Card:


    def __init__(self, cardNum, passWord, yu):
        self.cardNum = cardNum
        self.passWord = passWord
        self.yu = yu
        self.isLock = False  # 是否锁定