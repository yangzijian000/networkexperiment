# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 89, 23))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 89, 23))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 89, 23))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 89, 23))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(150, 120, 89, 23))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 120, 89, 23))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 89, 23))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(150, 200, 89, 23))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(280, 200, 89, 21))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "组员"))
        self.label_2.setText(_translate("Form", "杨子健"))
        self.label_3.setText(_translate("Form", "王鑫"))
        self.label_4.setText(_translate("Form", "付淼淼"))
        self.label_5.setText(_translate("Form", "任浩"))
        self.label_6.setText(_translate("Form", "林敬"))
        self.label_7.setText(_translate("Form", "王霞"))
        self.label_8.setText(_translate("Form", "马利芬"))
        self.label_9.setText(_translate("Form", "吴楚欣"))
        self.label_10.setText(_translate("Form", "沈秋翔"))

