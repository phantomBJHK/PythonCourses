import requests

from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

response = requests.get('https://maoyan.com/board', headers=headers)

bs_movies = BeautifulSoup(response.text,'html.parser')

datas = bs_movies.find_all('div', class_ = "movie-item-info")
print(type(datas), len(datas))
for movie in datas:

    title = movie.find('a').text.replace(' ', '').replace('\n', '')
    star = movie.find('p', class_ = 'star').text.replace(' ', '').replace('\n', '')
    time = movie.find('p', class_ = "releasetime").text.replace(' ', '').replace('\n', '')
    print(title)
    print(star)
    print(time)
    print('')

#print(datas)
#print(bs_movies)
#list_movies= bs_movies.find_all('dd',class_='pl2')

# for movie in list_movies:
#     tag_a = movie.find('a')
#     name = tag_a.text.replace(' ', '').replace('\n', '')
#     # 电影名，使用replace方法去掉多余的空格及换行符
#     url = tag_a['href']
#     # 电影详情页的链接
#     tag_p = movie.find('p', class_='pl')
#     # 提取父级标签中的<p>标签
#     information = tag_p.text.replace(' ', '').replace('\n', '')
#     # 电影基本信息，使用replace方法去掉多余的空格及换行符
#     tag_div = movie.find('div', class_='star clearfix')
#     # 提取父级标签中的<div>标签
#     rating = tag_div.text.replace(' ', '').replace('\n', '')
#     # 电影评分信息，使用replace方法去掉多余的空格及换行符
#     list_all.append([name,url,information,rating])
#     # 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all
#     sheet.append([name,url,information,rating])
# print(list_all)