# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sh/PycharmProjects/supertool/button.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 200, 231, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(250, 110, 201, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setObjectName("lcdNumber")
        self.buttonA5 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonA5.setGeometry(QtCore.QRect(340, 330, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonA5.setFont(font)
        self.buttonA5.setObjectName("buttonA5")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(410, 200, 61, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonA6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonA6.sizePolicy().hasHeightForWidth())
        self.buttonA6.setSizePolicy(sizePolicy)
        self.buttonA6.setObjectName("buttonA6")
        self.gridLayout_2.addWidget(self.buttonA6, 0, 0, 1, 1)
        self.buttonA3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonA3.sizePolicy().hasHeightForWidth())
        self.buttonA3.setSizePolicy(sizePolicy)
        self.buttonA3.setObjectName("buttonA3")
        self.gridLayout_2.addWidget(self.buttonA3, 3, 0, 1, 1)
        self.buttonA1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonA1.sizePolicy().hasHeightForWidth())
        self.buttonA1.setSizePolicy(sizePolicy)
        self.buttonA1.setObjectName("buttonA1")
        self.gridLayout_2.addWidget(self.buttonA1, 1, 0, 1, 1)
        self.buttonA2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonA2.sizePolicy().hasHeightForWidth())
        self.buttonA2.setSizePolicy(sizePolicy)
        self.buttonA2.setObjectName("buttonA2")
        self.gridLayout_2.addWidget(self.buttonA2, 2, 0, 1, 1)
        self.buttonA4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonA4.sizePolicy().hasHeightForWidth())
        self.buttonA4.setSizePolicy(sizePolicy)
        self.buttonA4.setObjectName("buttonA4")
        self.gridLayout_2.addWidget(self.buttonA4, 4, 0, 1, 1)
        self.Zero = QtWidgets.QPushButton(self.centralwidget)
        self.Zero.setGeometry(QtCore.QRect(260, 330, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Zero.setFont(font)
        self.Zero.setObjectName("Zero")
        self.exp = QtWidgets.QPushButton(self.centralwidget)
        self.exp.setGeometry(QtCore.QRect(190, 330, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.exp.setFont(font)
        self.exp.setObjectName("exp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonA5.setText(_translate("MainWindow", "="))
        self.buttonA6.setText(_translate("MainWindow", "C"))
        self.buttonA3.setText(_translate("MainWindow", "*"))
        self.buttonA1.setText(_translate("MainWindow", "+"))
        self.buttonA2.setText(_translate("MainWindow", "-"))
        self.buttonA4.setText(_translate("MainWindow", "/"))
        self.Zero.setText(_translate("MainWindow", "0"))
        self.exp.setText(_translate("MainWindow", "exp"))

