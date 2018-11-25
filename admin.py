#！/usr/bin/env python
# Author:Hank
'''
4.Admin：

属性：管理员账号、管理员密码

函数：显示系统欢迎界面、验证管理员身份信息、显示系统功能界面
Admin：

属性：管理员账号、管理员密码

函数：显示系统欢迎界面、验证管理员身份信息、显示系统功能界面
'''
import time

class Admin:
    #类属性
    admin='abc'
    password='123'

    #定义函数：显示系统欢迎界面
    def printaDMINvIEW(self):
        print("*****************************************************************")
        print("**")
        print("**")
        print("*欢迎登录汉克银行*")
        print("**")
        print("**")
        print("*****************************************************************")

    #定义函数：显示系统功能界面
    def printSysFuncView(self):
        print("*****************************************************************")
        print("*开户(1)查询(2)*")
        print("*取款(3)存款(4)*")
        print("*转账(5)改密(6)*")
        print("* 解锁(7) 锁定(8) *")
        print("* 退出(t) *")
        print("*****************************************************************")

    #定义函数,验证管理员身份信息
    def adminOption(self):
        #先验证管理员账号，如果账号不正确,函数终止了
        in_admin=input('请输入管理员账号：')
        if in_admin!=self.admin:
            return -1

        #如果程序能够执行到此处，说明账号没有问题，验证密码
        in_password=input('请输入管理员密码：')
        if in_password!=self.password:
            return -1

        #如果程序能够执行到此处，说明身份信息没有问题
        print('操作成功！请稍后...')
        time.sleep(2)
        return 0
