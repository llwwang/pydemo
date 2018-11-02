# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL
import smtplib
import random

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')

from_addr = "goldenvenus@qq.com"
password = "*****"
to_addr = "i@leozwang.com"
smtp_server ="smtp.qq.com"
r_a = random.uniform(0, 100)

msg = MIMEText('Hello, This is TBDS Speaking...'+str(r_a) , 'plain', 'utf-8')
msg['From'] = _format_addr(u'TBDSAlert <%s>' % from_addr)
msg['To'] = _format_addr(u'你是 <%s>' % to_addr)
msg['Subject'] = Header(u'来自TBDS的告警……', 'utf-8').encode()

r_a = random.uniform(0, 100)

server = SMTP_SSL(smtp_server)
server.set_debuglevel(1)
#server.ehlo()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()