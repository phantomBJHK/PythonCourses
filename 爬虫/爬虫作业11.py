import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

pwd = input('请输入密码：')
receiver = input('请输入收件地址：')

def get_weather():

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather1d/101211001.shtml'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    bsdata = BeautifulSoup(res.text, 'html.parser')
    data = bsdata.find('div', class_ = 't').find('ul', class_ = 'clearfix')

    data_time = data.find_all('h1')
    data_tem = data.find_all(class_='tem')
    data_wea = data.find_all(class_='wea')

    return data_time, data_wea, data_tem

def send_email(time, tem, wea, pwd, receiver):
    mailhost='smtp.netvigator.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,465)
    sender = 'jw78@netvigator.com'
    qqmail.login(sender,pwd)
    content= '天气信息：\n'+time[0].text + ' ' + 'tem[0].text' + ' ' + wea[0].text + '\n'+time[1].text + ' ' + 'str(tem[1].text)' + ' ' + wea[1].text
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '天气预报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(sender, recevier, message.as_string())
        return True

    except:
        return False

    qqmail.quit()

def job(pwd = pwd, recevier= receiver):

    print('开始一次发送任务')

    time, wea, tem = get_weather()

    IsSuccess = send_email(time, tem, wea, pwd, recevier) # 这里需要设置发件人的账号密码以及收件人的账号

    while IsSuccess is False:

        print("邮件发送失败，正在尝试重新发送")

        IsSuccess = send_email(tem, tem, wea)

    print('任务完成')



schedule.every().day.at("08:00").do(job)

while True:

    schedule.run_pending()

    time.sleep(1)