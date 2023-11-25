# Date:2023/11/24
# (C)Hongxing

from tkinter import messagebox
from sys import exit
import json

Data = {}
times = {}

def append():
    key = input("请输入标题：")
    val = input("请输入内容：")
    try:
        Data[key] = val
    except:
        print("存入失败")
    finally:
        print("存入成功！")

def query():
    key = input("请输入数据的标题：")
    try:
        out_data = Data[key]
    except:
        print("未找到该数据")
    finally:
        print("数据为：",out_data)

def save_at_json():
    # 写入 JSON 数据
    with open('data.json', 'w') as f:
        json.dump(Data,f)
    print("写入完成！")

def query_all():
    print(Data)

def read_at_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
        Data["at json"] = data

def modify():
    key = input("请输入标题：")
    val = input("请输入修改后的值：")
    try:
        Data[key] = val
    except:
        print("修改失败")
    finally:
        print("修改成功！")

def delete():
    key = input("请输入标题：")
    try:
        del Data[key]
    except:
        print("删除失败")
    finally:
        print("删除成功！")

def quit_system():
    messagebox.showwarning("提示：","请确保数据已保存")
    exit()

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
    print("8、退出系统")
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
        quit_system()
    else:
        print("请输入正确的模式")