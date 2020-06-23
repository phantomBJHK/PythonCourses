film = {
    '速度与激情':['强森','斯坦森'],
    '烈火英雄':['黄晓明','杜江','杨紫'],
    '深夜食堂':['梁家辉','刘涛'],
    '铤而走险':['大鹏','李梦','欧豪'],
    '使徒行者':['张家辉','古天乐']
}

star =input('你想看哪位演员的电影？')
for i in film:
    print(i)
    #actors=film.values()
    if star in film[i]:
        print(star+'出演影片'+i)