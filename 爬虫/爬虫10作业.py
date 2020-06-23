from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() #设置引擎为chrome，从本地打开一个chrome浏览器
driver.get('https://github.com/login') #访问页面，提取页面数据

form = driver.find_element_by_class_name('auth-form-body')
form.find_element_by_id('login_field').clear()
form.find_element_by_id('login_field').send_keys('BJHK')
time.sleep(2)
form.find_element_by_id('password').clear()
form.find_element_by_id('password').send_keys('axB12345678')
time.sleep(2)
form.find_element_by_class_name('btn').click()

time.sleep(3)

driver.close()