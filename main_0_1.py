import os
import subprocess
from tkinter import *
from tkinter import filedialog


# apt-get install python3-modules-tkinter


def browse_cer(): #[V]
    filename = filedialog.askopenfilename(initialdir="~/",
                                          title="Select a File",
                                          filetypes=(("Сертификаты",
                                                      "*.cer"),
                                                     ("Все файлы", "*.*")))
    filename = filename.replace(' ', '\ ')
    path_cer['text'] = filename


def get_list_cont(): #[V]
    csptest = os.popen('/opt/cprocsp/bin/amd64/csptest -keyset -enum_cont -fqcn -verifyc -uniq | iconv -f cp1251').read()
    csptest=str(csptest)
    #print(csptest)
    list = csptest.split('\n')
    strings_with_substring = [string for string in list if "FLASH" in string]
    info_cont.delete(1.0, END)
    for i in range(0, len(strings_with_substring)):
        pos = strings_with_substring[i].find('|')
        info_cont.insert(1.0, strings_with_substring[i]+'\n')
        strings_with_substring[i] = strings_with_substring[i][pos + 1:]
        #strings_with_substring[i] = strings_with_substring[i].replace('\\', '\\\\', 2)

    list_cont.delete(0, 'end')
    for i in strings_with_substring:
        list_cont.insert(END, i)


def install_cert_into_cont(): #[v]
    textt = path_cer.cget("text")
    command_shell = "/opt/cprocsp/bin/amd64/certmgr -inst -store uMy -file " + textt + " -cont '" + list_cont.get(ACTIVE) + "'"
    try_cmd(command_shell)


def bind_cont_to_cert(): #[v]
    command_shell = "/opt/cprocsp/bin/amd64/csptestf -absorb -certs -autoprov"
    try_cmd(command_shell)


def install_local_cert(): #[v]
    textt = path_cer.cget("text")
    command_shell = "/opt/cprocsp/bin/amd64/certmgr -inst -file " + textt + " -store uMy"
    try_cmd(command_shell)

def try_cmd(cmd): #[v]
    try:
        outpu = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        output.insert(END, "ERRRRORRRR")
        output.insert(END, exc.output)
    else:
        output.insert(END, "NOOOORM")
        output.insert(END, format(outpu))

    output.insert(END, "*************************************************************************************************************\n"
                       "*************************************************************************************************************\n")
    # ErrorCode
    # [ErrorCode: 0x00000667] Сертификат не найден для установки
    # [ErrorCode: 0x80090016] Контейнер не выбран
    # [ErrorCode: 0x8009001a] Контейнер не найден
    # ПРИВЯЗАТЬ -> No containers. [ErrorCode: 0x00000000]    Контейнер не вставлен в ПК

def view_cryptopro_lic(): #[V]
    command_shell = "/opt/cprocsp/sbin/amd64/cpconfig -license -view"
    try_cmd(command_shell)


def view_local_certs(): #[V]
    command_shell = "/opt/cprocsp/bin/amd64/certmgr -list -store uMy"
    try_cmd(command_shell)

def view_certs_in_cont(): #[v]
    command_shell = "/opt/cprocsp/bin/amd64/csptest -keyset -check -cont '" + list_cont.get(ACTIVE) + "'  | iconv -f cp1251"
    try_cmd(command_shell)

# Create the root window
window = Tk()
window.title('Certificate Manager by Bilas D.E.')
window.geometry("800x940")
window.resizable(width=0, height=0)
window.config(background="white")

path_cer = Label(window, width=100, height=2)
button_browse_cer = Button(window,
                        text="Загрузить сертификат",
                        command=browse_cer)
button_get_list_cont = Button(window,
                         text="Список контейнеров",
                         command=get_list_cont)

list_cont = Listbox(window, width=100)

info_cont = Text(window, width=100, height=6)

button_install_cert_into_cont= Button(window,
                        text="Записать сертификат в контейнер",
                        command=install_cert_into_cont)

button_bind_cont_to_cert= Button(window,
                       text="Привязать сертификат к контейнеру",
                       command=bind_cont_to_cert)

button_install = Button(window,
                        text="Установить сертификат на ПК",
                        command=install_local_cert)
button_view_cryptopro_lic = Button(window,
                         text="Посмотреть лицензию",
                         command=view_cryptopro_lic)
button_view_local_certs = Button(window,
                           text="Посмотреть личные сертификаты",
                           command=view_local_certs)

button_view_certs_in_cont = Button(window,
                           text="Посмотреть сертификаты в контейнере",
                           command=view_certs_in_cont)


output = Text(window, width=110, height=25)
button_exit = Button(window,
                     text="Выход",
                     command=exit)

path_cer.grid(column=1, row=1)
button_browse_cer.grid(column=1, row=2)
button_get_list_cont.grid(column=1, row=3)
list_cont.grid(column=1, row=4)
info_cont.grid(column=1, row=5)
button_install_cert_into_cont.grid(column=1, row=6)
button_bind_cont_to_cert.grid(column=1, row=7)
button_install.grid(column=1, row=8)
button_view_cryptopro_lic.grid(column=1, row=9)
button_view_local_certs.grid(column=1, row=10)
button_view_certs_in_cont.grid(column=1, row=11)



output.grid(column=1, row=12)
button_exit.grid(column=1, row=13)
# Let the window wait for any events
window.mainloop()
###/var/opt/cprocsp/keys/biryukova
###/opt/cprocsp/bin/amd64/csptest -keycopy -contsrc '\\.\HDIMAGE\HDIMAGE\\mgedhaqv.000\1D9D' -contdest '\\.\FLASH\FLASH\\mgedhaqv.000\1D9D
