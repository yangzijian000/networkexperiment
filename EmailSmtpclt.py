# -*- coding: utf-8 -*-
"""
Created on Fri May 05 19:26:13 2017

@author: YANGz1J
"""
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import email
import Email
import team
my_sender='networkexperiment0@163.com'    # 发件人邮箱账号
my_pass = 'qwer1234'              # 发件人邮箱授权码
my_user='networkexperiment0@163.com'      # 收件人邮箱账号，我这边发送给自己
# def mail():
#     ret=True
#     try:
#         msg=MIMEText('计算机网络邮件客户实验','plain','utf-8')#plain是指显示纯文本
#         msg['From']=formataddr(["YANGz1J",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To']=formataddr(["YANGz1J",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject']="计算机网络邮件客户实验"                # 邮件的主题，也可以说是标题
#
#         server=smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
#         server.set_debuglevel(1)
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret=False
#     return ret
# def mail_Enclosure():
#     ret =True
#     try:
#         msg = MIMEMultipart()
#         msg['From']=formataddr(["YANGz1J",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To']=formataddr(["YANGz1J",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject']="计算机网络邮件客户实验"                # 邮件的主题，也可以说是标题
#
#         #邮件正文内容
#         msg.attach(MIMEText('这是计算机网络邮件客户实验 邮件发送测试……', 'plain', 'utf-8'))
#
#         # 构造附件1，传送当前目录下的 TaylorSwift.jpg 文件
#         att1 = MIMEText(open('TaylorSwift.jpg', 'rb').read(), 'base64', 'utf-8')#base64表示MIME的编码方式，是一种8bite编码方式
#         att1["Content-Type"] = 'application/octet-stream'
#         # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#         att1["Content-Disposition"] = 'attachment; filename="TaylorSwift.jpg"'
#         msg.attach(att1)
#         server=smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
#         server.set_debuglevel(1)
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret=False
#     return ret
# ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")
# ret=mail_Enclosure()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")