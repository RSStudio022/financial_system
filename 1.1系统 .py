from tkinter import messagebox
from os import system
from sys import exit
import json

User = {"4qk7unhuy":"iytudnp7e-SYS-FREE","Su":"2012net-FREE"}
User_Level = {"4qk7unhuy":"admin"}
Admin = {"4qk7unhuy":"iytudnp7e-SYS-FREE"}
levels = ["Guest","User","admin"]
Data = {}
times = {}
help_docs = """财政系统
本系统自带Admin用户
注册需填写Admin用户的密码和用户名
Admin用户名初始为系统自动生成
可进行更改
如有bug
可向2955903656@qq.com发送邮件报告
我们会在积累一定数量后进行修复
版本：0.285.954.256"""

def start():#初始化
    with open('Users.json', 'r') as f:
        data = json.load(f)
        User = data

def append():#添加一个数据
    key = input("请输入标题：")
    val = input("请输入内容：")
    try:
        Data[key] = val
    except:
        print("存入失败")
    finally:
        print("存入成功！")

def query():#查询一个数据
    key = input("请输入数据的标题：")
    try:
        out_data = Data[key]
    except:
        print("未找到该数据")
    finally:
        print("数据为：",out_data)

def save_at_json():#保存为json文件
        # 写入 JSON 数据
    with open('data.json', 'w') as f:
        json.dump(Data,f)
        print("写入完成！")

def query_all():#查看所有数据
    print(Data)

def read_at_json():#导入json文件
    with open('data.json', 'r') as f:
        data = json.load(f)
        Data["at json"] = data

def modify():#修改值
    key = input("请输入标题：")
    val = input("请输入修改后的值：")
    try:
        Data[key] = val
    except:
        print("修改失败")
    finally:
        print("修改成功！")

def delete():#删除一个元素
    key = input("请输入标题：")
    try:
        del Data[key]
    except:
        print("删除失败")
    finally:
        print("删除成功！")

def clear_window():#清屏
    system("cls")

def print_help():#显示帮助文档
    print(help_docs)

def quit_system():#退出系统
    with open('Users.json', 'w') as f:#保存用户名单
        json.dump(User,f)
    messagebox.showwarning("提示：","请确保数据已保存")
    exit()

def sys_main():#登录后进入的系统
    while 1:
        print("-----------------------")
        print("|                     |")
        print("| 欢迎使用财务管理系统 |")
        print("|                     |")
        print("-----------------------")
        print("1、添加一个数据")
        print("2、查询一个数据")
        print("3、保存数据到json文件")
        print("4、查看所有数据")
        print("5、读取json数据")
        print("6、修改一个数据")
        print("7、删除一个数据")
        print("8、清屏")
        print("9、查看帮助文档")
        print("10、返回登录界面")
        print("11、退出系统")
        model = input("请输入模式：")
        if model == "1":
            append()
        elif model == "2":
            query()
        elif model == "3":
            save_at_json()
        elif model == "4":
            query_all()
        elif model == "5":
            read_at_json()
        elif model == "6":
            modify()
        elif model == "7":
            delete()
        elif model == "8":
            clear_window()
        elif model == "9":
            print_help()
        elif model == "10":
            login_and_register()
        elif model == "11":
            quit_system()
        else:
            print("请输入正确的模式")

class login_and():
    def register_User():#添加用户
        Admin_name = input("请输入管理员用户名：")
        Admin_Password = input("请输入管理员密码：")
        if (Admin_name == "4qk7unhuy" and Admin_Password == User["4qk7unhuy"]):
            New_User_Name = input("请输入新用户名称：")
            New_User_Password = input("请输入新用户密码：")
            New_User_Level = input("请输入新用户等级：")
            if not(New_User_Level in levels):
                print("等级错误")
            else:
                User[New_User_Name] = New_User_Password
                User_Level[New_User_Name] = New_User_Level
                print("创建成功！")
        else:
            print("错误！")
    def login_User():#登录
        Login_User_Name = input("请输入用户名：")
        Login_User_Password = input("请输入密码：")
        if User[Login_User_Name] == Login_User_Password and Login_User_Name in User:
            print("你好，",Login_User_Name)
            sys_main()
            Now_Users = Login_User_Name
        else:
            print("错误")
    
    def delete_User():#删除用户
        Admin_name = input("请输入管理员用户名：")
        Admin_Password = input("请输入管理员密码：")
        if (User_Level[Admin_name] == "admin" and User[Admin_name] == Admin_Password and Admin_name in User):
            del_User_Name = input("请输入要删除用户的名称：")
            del_User_Password = input("请输入要删除用户的密码：")
            if (del_User_Name in User and User[del_User_Name] == del_User_Password):
                del User[del_User_Name]
                print("删除成功！")
        else:
            print("错误！")

    def modeify_User_Password():#修改用户密码
        modeify_User_Name = input("请输入用户的名称：")
        modeify_User_Password = input("请输入原密码：")
        if (modeify_User_Name in User and User[modeify_User_Name] == modeify_User_Password):
            modeify_User_NewPassword = input("请输入新密码：")
            User[modeify_User_Name] = modeify_User_NewPassword
            print("修改成功！")
        if (User_Level[modeify_User_Name] == "admin"):
            modeify_User_NewPassword = input("请输入新密码：")
            User[modeify_User_Name] = modeify_User_NewPassword
            Admin[modeify_User_Name] = modeify_User_NewPassword
            print("修改成功！")
    def modeify_User_Name():#修改用户名称
        modeify_User_Name = input("请输入用户的名称：")
        modeify_User_Password = input("请输入原密码：")
        if (modeify_User_Name in User and User[modeify_User_Name] == modeify_User_Password):
            modeify_User_NewName = input("请输入新名称：")
            User[modeify_User_NewName] = modeify_User_Password
            print("修改成功！")
        if (User_Level[modeify_User_Name] == "admin"):
            modeify_User_NewPassword = input("请输入名称：")
            User[modeify_User_Name] = modeify_User_NewPassword
            Admin[modeify_User_Name] = modeify_User_NewPassword
            print("修改成功！")

def login_and_register():#登录注册界面
    print("1、注册用户")
    print("2、登录用户")
    print("3、删除用户")
    print("4、修改密码")
    print("5、修改用户名")
    print("6、退出")
    model = input("请输入模式：")
    if model == "1":
        login_and.register_User()
    elif model == "2":
        login_and.login_User()
    elif model == "3":
        login_and.delete_User()
    elif model == "4":
        login_and.modeify_User_Password()
    elif model == "5":
        login_and.modeify_User_Name()
    elif model == "6":
        quit_system()

def main():#主界面
    login_and_register()

while 1:
    main()#调用主界面