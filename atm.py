#！/usr/bin/env python
# Author:Hank

import random
from card import Card
from user import User
'''
3.ATM：
属性：字典对象(键：卡号 --> 值：用户)
函数：开户、查询、取款、存款、转账、改密、解锁、锁定
'''
class ATM:

    #构造
    def __init__(self,allUsers):
        # 字典对象-->键：卡号 值：用户
        self.allUsers=allUsers

    #函数/功能
    #开户
    def createUser(self):
        name=input('请输入用户名:')
        idCard=input('请输入身份证号：')
        phone=input('请输入手机号：')
        preStoreMoney=float(input('请输入预存款金额:'))

        #校验预存款金额
        if preStoreMoney<=0:
            print('预存款金额有误！开户失败...')
            return

        #设置密码
        realPasswd=input('请设置密码:')

        #进行密码验证(3次机会)：
        i=3
        while i>0:
            tempPasswd=input('请输入密码：%s次' %i)
            if tempPasswd != realPasswd:
                i -= 1
            else:
                break

        # 判断i中的值，来确定是否3次中有输入对的
        if i==0:
            print('输入密码有误！开户失败...')
            return

        #验证密码
        if not self.checkPWD(realPasswd):
            print('输入密码有误！开户失败...')
            return

        #生成卡号
        cardId=''
        for i in range(6):
            cardId += str(random.randint(0,9))

        cardId=self.createCard()

        #实例化Card对象和User对象
        card=Card(cardId,realPasswd,preStoreMoney)
        user=User(name,phone,idCard,card)

        #填充字典对象
        self.allUsers[cardId]=user

        print('开户成功！请牢记卡号：%s' % cardId)

    #查询
    def searchUserInfo(self):
        #验证卡号是否存在
        user=self.checkCardId()
        card=user.card

        #判断user
        if not user:
            print('此卡号不存在,查询失败...')
            return

        #验证卡的状态
        if card.lockCard:
            print('此卡已被锁定，请解锁再进行相关操作...')
            return

        #如果程序能够执行到此处说明卡号是存在的
        #验证密码
        if not self.checkPWD(card.cardPasswd):
            print('输入密码有误！此卡被锁定...')
            card.lockCard=True
            return

        print('账号:%s 余额：%s' %(card.cardId,card.cardMoney))

    #验证密码
    def checkPWD(self,realPasswd):
        i = 3
        while i > 0:
            tempPasswd= input('请输入密码：(%s)次' %i)

            if tempPasswd == realPasswd:
                return True
            i -= 1
        return False

    #生成卡号：
    def createCard(self):
        while 1:
            str1=""
            for i in range(6):
                str1 += str(random.randint(0,9))
                if str1 not in self.allUsers:
                    return str1

    #验证卡号
    def checkCardId(self):
        cardId=input('请输入卡号：')
        user=self.allUsers.get(cardId)
        return user

    #取款
    def getMoney(self):
        #验证卡号
        user=self.checkCardId()
        if not user:
            print('卡号不存在,取款失败...')
            return

        #验证卡的状态
        if user.card.lockCard:
            print('此卡已被锁定，请解锁再进行相关操作...')
            return

        #验证密码
        if not self.checkPWD(user.card.cardPasswd):
            print('密码有误，此卡被锁定...')
            user.card.lockCard = True
            return

        money = float(input('请输入取款金额：'))

        #验证取款金额
        if money <= 0:
            print('金额有误！取款失败...')
            return
        if money > user.card.cardMoney:
            print('余额不足！取款失败...')
            return

        user.card.cardMoney -= money
        print('取款成功...')

    #存款
    def saveMoney(self):

        # 验证卡号
        user = self.checkCardId()
        if not user:
            print('卡号不存在，存款失败...')
            return

        # 验证卡的状态
        if user.card.lockCard:
            print('此卡已被锁定，请解锁再进行相关操作...')
            return

        # 验证密码：
        if not self.checkPWD(user.card.cardPasswd):
            print('密码有误！此卡被锁定...')
            user.card.lockCard = True
            return

        money = float(input('请输入存款金额...'))

        # 验证money
        if money <= 0:
            print('金额有误！存款失败...')
            return

        user.card.cardMoney += money
        print('存款成功...')

    #转账
    def transferMoney(self):
        outId=input('请输入转出的卡号:')

        #验证转出卡号
        outUser=self.allUsers.get(outId)
        if not outUser:
            print('转出卡号不存在,转账失败...')
            return

        #验证转出卡的状态
        if outUser.card.lockCard:
            print('此卡已被锁定，请解锁再进行相关操作...')
            return

        #验证密码(转出的卡)
        if not self.checkPWD(outUser.card.cardPasswd):
            print('密码有误，此卡被锁定...')
            outUser.card.lockCard = True
            return

        inId=input('请输入转入的卡号：')

        #验证转入卡号
        inUser=self.allUsers.get(inId)
        if not inUser:
            print('转入的卡号不存在,转账失败...')
            return

        #验证转账金额
        money = float(input('请输入转账金额:'))
        if money <= 0:
            print('金额有误！转账失败...')
            return
        if money > outUser.card.cardMoney:
            print('转出卡的余额不足！转账失败...')
            return

        #进行转账操作
        outUser.card.cardMoney -= money
        inUser.card.cardMoney += money
        print('转账成功...')

    #改密
    def updatePWD(self):

        #验证卡号
        user=self.checkCardId()
        if not user:
            print('卡号不存在！改密失败...')
            return

        #验证卡的装填
        if user.card.lockCard:
            print('此卡已被锁定，请解锁再进行相关操作...')
            return

        #验证密码
        if not self.checkPWD(user.card.cardPasswd):
            print('密码有误！此卡被锁定...')
            user.card.lockCard=True
            return

        #设置新密码
        newPWD=input('请设置新的密码...')

        #验证新密码
        if not self.checkPWD(newPWD):
            print('密码有误！改密失败...')
            return

        #开始改密
        user.card.cardPasswd=newPWD

        print('改密成功...')

    #锁定Passwd
    def lockCard(self):

        # 验证卡号:
        user=self.checkCardId()
        if not user:
            print('卡号不存在,锁卡失败...')
            return

        #验证卡的状态
        if user.card.lockCard:
            print('此卡已经被锁定,锁卡失败')
            return

        #验证密码
        if not self.checkPWD(user.card.cardPasswd):
            print('密码有误！锁卡失败...')
            return

        #验证身份证号
        idCard=input('请输入身份证号:')
        if idCard != user.idCard:
            print('身份证信息有误！锁卡失败...')
            return

        #锁上卡
        user.card.lockCard=True

        print('锁卡成功...')

    #解锁
    def unlockCard(self):
        # 验证卡号:
        user = self.checkCardId()
        if not user:
            print('卡号不存在,解锁失败...')
            return

        # 验证卡的状态
        if user.card.lockCard==False:
            print('此卡没有被锁定,解锁失败...')
            return

        # 验证密码
        if not self.checkPWD(user.card.cardPasswd):
            print('密码有误！解锁失败...')
            return

        # 验证身份证号
        idCard = input('请输入身份证号:')
        if idCard != user.idCard:
            print('身份证信息有误！解锁失败...')
            return

        #解开卡
        user.card.lockCard = False
        print('解锁成功...')












