#！/usr/bin/env python
# Author:Hank
'''
1.Card：

属性：卡号、密码、余额...

函数：初始化函数(构造)
'''
class Card:
    # 构造
    def __init__(self,cardId,cardPasswd,cardMoney):

        self.cardId=cardId
        self.cardPasswd=cardPasswd
        self.cardMoney=cardMoney

        '''
        定义属性lockCard,接受布尔数据
        譬如：值为True我们可以认为锁定了,值为False认为没有锁定,可以认为lockCard属性是一个开关
        '''
        self.lockCard=False
