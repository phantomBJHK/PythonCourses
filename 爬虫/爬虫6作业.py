import requests

headers = {'user-agent': 'Mozzila.5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

for i in range(0,3):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+str(i*20)
    res_movie = requests.get(url, headers = headers)

    json_movie = res_movie.json()
    list_movies = json_movie['subjects']
    for comment in list_movies:
        print(comment['title'])