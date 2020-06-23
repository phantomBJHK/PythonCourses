from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() #设置引擎为chrome，从本地打开一个chrome浏览器
driver.get('https://github.com/login') #访问页面，提取页面数据

time.sleep(2)

form = driver.find_element_by_class_name('auth-form-body')
form.find_element_by_id_name('login_field').clear()
form.find_element_by_id_name('login_field').send_keys('BJHK')
time.sleep(2)
form.find_element_by_id_name('password').clear()
form.find_element_by_id_name('password').send_keys('axB12345678')
time.sleep(2)
form.find_element_by_class_name('btn').click()

time.sleep(3)

# driver.get('https://xiaoke.kaikeba.com/example/wordpress/wp-login.php?redirect_to=https%3A%2F%2Fxiaoke.kaikeba.com%2Fexample%2Fwordpress%2F2019%2F10%2F17%2F%25e5%25bc%2580%25e8%25af%25be%25e5%2590%25a7%25e6%2597%25a0%25e6%2595%258c%25e5%25a5%25bd%25e5%2590%2583%25e7%259a%2584%25e9%25a3%259f%25e5%25a0%2582%25e4%25b8%2580%25e5%2591%25a8%25e8%258f%259c%25e8%25b0%25b1%2F')
driver.find_element_by_id('user_login').send_keys('kaikeba')
driver.find_element_by_id('user_pass').send_keys('kaikeba888')
driver.find_element_by_id('wp-submit').click()
time.sleep(3)

comments = 'selenium大法好！123'

write_comments = driver.find_element_by_tag_name('textarea').send_keys(comments)
time.sleep(3)
driver.find_element_by_id('submit').click()
#
#
# print(len(comments))
#
# for i in range(len(comments)):
#     comment = comments[i].find_element_by_tag_name('p')
#     print('评论' + str(i) + comment.text + '\n-------------------------------------------------------------------')

driver.close()