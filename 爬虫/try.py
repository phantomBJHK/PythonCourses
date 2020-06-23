import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
mailhost='smtp.netvigator.com'
# qqmail = smtplib.SMTP_SSL()
qqmail = smtplib.SMTP_SSL(mailhost)
qqmail.connect(mailhost,465)
time.sleep(2)
qqmail.login('jw78@netvigator.com','Jw97439743')
content= '亲爱的，今天的天气是：'
message = MIMEText(content, 'plain', 'utf-8')
subject = '今日天气预报'
message['Subject'] = Header(subject, 'utf-8')
qqmail.sendmail('jw78@netvigator.com', 'jw78@yahoo.com', message.as_string())
print('邮件发送成功')
qqmail.quit()