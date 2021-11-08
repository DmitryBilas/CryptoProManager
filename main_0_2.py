import os
import subprocess
from tkinter import *
from tkinter import filedialog
from main_window_0_2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys



class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        #BUTTONS
        self.button_browse_cer.clicked.connect(lambda: self.browse_cer())
        self.button_list_of_cont.clicked.connect(lambda: self.get_list_cont())
        self.button_bind_cont_to_cert.clicked.connect(lambda: self.bind_cont_to_cert())
        self.button_get_lic.clicked.connect(lambda: self.get_lic())
        self.button_exit.clicked.connect(app.exit)

    def get_lic(self):
        lic = os.popen(
            '/opt/cprocsp/sbin/amd64/cpconfig -license -view').read()
        lic = str(lic)
        self.output.append(lic)

    def get_list_cont(self):
        csptest = os.popen(
            '/opt/cprocsp/bin/amd64/csptest -keyset -enum_cont -fqcn -verifyc -uniq | iconv -f cp1251').read()
        csptest = str(csptest)
        # print(csptest)
        list = csptest.split('\n')
        strings_with_substring = [string for string in list if "FLASH" or " " in string]

        #info_cont.delete(1.0, END)
        for i in range(0, len(strings_with_substring)):
            pos = strings_with_substring[i].find('|')
            #info_cont.insert(1.0, strings_with_substring[i] + '\n')
            strings_with_substring[i] = strings_with_substring[i][pos + 1:]
            # strings_with_substring[i] = strings_with_substring[i].replace('\\', '\\\\', 2)
        print(strings_with_substring)

        self.list_cont.clearPropertyFlags()
        for i in range(0,self.list_cont.count()):
            self.list_cont.takeItem(0)
        #list_cont.delete(0, 'end')
        for i in strings_with_substring:
            self.list_cont.addItem(i)
            #self.list_of_cont.insert(END, i)


    def browse_cer(self):
        path = QFileDialog.getOpenFileName(self,'Open file','~/',('Cers (*.cer)'))[0]
        path = path.replace(' ', '\ ')
        self.label.setText(path)

    def bind_cont_to_cert(self):
        command_shell = "/opt/cprocsp/bin/amd64/csptestf -absorb -certs -autoprov"
        self.try_cmd(command_shell)

    def try_cmd(self,cmd):
        try:
            outpu = subprocess.check_output(
                cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            #output.insert(END, "ERRRRORRRR")
            #output.insert(END, exc.output)
            self.output.append(exc.output)
        else:
            #output.insert(END, "NOOOORM")
            #output.insert(END, format(outpu))
            self.output.append(format(outpu))

        #output.insert(END,
                     # "*************************************************************************************************************\n"
                     # "*************************************************************************************************************\n")
        # ErrorCode
        # [ErrorCode: 0x00000667] Сертификат не найден для установки
        # [ErrorCode: 0x80090016] Контейнер не выбран
        # [ErrorCode: 0x8009001a] Контейнер не найден
        # ПРИВЯЗАТЬ -> No containers. [ErrorCode: 0x00000000]    Контейнер не вставлен в ПК



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())




