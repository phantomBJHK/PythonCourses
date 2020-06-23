import sys
contact = {'我我我':'1234556789','他他他':'392817394','你你你':'848271893'}

while True:

    print('''
    =======通讯录管理系统=======
    1.增加姓名和手机
    2.删除姓名
    3.修改手机
    4.查询所有用户
    5.根据姓名查找手机
    6.退出程序''')

    option = int(input('请选择：'))

    if option == 4:
        print(contact)
        continue

    elif option == 6:
        sys.exit()

    elif option == 2:
        name = input('请输入姓名：')
        del contact[name]
        print('已删除'+name)
        
    elif option == 5:
        name = input('请输入姓名：')
        print(name+':'+contact[name])

    elif option == 1 or option == 3:
        name = input('请输入姓名：')
        num = str(input('请输入号码'))
        contact[name] = num
        print(name+':'+num+'已输入')

