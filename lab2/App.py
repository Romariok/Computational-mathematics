# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab2/lab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 888)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 480, 161, 121))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(190, 700, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 380, 611, 321))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 350, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 821, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 160, 789, 169))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.layoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(50, 0, 95, 54))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_10.addWidget(self.lineEdit)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(200, 0, 103, 54))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_11.addWidget(self.lineEdit_2)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(350, 0, 88, 54))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_12.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 291, 61))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 50, 151, 21))
        self.lineEdit_5.setToolTip("")
        self.lineEdit_5.setStatusTip("")
        self.lineEdit_5.setWhatsThis("")
        self.lineEdit_5.setAccessibleName("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 100, 191, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(530, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(69, 79, 41, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(199, 9, 151, 131))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(569, 9, 231, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(-1, -1, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(389, -1, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(440, 80, 41, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(220, 100, 41, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(160, 0, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 160, 789, 169))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.widget_4)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(29, 0, 162, 54))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem3)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_13.addWidget(self.lineEdit_11)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.widget_4)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(200, 0, 162, 54))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_14.addWidget(self.label_18)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem4)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_14.addWidget(self.lineEdit_12)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.widget_4)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(370, 0, 88, 54))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem5)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_15.addWidget(self.lineEdit_13)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 100, 271, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(540, 50, 151, 21))
        self.lineEdit_14.setToolTip("")
        self.lineEdit_14.setStatusTip("")
        self.lineEdit_14.setWhatsThis("")
        self.lineEdit_14.setAccessibleName("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_8.setGeometry(QtCore.QRect(520, 100, 191, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(530, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(520, 10, 161, 111))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 740, 611, 101))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная 2"))
        self.pushButton_2.setText(_translate("MainWindow", "Посмотреть график"))
        self.label_13.setText(_translate("MainWindow", "Результат выполнения"))
        self.label_5.setText(_translate("MainWindow", "Таблица"))
        self.label_10.setText(_translate("MainWindow", "Левая граница"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.label_11.setText(_translate("MainWindow", "Правая граница"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.label_12.setText(_translate("MainWindow", "Погрешность"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.pushButton.setText(_translate("MainWindow", "Решить"))
        self.lineEdit_5.setText(_translate("MainWindow", "lab2/input.txt"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Путь до файла"))
        self.pushButton_3.setText(_translate("MainWindow", "Решить"))
        self.label_6.setText(_translate("MainWindow", "Данные из файла"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1)5.15x</span><span style=\" font-size:10pt; vertical-align:super;\">3</span><span style=\" font-size:10pt;\">-6.25x</span><span style=\" font-size:10pt; vertical-align:super;\">2</span><span style=\" font-size:10pt;\">-0.35x+5.11</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2)x</span><span style=\" font-size:10pt; vertical-align:super;\">3</span><span style=\" font-size:10pt;\">+x+4.4=0               </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3)exp(x*2.11)-5=0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4)sin(3+x)+5.1*x-2</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Метод Хорд</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) Метод Ньютона</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) Метод Простых Итераций</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Выбор функции"))
        self.label_15.setText(_translate("MainWindow", "Выбор метода"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Нелинейное уравнение"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.label_16.setText(_translate("MainWindow", "Выбор систем"))
        self.label_17.setText(_translate("MainWindow", "(1) Первое приближение"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.label_18.setText(_translate("MainWindow", "(2) Первое приближение"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.label_19.setText(_translate("MainWindow", "Погрешность"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.pushButton_7.setText(_translate("MainWindow", "Решить"))
        self.lineEdit_14.setText(_translate("MainWindow", "lab2/input1.txt"))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "Путь до файла"))
        self.pushButton_8.setText(_translate("MainWindow", "Решить"))
        self.label_7.setText(_translate("MainWindow", "Данные из файла"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) sin(y)-2x=2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    cos(x+0.5)+y=1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) sin(x+1)-y=1.2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2x+cos(y)=2</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Система Нелинейных уравнений"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
