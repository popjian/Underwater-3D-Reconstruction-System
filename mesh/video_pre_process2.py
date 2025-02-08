# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_pre_process.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 173)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 130, 71, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 130, 101, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(100, 30, 91, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 30, 91, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 20))
        self.label.setObjectName("label")
        self.horizontalSliderConf = QtWidgets.QSlider(Form)
        self.horizontalSliderConf.setGeometry(QtCore.QRect(100, 81, 131, 21))
        self.horizontalSliderConf.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderConf.setObjectName("horizontalSliderConf")
        self.confValue = QtWidgets.QLineEdit(Form)
        self.confValue.setGeometry(QtCore.QRect(240, 81, 61, 20))
        self.confValue.setMaximumSize(QtCore.QSize(70, 16777215))
        self.confValue.setObjectName("confValue")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 72, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "视频分割"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.pushButton_2.setText(_translate("Form", "开始视频分割"))
        self.radioButton.setText(_translate("Form", "单目相机"))
        self.radioButton_2.setText(_translate("Form", "双目相机"))
        self.label.setText(_translate("Form", "相机类型："))
        self.label_2.setText(_translate("Form", "间隔帧率："))

