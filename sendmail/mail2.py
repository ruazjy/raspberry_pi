from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


# 邮件主题，收件人名字显示为友好的名字 明明收到了邮件，却提示不再收件人中
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# from_addr = input('From:')
# password = input('Password')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')

from_addr = '331182615@qq.com'
password = 'ecsbhfokjcjtbifi'
to_addr = 'tieshuxiaohan@163.com'
smtp_server = 'smtp.qq.com'

# 发送普通的纯文本文件
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 发送html邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')
# 格式化邮件地址
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
