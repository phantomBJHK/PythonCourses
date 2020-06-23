from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() #设置引擎为chrome，从本地打开一个chrome浏览器
driver.get('https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html') #访问页面，提取页面数据

time.sleep(3)

get_more = driver.find_element_by_class_name('js_get_more_hot').click()

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') #使用class_name找到评论

print(len(comments))

for i in range(len(comments)):
    comment = comments[i].find_element_by_tag_name('p')
    print('评论' + str(i) + comment.text + '\n-------------------------------------------------------------------')

driver.close()