print('''给你10个亿你想干什么，你选哪个？
1. 想飞上天和太阳肩并肩；
2. 在天安门前面开游泳馆；
3. 离开地球去宇宙；
4. 拯救中国足球。''')

hobby = int(input('来吧，输入序号：'))
if hobby == 1:
    print('你最好别下来了！')
elif hobby == 2:
    print('别做梦了，可能吗？')
elif hobby == 3:
    print('行，拜拜~')
elif hobby == 4:
    print('这个行，有魄力！')
else:
    print('输入错误，下次再见！')