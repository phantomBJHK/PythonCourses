import bs4, requests
start_urls = ['http://duozhi.com/']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
res = requests.get('http://duozhi.com/', headers = headers)

bs = bs4.BeautifulSoup(res.text, 'html.parser')
post_list = bs.find_all('div', class_ = 'post-item')
for post in post_list:
    title = post.find('a', class_ = 'post-title').text
    description = post.find('p', class_ = 'post-desc').text
    print(title, description)
    