import sys
import os
import keyboard
import time
import datetime
import ctypes



def close_window():
    """
    Закрытие окна командной строки
    """
    keyboard.send("alt+space")
    time.sleep(0.2)
    key_step = 0
    while key_step != 5:
        keyboard.send("Down")
        key_step += 1
    keyboard.send("enter")


def device_out(dev_id):
    """
    Процесс авторизации устройства через telnet
    """
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(1.5)
    keyboard.write("telnet 192.168.24.%s" % dev_id)
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.write("root")
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.write("root")
    keyboard.send("enter")
    time.sleep(0.3)


# def video(self):
#     """
#     Видео данного устройства
#     """
#
#     d = self.ui.comboBox_2.currentText()
#     d = int(d) + 20
#     time.sleep(0.2)
#     self.browser.close()
#     self.clear_layout()
#     self.browser = QtWebEngineWidgets.QWebEngineView(self)
#     self.browser.load(QUrl("http://192.168.24.%s" % d))
#     self.ui.gridLayout.addWidget(self.browser)


def terminal_device(d):
    """
    Выбор терминала (кассы) для перезапуска в comboBox и преобразование его
    в нужный IP адресс, далее через командную строку переходи в telnet
    и перезапускаем устройство с помощью автоматического ввода пароля
    логина и команды перезагрузки в Cmd
    """

    d = int(d)
    d = d % 100 + 60
    device_out(d)
    keyboard.write("reboot")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    close_window()


def barrier_device(d):
    """
    Выбор терминала (стойки) для перезапуска в comboBox и преобразование его
    в нужный IP адресс, далее через командную строку переходи в telnet
    и перезапускаем устройство с помощью автоматического ввода пароля
    логина и команды перезагрузки в Cmd
    """
    d = int(d)
    device_out(d)
    keyboard.write("reboot")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    close_window()


def network_test_terminal(d):
    """
    Пинг тест данного устройства
    """
    d = int(d)
    d = d % 100 + 60
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(1.5)
    keyboard.write("ping 192.168.24.%s -t" % d)
    keyboard.send("enter")
    time.sleep(3)
    close_window()


def network_test_barrier(d):
    """
    Пинг тест данного устройства
    """
    d = int(d)
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(1.5)
    keyboard.write("ping 192.168.24.%s -t" % d)
    keyboard.send("enter")
    time.sleep(3)
    close_window()


def bios_terminal(d):
    """
    Выход в биос меню конфигурации устройства
    """
    d = int(d)
    d = d % 100 + 60
    device_out(d)
    keyboard.write("sh -c /usr/srvmode")
    keyboard.send("enter")


def bios_barrier(d):
    """
    Выход в биос меню конфигурации устройства
    """
    d = int(d)
    device_out(d)
    keyboard.write("sh -c /usr/srvmode")
    keyboard.send("enter")
#
# команды


# 2 блокировать
def block_bar(d):
    template(d)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("3")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 3 разблокировать
def un_block_bar(d):
    template(d)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("4")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 4 открыть шлагбаум
def open_bar(d):
    template(d)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 5 закрыть шлагбаум
def close_bar(d):
    template(d)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 6 не работает
def not_work_bar(d):
    template(d)
    keyboard.send("9")
    time.sleep(0.3)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 7 в работе
def work_bar(d):
    template(d)
    keyboard.send("9")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 8 сброс билетов
