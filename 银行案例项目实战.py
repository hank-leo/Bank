#！/usr/bin/env python
# Author:Hank

#在先测试模块中实例化对象,调用功能,完成需求
from admin import Admin
from atm import ATM
import time
import pickle
'''
实例化对象，调用功能，看到效果
'''
def main():

    #实例化Admin对象
    admin=Admin()

    #管理员开机(显示系统欢迎界面)
    admin.printaDMINvIEW()

    #验证管理员身份
    if admin.adminOption():
        return

    '''
    序列化allUsers散装数据到程序中还原成为allUsers对象
    '''
    try:
        with open('allUsers.txt','rb') as fr:
            allUsers=pickle.load(fr)
            print(allUsers)
            #实例化ATM对象
            atm=ATM(allUsers)
    except:
        print('except...')

        #实例化ATM对象
        allUsers={}
        atm=ATM(allUsers)

    while 1:
        #如果程序能够执行到此处说明身份信息没问题
        admin.printSysFuncView()
        num=input('请选择您需要执行的操作...')
        if num=='1':
            atm.createUser()
        elif num=='2':
            atm.searchUserInfo()
        elif num=='3':
            atm.getMoney()
        elif num == '4':
            atm.saveMoney()
        elif num == '5':
            atm.transferMoney()
        elif num == '6':
            atm.updatePWD()
        elif num == '7':
            atm.unlockCard()
        elif num == '8':
            atm.lockCard()
        elif num=='t':
            '''
            对象序列化操作：将allUsers对象数据存储到allUser.txt文件中
            '''
            with open('allUser.txt','wb') as fw:
                pickle.dump(atm.allUsers,fw)
            return

        time.sleep(2)
main()





