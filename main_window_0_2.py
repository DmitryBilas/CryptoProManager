# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_0_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_browse_cer = QtWidgets.QPushButton(self.centralwidget)
        self.button_browse_cer.setGeometry(QtCore.QRect(10, 10, 151, 25))
        self.button_browse_cer.setObjectName("button_browse_cer")
        self.path_cert = QtWidgets.QLabel(self.centralwidget)
        self.path_cert.setGeometry(QtCore.QRect(170, 10, 501, 31))
        self.path_cert.setText("")
        self.path_cert.setObjectName("path_cert")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 340, 53, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 141, 17))
        self.label_3.setObjectName("label_3")
        self.button_view_list_cont = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_list_cont.setGeometry(QtCore.QRect(180, 60, 161, 25))
        self.button_view_list_cont.setObjectName("button_view_list_cont")
        self.button_install_cert_into_cont = QtWidgets.QPushButton(self.centralwidget)
        self.button_install_cert_into_cont.setGeometry(QtCore.QRect(790, 150, 241, 25))
        self.button_install_cert_into_cont.setObjectName("button_install_cert_into_cont")
        self.button_bind_cont_to_cert = QtWidgets.QPushButton(self.centralwidget)
        self.button_bind_cont_to_cert.setGeometry(QtCore.QRect(790, 190, 241, 25))
        self.button_bind_cont_to_cert.setObjectName("button_bind_cont_to_cert")
        self.button_install_local_cert = QtWidgets.QPushButton(self.centralwidget)
        self.button_install_local_cert.setGeometry(QtCore.QRect(790, 220, 241, 25))
        self.button_install_local_cert.setObjectName("button_install_local_cert")
        self.button_view_local_certs = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_local_certs.setGeometry(QtCore.QRect(790, 250, 241, 25))
        self.button_view_local_certs.setObjectName("button_view_local_certs")
        self.button_view_certs_in_cont = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_certs_in_cont.setGeometry(QtCore.QRect(790, 280, 241, 25))
        self.button_view_certs_in_cont.setObjectName("button_view_certs_in_cont")
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(30, 370, 981, 361))
        self.output.setObjectName("output")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(760, 750, 241, 25))
        self.button_exit.setObjectName("button_exit")
        self.list_cont = QtWidgets.QListWidget(self.centralwidget)
        self.list_cont.setGeometry(QtCore.QRect(30, 100, 731, 221))
        self.list_cont.setObjectName("list_cont")
        self.button_view_lic = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_lic.setGeometry(QtCore.QRect(790, 120, 241, 25))
        self.button_view_lic.setObjectName("button_view_lic")
        self.button_clear_output = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_output.setGeometry(QtCore.QRect(30, 750, 131, 25))
        self.button_clear_output.setObjectName("button_clear_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_browse_cer.setText(_translate("MainWindow", "Загрузить сертификат"))
        self.label_2.setText(_translate("MainWindow", "Консоль"))
        self.label_3.setText(_translate("MainWindow", "Список контейнеров:"))
        self.button_view_list_cont.setText(_translate("MainWindow", "Список контейнеров"))
        self.button_install_cert_into_cont.setText(_translate("MainWindow", "Записать сертификат в контейнер"))
        self.button_bind_cont_to_cert.setText(_translate("MainWindow", "Привязать сертификат к контейнеру"))
        self.button_install_local_cert.setText(_translate("MainWindow", "Установить сертификат на ПК"))
        self.button_view_local_certs.setText(_translate("MainWindow", "Посмотреть личные сертификаты"))
        self.button_view_certs_in_cont.setText(_translate("MainWindow", "Посмотреть сертификаты в контейнере"))
        self.button_exit.setText(_translate("MainWindow", "Выход"))
        self.button_view_lic.setText(_translate("MainWindow", "Посмотреть лицензию"))
        self.button_clear_output.setText(_translate("MainWindow", "Очистить консоль"))
        self.menu.setTitle(_translate("MainWindow", "Главная"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Лицензия КриптоПро"))
        self.action_2.setText(_translate("MainWindow", "Лицензия КриптоПро"))
        self.action_3.setText(_translate("MainWindow", "О программе"))
