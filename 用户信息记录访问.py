# -*- coding: utf-8 -*-

#主界面
def get_main_screen():
    print('*'*26)
    print(' '*5+'名片管理系统v1.3\n')
    print(' '*5+'1.新建名片')
    print(' '*5+'2.显示全部名片')
    print(' '*5+'3.查询名片\n')
    print(' '*5+'0.退出系统')
    print('*'*26)
    
#获取储存用户的数据，返回users_lib字典
def load_users_lib():
    dic = {}
    if os.path.exists(r'F:\test\users.json') == False:
        os.makedirs(r'F:\test')  #创建路径所需的文件夹
        with open(r'F:\test\users.json','a') as obj:  #没有users.json文件则创建一个，并写入一个空字典
            json.dump(dic,obj)     
    with open(r'F:\test\users.json') as obj:
        users_lib = json.load(obj)  #读取用户数据并保存在字典users_lib中   
    return users_lib
         
#写入用户信息到users.json中
def write_user_info(users_lib):
    with open(r'F:\test\users.json','w') as obj:
        json.dump(users_lib,obj)

#操作确认
def check_status(status):
    print('您选择的操作是：' + str(status))
    print('-'*20)
    
#新建名片，返回用户信息和用于查询的姓名
def create_new_card():
    key_info = ('姓名','电话','QQ','邮箱')
    user_info = {}
    cancel =0  #用于判断用户是否终止新建操作
    for key in key_info:
        if key == '邮箱':  #邮箱单独处理，因为不限制字符串长度
            user_info[key] = input('请输入邮箱（输入0取消该次新建操作）：')
            if user_info[key] == '0':  #终止新建操作时
                user_info['姓名'] = ''
                cancel = 1
                break
        else:
            check = input('请输入'+key+'（不多于15个字符，输入0取消该次新建操作）：')
            if check == '0': #终止新建操作时
                user_info['姓名'] = ''  #防止返回的user_info['姓名']报错
                cancel = 1
                break
            else:  #正常操作时
                while True:
                    if len(check) >= 15:  #输入的字符串不符合长度时
                        print('请限制在15个字符内')
                    else:
                        user_info[key] = check
                        break
    return user_info['姓名'], user_info, cancel

#用户列表
def list_users(users_lib):
    key_info = ('姓名','电话','QQ','邮箱')
    #打印表头
    for k in key_info:  
        if k == 'QQ':  #中文每个字符占据的位置相当于英文两个字符
            print(k, end=' '*13)
        else:
            print(k, end=' '*11)
    print('\n',end='')
    print('-'*70)  #表头分隔符
    
    #打印内容
    for cards in users_lib.values():
        for info_key, info_value in cards.items():
            if  info_key == '邮箱':
                print(info_value, end='')
            else:
                print('%-15s' % info_value, end='')  #占位为15个字符
        print()
    print('-'*70)  #表尾分隔符

#修改用户信息，返回新的姓名和新的用户信息
def alter_user_info(user_info):
    new_user_info = {}
    for key,value in user_info.items():
        new_value = input('请输入'+ key +'[回车不修改]：')
        if new_value == '':
            new_user_info[key] = value
        else:
            new_user_info[key] = new_value
    return new_user_info['姓名'],new_user_info
    
#主程序
import json,os

while True:
    users_lib = load_users_lib()  #加载用户数据
    get_main_screen()  #打印主界面
    main_status = input('请选择操作功能: ')
    
    #主界面选择分支
    #1.退出程序
    if main_status == '0':
        check_status(main_status)
        print('功能：退出程序')
        print('感谢使用')
        print('\n')
        break
    
    #2.新建名片
    elif main_status == '1': 
        check_status(main_status)
        print('功能：新建名片')
        user_name,user_info,cancel = create_new_card()  #获取新用户信息
        if cancel == 1:  #用户终止了输入，不保存
            print('\n')
            continue
        else:  #用户正常输入
            users_lib[user_name] = user_info
            write_user_info(users_lib)  #将新用户信息保存到users.json中
            print('用户创建成功！')
            print('\n')
    
    #3.显示全部
    elif main_status == '2':
        check_status(main_status)
        print('功能：显示全部名片')
        if users_lib == {}:  #用户数据为空
            print('提示：没有任何名片记录,请新建名片')
            continue
        else:  #用户数据不为空
            list_users(users_lib)
            while True:  
                ops_2 = input('0：返回上一个界面\n1：删除所有名片\n您希望的操作是：')
                if ops_2 == '0':  #返回上一个界面
                    break
                elif ops_2 == '1':  #删除所有名片
                    while True:
                        ops_1 = input('您确定要删除所有名片吗？\nyes：继续\nno：终止\n你希望的操作是：')
                        if ops_1 == 'yes':  #确定删除
                            users_lib = {}
                            write_user_info(users_lib)
                            print('已删除所有名片！')
                            break
                        elif ops_1 == 'no':  #放弃删除
                            break
                        else:
                            print('请输入"yes"或者"no"!')
                    break
                else:
                    print('请从上述选项中选择！')
            print('\n')
     
    #4.查询名片
    elif main_status == '3': 
        check_status(main_status)
        while True:
            print('功能：查询名片')
            inq_name = input('请输入要查找的姓名（输入0返回上一个界面）：')
            if inq_name == '0':  #返回上一个界面
                print('\n')
                break
            else:  #查找用户姓名
                if inq_name in users_lib.keys():  #用户姓名输入正确且存在时
                    inq_user_info = {inq_name:users_lib[inq_name]}
                    list_users(inq_user_info)
                    while True:  
                        ops = input('可通过以下方式对名片进行操作：\n1：修改\n2：删除\n0返回上一个界面\n您希望的操作是：')
                        if ops == '1':  #修改用户信息
                            new_name, new_info = alter_user_info(users_lib[inq_name])
                            del users_lib[inq_name]
                            users_lib[new_name] = new_info
                            write_user_info(users_lib)
                            print(inq_name+'的名片修改成功')
                            break
                        elif ops == '2':  #删除用户信息并重新保存全部用户数据
                            del users_lib[inq_name]
                            write_user_info(users_lib)
                            print('删除成功')
                            break 
                        elif ops =='0':  #放弃操作
                            break
                        else:
                            print('请从上述选项中选择！')
                            continue
                else:
                    print('该用户不存在！可使用“显示全部名片”功能确定用户姓名')
            print('\n')
        
    else:
        print('请从上述选项中选择！')