# -*- coding: utf-8 -*-

#主界面
def get_main_screen():
    print('*'*20)
    print('名片管理系统v1.0\n')
    print('1.新建名片')
    print('2.显示全部名片')
    print('3.查询名片\n')
    print('0.退出系统')
    print('*'*20)
    
#获取储存用户的数据，返回users_lib字典
def load_users_lib():
    import json,os
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
    import json
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
    cancel =0
    for key in key_info:
        if key == '邮箱':
            user_info[key] = input('请输入邮箱（输入0取消该次新建操作）：')
            if user_info[key] == '0':
                user_info['姓名'] = ''
                cancel = 1
                break
        else:
            check = input('请输入'+key+'（不多于15个字符，输入0取消该次新建操作）：')
            if check == '0':
                user_info['姓名'] = ''
                cancel = 1
                break
            else:
                while True:
                    if len(check) >= 15:
                        print('请限制在15个字符内')
                    else:
                        user_info[key] = check
                        break
    return user_info['姓名'], user_info, cancel

#用户列表
def list_users(users_lib):
    key_info = ('姓名','电话','QQ','邮箱')
    for k in key_info:
        if k == 'QQ':  #中文每个字符占据的位置相当于英文两个字符
            print(k, end=' '*13)
        else:
            print(k, end=' '*11)
    print('\n',end='')
    print('-'*70)
    for cards in users_lib.values():
        for info_key, info_value in cards.items():
            if  info_key == '邮箱':
                print(info_value, end='')
            else:
                space_num = 15 - len(info_value)
                print(info_value, end= ' '*space_num)
        print()
    print('-'*70)

#修改用户信息，返回姓名和用户列表
def alter_user_info(user_info):
    new_user_info = {}
    for key,value in user_info.items():
        new_value = input('请输入'+ key +'[回车不修改]：')
        if new_value == '':
            new_user_info[key] = value
        else:
            new_user_info[key] = new_value
    return user_info['姓名'],new_user_info
    
#主程序
while True:
    users_lib = load_users_lib()
    get_main_screen()
    main_status = input('请选择操作功能: ')
    if main_status == '0':  #退出程序
        check_status(main_status)
        print('功能：退出程序')
        print('感谢使用')
        print('\n')
        break
        
    elif main_status == '1':  #新建名片
        check_status(main_status)
        print('功能：新建名片')
        user_name,user_info,cancel = create_new_card()  #新用户信息
        if cancel == 1:
            print('\n')
            continue
        else:
            users_lib[user_name] = user_info
            write_user_info(users_lib)  #将新用户信息保存到users.json中
            print('用户创建成功！')
            print('\n')
        
    elif main_status == '2':  #显示全部
        check_status(main_status)
        print('功能：显示全部名片')
        if users_lib == {}:
            print('提示：没有任何名片记录,请新建名片')
            continue
        else: 
            list_users(users_lib)
            print('\n')
        
    elif main_status == '3':  #查询名片
        check_status(main_status)
        print('功能：查询名片')
        inq_name = input('请输入要查找的姓名（输入0返回上一个界面）：')
        if inq_name == '0':
            print('\n')
            continue
        else:
            if inq_name in users_lib.keys():
                inq_user_info = {inq_name:users_lib[inq_name]}
                list_users(inq_user_info)
                while True:
                    ops = input('可通过以下方式对名片进行操作：1：修改  2：删除  0:返回上级菜单\n您希望的操作是：')
                    if ops == '1':
                        new_name, new_info = alter_user_info(users_lib[inq_name])
                        del users_lib[inq_name]
                        users_lib[new_name] = new_info
                        write_user_info(users_lib)
                        print(inq_name+'的名片修改成功')
                        break
                    elif ops == '2':
                        del users_lib[inq_name]
                        write_user_info(users_lib)
                        print('删除成功')
                        break
                    elif ops =='0':
                        break
                    else:
                        print('请从上述选项中选择！')
                        continue
            
            else:
                print('该用户不存在！可使用“显示全部名片”功能确定用户姓名')
            print('\n')
        
    else:
        print('请从上述选项中选择！')