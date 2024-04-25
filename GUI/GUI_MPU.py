# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_MPU.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from QCustomPlot_PyQt5 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1658, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 181, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 32, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 62, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_connect = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_connect.setGeometry(QtCore.QRect(40, 90, 93, 28))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.comboBox_port = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_port.setGeometry(QtCore.QRect(90, 20, 73, 22))
        self.comboBox_port.setObjectName("comboBox_port")
        self.comboBox_baudrate = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_baudrate.setGeometry(QtCore.QRect(90, 50, 73, 22))
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.roll_txt = QtWidgets.QTextBrowser(self.centralwidget)
        self.roll_txt.setGeometry(QtCore.QRect(310, 50, 111, 31))
        self.roll_txt.setObjectName("roll_txt")
        self.pitch_txt = QtWidgets.QTextBrowser(self.centralwidget)
        self.pitch_txt.setGeometry(QtCore.QRect(310, 90, 111, 31))
        self.pitch_txt.setObjectName("pitch_txt")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 60, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 100, 55, 16))
        self.label_7.setObjectName("label_7")
        self.yaw_txt = QtWidgets.QTextBrowser(self.centralwidget)
        self.yaw_txt.setGeometry(QtCore.QRect(310, 130, 111, 31))
        self.yaw_txt.setObjectName("yaw_txt")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 140, 55, 16))
        self.label_8.setObjectName("label_8")
        self.receive_txt = QtWidgets.QTextBrowser(self.centralwidget)
        self.receive_txt.setGeometry(QtCore.QRect(220, 200, 256, 192))
        self.receive_txt.setObjectName("receive_txt")
        self.plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plot_btn.setGeometry(QtCore.QRect(590, 340, 93, 28))
        self.plot_btn.setObjectName("plot_btn")
        self.stop_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_plot_btn.setGeometry(QtCore.QRect(720, 340, 93, 28))
        self.stop_plot_btn.setObjectName("stop_plot_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1658, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.plot_widget1 = QCustomPlot(self.centralwidget)
        self.plot_widget1.setGeometry(QtCore.QRect(700, 10, 880, 190))
        self.plot_widget1.setAutoFillBackground(False)
        self.plot_widget1.xAxis.setLabel("Time (s)")
        self.plot_widget1.yAxis.setLabel("Value Degree")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Serial"))
        self.label.setText(_translate("MainWindow", "PORT"))
        self.label_2.setText(_translate("MainWindow", "BAUDRATE"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.label_6.setText(_translate("MainWindow", "ROLL"))
        self.label_7.setText(_translate("MainWindow", "PITCH"))
        self.label_8.setText(_translate("MainWindow", "YAW"))
        self.plot_btn.setText(_translate("MainWindow", "Plot"))
        self.stop_plot_btn.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())