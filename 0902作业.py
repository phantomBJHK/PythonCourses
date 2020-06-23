while True:
    a = input('请输入：')
    try:
        b = int(a)
        if (b%2 == 0) or ('7' in a):
            print('是')
            continue
        else:
            print('否')
            continue
    except:
        print('不是数字，请重新输入！')
        continue