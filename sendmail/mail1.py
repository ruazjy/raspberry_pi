from email.mime.text import MIMEText
import smtplib

# 注意开启注意授权码问题
msg = MIMEText('hello', 'plain', 'utf-8')

# from_addr = input('From:')
# password = input('Password:')
# smtp_server = input('SMTP server:')
# to_addr = input('To:')

from_addr = '331182615@qq.com'
password = 'ecsbhfokjcjtbifi'
smtp_server = 'smtp.qq.com'
to_addr = 'tieshuxiaohan@163.com'

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 特么终于可以了