def reset_tickets(d):
    template(d)
    keyboard.send("6")
    time.sleep(0.3)
    keyboard.send("6")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("delete")
    time.sleep(1.2)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.write("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# 94 команда
def command_94(d):

    # получаем время:
    date = str(datetime.date.today())
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    day = int(date_list[2])
    month = int(date_list[1])
    command = (5 * day) + month
    if command < 100:
        com_str = '0' + str(command)
    else:
        com_str = str(command)


    template(d)
    keyboard.send("9")
    time.sleep(0.3)
    keyboard.send("4")
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send(com_str[0])
    time.sleep(0.3)
    keyboard.send(com_str[1])
    time.sleep(0.3)
    keyboard.send(com_str[2])
    time.sleep(0.3)
    keyboard.send("*")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()


# шаблон ввода в pglsvrem
def template(d):

    d = str(d)
    time.sleep(0.3)
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(0.7)
    keyboard.write("pglsvrem")
    time.sleep(0.5)
    keyboard.send("enter")
    time.sleep(1.0)
    keyboard.write(d)
    time.sleep(0.5)
    keyboard.send("tab")
    time.sleep(0.5)
    keyboard.send("space")
    time.sleep(0.5)
    keyboard.send("delete")
    time.sleep(0.5)


# команды для касс

# шаблон ввода в svrem
def template_term(d):
    d = str(d)
    time.sleep(0.3)
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(0.7)
    keyboard.write("svrem")
    time.sleep(0.5)
    keyboard.send("enter")
    time.sleep(1.5)

    key_step = 0
    while key_step != 23 + (int(d) - 600):
        keyboard.send("Down")
        time.sleep(0.1)
        key_step += 1

    key_step = 0
    while key_step != 5:
        keyboard.send("tab")
        key_step += 1
    time.sleep(0.2)

    keyboard.send("enter")
    time.sleep(1.0)
    keyboard.send(",")
    time.sleep(0.5)
    keyboard.send(",")
    time.sleep(0.5)


# сброс ошибок 07
def comm_07(d):
    template_term(d)
    keyboard.send("0")
    time.sleep(0.5)
    keyboard.send("7")
    time.sleep(0.5)
    keyboard.send("enter")
    time.sleep(0.5)
    keyboard.send(",")
    time.sleep(0.5)
    keyboard.send("d")
    time.sleep(1.0)
    keyboard.send("alt+f4")
    time.sleep(1.0)
    close_window()
    time.sleep(0.5)
    close_window()


# перезагрузка билда
def bild_reset(d):
    template_term(d)
    keyboard.send("4")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.send("0")
    time.sleep(0.3)
    keyboard.send("5")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(1.0)
    keyboard.send("alt+f4")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(1.0)
    close_window()
    time.sleep(0.5)
    close_window()


#  докладка билда
def money_up_reset(d):
    template_term(d)
    keyboard.send("4")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("4")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(1.0)
    keyboard.send("alt+f4")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(1.0)
    close_window()
    time.sleep(0.5)
    close_window()


#  сброс билда
def money_down_reset(d):
    template_term(d)
    keyboard.send("4")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("3")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(1.0)
    time.sleep(1.0)
    keyboard.send("alt+f4")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(1.0)
    close_window()
    time.sleep(0.5)
    close_window()


#   х отчёт
def x_report(d):
    template_term(d)
    keyboard.send("6")
    time.sleep(0.3)
    keyboard.send("3")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.send("0")
    time.sleep(0.3)
    keyboard.send("2")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.5)
    keyboard.send(",")
    time.sleep(0.3)
    keyboard.send(",")
    time.sleep(0.3)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(1.0)
    close_window()
    time.sleep(0.5)
    close_window()


#   z отчёт
def z_report(d):
    template_term(d)
    keyboard.send("6")
    time.sleep(0.3)
    keyboard.send("3")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.send("0")
    time.sleep(0.3)
    keyboard.send("1")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(0.5)
    keyboard.send(",")
    time.sleep(0.3)
    keyboard.send(",")
    time.sleep(0.3)
    keyboard.send("d")
    time.sleep(0.3)
    keyboard.send("alt+f4")
    time.sleep(1.0)
    close_window()
    time.sleep(0.5)
    close_window()


#   94 касса
def term_94(d):
    template_term(d)
    keyboard.send("9")
    time.sleep(0.5)
    keyboard.send("4")
    time.sleep(0.5)
    keyboard.send("enter")
    time.sleep(0.5)

    # получаем время:
    date = str(datetime.date.today())
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    day = int(date_list[2])
    month = int(date_list[1])
    command = (5 * day) + month
    if command < 100:
        com_str = '0' + str(command)
    else:
        com_str = str(command)

    keyboard.send(com_str[0])
    time.sleep(0.5)
    keyboard.send(com_str[1])
    time.sleep(0.5)
    keyboard.send(com_str[1])
    time.sleep(0.5)

    keyboard.send("enter")
    time.sleep(1.3)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()
    time.sleep(0.5)
    close_window()


# проверка запущенна ли программа
def test_svrem():
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(1.5)
    keyboard.write("taskkill /im svrem.exe")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(1.5)
    close_window()


# проверка запущенна ли программа
def test_pglsvrem():
    os.startfile(r"C:\Windows\System32\\cmd.exe")
    time.sleep(1.5)
    keyboard.write("taskkill /im pglsvrem.exe")
    time.sleep(0.3)
    keyboard.send("enter")
    time.sleep(1.5)
    close_window()


# проверка установки английского языка на клавиатуре

def get_layout():
        time.sleep(0.3)
        keyboard.send("shift+alt")
        time.sleep(0.3)


# выход
def cl_d(d):
    template_term(d)
    keyboard.send("d")
    time.sleep(0.5)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    keyboard.send("alt+f4")
    time.sleep(0.5)
    close_window()
    time.sleep(0.5)
    close_window()
