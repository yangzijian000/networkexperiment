# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from PyQt5 import QtCore, QtGui, QtWidgets
import Email
import team
class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 330)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 100, 261, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 240, 126, 33))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 100, 89, 23))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 261, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 51, 23))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 280, 71, 33))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "邮件客户端登陆"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "用户名:"))
        self.label_2.setText(_translate("Form", "密码:"))
        self.pushButton_2.setText(_translate("Form", "组员"))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.lineEdit_2.returnPressed.connect(self.pushButton_clicked)
    def pushButton_clicked(self):
        try:
            sender = self.lineEdit.text()
            passwd = self.lineEdit_2.text()
            self.hide()
            self.emailDialog = email_senderui(sender,passwd)
            self.emailDialog.show()
        except Exception as e:
            print(e)
    def pushButton_2_clicked(self):
        self.teamDialog = Team()
        self.teamDialog.show()
class email_senderui(QtWidgets.QWidget,Email.Ui_Form):
    def __init__(self,sender,passwd):
        super(email_senderui,self).__init__()
        self.sender = sender
        self.passwd = passwd
        self.rcpt = ''
        self.setupUi(self)
        self.initui()
    def initui(self):
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
    def pushButton_clicked(self):
        self.rcpt = str(self.lineEdit.text())
        self.subject = str(self.lineEdit_2.text())
        self.msg = str(self.textEdit.toPlainText())
        self.senderEmail()
    def pushButton_clicked_2(self):
        self.rcpt = str(self.lineEdit.text())
        self.subject = str(self.lineEdit_2.text())
        self.msg = str(self.textEdit.toPlainText())
        self.sendermail_Enclosure()
        self.pushButton.clicked.disconnect(self.pushButton_clicked_2)
        self.pushButton.clicked.connect(self.pushButton_clicked)
    def pushButton_2_clicked(self):
        self.fnames = QtWidgets.QFileDialog.getOpenFileNames(self,'请选择附件','/.')
        self.pushButton.clicked.disconnect(self.pushButton_clicked)
        self.pushButton.clicked.connect(self.pushButton_clicked_2)
    def senderEmail(self):
        try:
            text = self.msg
            pattern = re.compile(r'@([\S]+)\.com')
            print (type(self.sender))
            match = pattern.search(str(self.sender)).group(1)
            print (match)
            msg=MIMEText(text,'plain','utf-8')#plain是指显示纯文本
            msg['From']=formataddr(["YANGz1J",self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["YANGz1J",self.rcpt])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=self.subject                # 邮件的主题，也可以说是标题
            emailserver = 'smtp.%s.com'%(match)
            server=smtplib.SMTP(emailserver, 25)  # 发件人邮箱中的SMTP服务器，端口是25
            server.set_debuglevel(1)
            server.login(self.sender, self.passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender,self.rcpt,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的
            print(e)

    def sendermail_Enclosure(self):
        try:
            text = self.msg
            msg = MIMEMultipart()
            msg['From'] = formataddr(["YANGz1J", self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["YANGz1J", self.rcpt])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = self.subject  # 邮件的主题，也可以说是标题

            # 邮件正文内容
            msg.attach(MIMEText(text, 'plain', 'utf-8'))


            context_type = {'.tif':'image/tiff', '.avi':'video/avi', '.htm':'text/html','.txt':'text/plain',
                            '.jpg':'image/jpeg','.mp3':'audio/mp3','.PDF':'application/pdf','.pdf':'application/pdf'}
            # 构造附件
            for fname in self.fnames[0]:
                att = MIMEText(open(fname, 'rb').read(),'base64','utf-8')# base64表示MIME的加密方式，是一种8bite编码方式

                print (fname)
                pattern = re.compile(r'/([^/]+(\.[\w]+))')
                match =pattern.search(fname)
                filename = match.group(1)
                filetype = match.group(2)
                print(filename.encode('gbk').decode('gbk'))
                att["Content-Type"] = context_type[filetype]
                content_disposition = 'attachment; filename=%s'%(filename)# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
                #attachment --- 作为附件下载
                print(content_disposition)
                att["Content-Disposition"] = content_disposition
                msg.attach(att)
            pattern = re.compile(r'@([\S]+)\.com')
            print (type(self.sender))
            match = pattern.search(str(self.sender)).group(1)
            print (match)
            emailserver = 'smtp.%s.com' % (match)
            server = smtplib.SMTP(emailserver, 25)  # 发件人邮箱中的SMTP服务器，端口是25
            server.set_debuglevel(1)
            server.login(self.sender, self.passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender, self.rcpt, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的语句
            print (e)

class Team(QtWidgets.QWidget,team.Ui_Form):
    def __init__(self):
        super(Team,self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    EMailclt = Ui_Form()
    EMailclt.show()
    sys.exit(app.exec_())