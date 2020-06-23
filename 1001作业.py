def assesment(mark):
    if mark >= 90:
        return 'A'
    elif mark < 60:
        return 'C'
    else:
        return 'B'

while True:
    mark = input('请输入成绩，或输入Q退出程序：')
    if mark == 'Q':
        break

    try:
        mark = float(mark)
    except:
        print('输入错误，请重新输入！')
        continue

    print('您的成绩评级是'+assesment(mark))