import telebot
from telebot import types
import devices
import client_search as cs
import users
from tokken_key import TOKKEN


TERM = [601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622,
        623, 624, 625, 626, 627, 628, 629]

BAR = [101, 102, 105, 106, 107, 108, 109, 110, 112, 113, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212]

TERM_NAME = ['Касса 601', 'Касса 602', 'Касса 603', 'Касса 604', 'Касса 605', 'Касса 606', 'Касса 607', 'Касса 608',
             'Касса 609', 'Касса 610', 'Касса 611', 'Касса 612', 'Касса 613', 'Касса 614', 'Касса 615', 'Касса 616',
             'Касса 617', 'Касса 618', 'Касса 619', 'Касса 620', 'Касса 621', 'Касса 622', 'Касса 623', 'Касса 624',
             'Касса 625', 'Касса 626', 'Касса 627', 'Касса 628', 'Касса 629', "Главное меню"]
BAR_NAME = ['Въезд 101', 'Въезд 102', 'Въезд 105', 'Въезд 106', 'Въезд 107', 'Въезд 108', 'Въезд 109', 'Въезд 110',
            'Въезд 112', 'Въезд 113', 'Выезд 203', 'Выезд 204', 'Выезд 205', 'Выезд 206', 'Выезд 207', 'Выезд 208',
            'Выезд 209', 'Выезд 210', 'Выезд 211', 'Выезд 212', "Чистка всех корзин", "Главное меню"]

COMMAND_TERM = ["Перезагузка кассы", "Сброс денег", "Загрузка денег", "Перезагрузкака Btb", "Комманда 94",
                "Отправить Z-отчёт ", "Отправить X-отчёт 63*02", "Сброс Ошибок (*07)", "Выход CL+D", "Поменять раскладку",
                "Главное меню"]
COMMAND_BAR = ["Перезагузка стойки", "Заблокировать", "Разблокировать", "Открыть", "Закрыть", "Не работает",
               "Работает", "Сброс билетов", "Команда 94", "Главное меню"]

USERS_MAIN = ["Посмотреть пользователей", "Добавить пользователя", "Удалить пользователя", "Главное меню"]
ADM_USER = 'Lexx85'
device = 0
barier = 0


bot = telebot.TeleBot(TOKKEN)
bot.set_webhook()


@bot.message_handler(commands=['start'])
def start(message):
    clients_bot = users.read_users()
    adm = [ADM_USER, ]  # список из id пользователей
    for user in clients_bot:
        adm.append(user)
    if message.from_user.username == ADM_USER or message.from_user.username in clients_bot:
        mess = 'Приветствую тебя ' + message.from_user.username + ' пользователь!'
        bot.send_message(message.chat.id, mess)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(" Кассы ")
        btn2 = types.KeyboardButton(" Стойки ")
        btn3 = types.KeyboardButton(" Поиск по номеру ")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Главное меню!".format(message.from_user),
                         reply_markup=markup)

    if message.from_user.username not in clients_bot:
        mess = 'Приветствую тебя пользователь ' + message.from_user.username + '  ! Отправьте заявку на вступление в бота разработчику @' + ADM_USER
        bot.send_message(message.chat.id, mess)


# Главное меню

@bot.message_handler()
def get_user_text(message):
    print(message.text)
    print(message.from_user.username)

    clients_bot = users.read_users()
    adm = [ADM_USER, ]  # список из id пользователей
    for user in clients_bot:
        adm.append(user)
    if message.from_user.username in clients_bot or message.from_user.username not in adm:
        if message.text == "Привет" or message.text == "привет":
            mess = "Добрый день, " + message.from_user.first_name + " " + message.from_user.last_name + "!"
            bot.send_message(message.chat.id, mess)

        # меню пользователи
        elif message.text == "Пользователи":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for command in USERS_MAIN:
                btn = command
                markup.add(btn)
            bot.send_message(message.chat.id, 'Выберите команду', reply_markup=markup)

        elif message.text == "Поиск по номеру":
            bot.register_next_step_handler(message, number_search)
        elif message.text == "Главное меню":
            start(message)

            # 0) добавить пользователя в телеграмм бота
        elif message.text == USERS_MAIN[0]:
            bot.send_message(message.chat.id, "посмотреть пользователей:")
            info = users.read_users()
            bot.send_message(message.chat.id, "Пользователи бота:" + info)

            # 1) добавить пользователя в телеграмм бота
        elif message.text == USERS_MAIN[1]:
            bot.send_message(message.chat.id, "Введите имя нового пользователя:")
            bot.register_next_step_handler(message, new_users)

            # 2) удалить пользователя в телеграмм бота
        elif message.text == USERS_MAIN[2]:
            bot.send_message(message.chat.id, "Введите имя пользователя которго нужно удалить:")
            bot.register_next_step_handler(message, dell_users)

        # КАССОВОЕ МЕНЮ
        elif message.text == "Кассы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for term in TERM_NAME:
                markup.add(term)
            bot.send_message(message.chat.id, 'Выберите терминал', reply_markup=markup)

        elif message.text in TERM_NAME:
            devices.test_svrem()
            term = message.text
            global device
            index = TERM_NAME.index(term)
            device = TERM[index]
            print(device)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for command in COMMAND_TERM:
                markup.add(command)
            bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)

        # прописываем команды устройств
        # 1.0 перезагрузка кассовых терминалов
        elif message.text == COMMAND_TERM[0]:
            mess = "Устройство " + str(device) + " Устройство перезагружено, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.terminal_device(device)
            bot.send_message(message.chat.id, "Устройство перезагружено")
            bot.send_message(1422691786, "Действие завершено!")

        # 1.1 сброс денег
        elif message.text == COMMAND_TERM[1]:
            mess = "Устройство " + str(device) + " Деньги сбрасываются, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.money_down_reset(device)
            bot.send_message(message.chat.id, "Деньги сбрасываются...")
            bot.send_message(1422691786, "Действие завершено!")


        # 2.1 докладка денег
        elif message.text == COMMAND_TERM[2]:
            mess = "Устройство " + str(device) + " Докладывайте деньги, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.money_up_reset(device)
            bot.send_message(message.chat.id, "Докладывайте деньги!")
            bot.send_message(1422691786, "Действие завершено!")

        # 3.1 перезагрузка билда
        elif message.text == COMMAND_TERM[3]:
            mess = "Устройство " + str(device) + " Перезагружается btb, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.bild_reset(device)
            bot.send_message(message.chat.id, "Перезагружается btb")
            bot.send_message(1422691786, "Действие завершено!")

        # 4.1 команда 94
        elif message.text == COMMAND_TERM[4]:
            mess = "Устройство " + str(device) + " Команда 94 выполняется, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.term_94(device)
            bot.send_message(message.chat.id, "Команда 94 выполняется!")
            bot.send_message(1422691786, "Действие завершено!")

        # 5.1 z
        elif message.text == COMMAND_TERM[5]:
            mess = "Устройство " + str(device) + " Z отчёт отправлен, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.z_report(device)
            bot.send_message(message.chat.id, "Z отчёт отправлен!")
            bot.send_message(1422691786, "Действие завершено!")

        # 6.1 x
        elif message.text == COMMAND_TERM[6]:
            mess = "Устройство " + str(device) + " X отчёт отправлен, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.x_report(device)
            bot.send_message(message.chat.id, "X отчёт отправлен!")
            bot.send_message(1422691786, "Действие завершено!")

        # 7. сброс ошибок 07
        elif message.text == COMMAND_TERM[7]:
            mess = "Устройство " + str(device) + " Ошибки сброшены, пользователь: " + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.comm_07(device)
            bot.send_message(message.chat.id, "Ошибки сброшены")
            bot.send_message(1422691786, "Действие завершено!")

        # 8. CL+D
        elif message.text == COMMAND_TERM[8]:
            mess = "Устройство " + str(device) + " вышло из тех. режима пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.cl_d(device)
            bot.send_message(message.chat.id, "Выход из технического режима")
            bot.send_message(1422691786, "Действие завершено!")

        # 9. англ раскладка клавиатуры
        elif message.text == COMMAND_TERM[9]:
            devices.get_layout()
            bot.send_message(message.chat.id, "Раскладка переключена")



        # СТОЕЧНОЕ МЕНЮ
        elif message.text == "Стойки":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for bar in BAR_NAME:
                markup.add(bar)
            bot.send_message(message.chat.id, 'Выбер'
                                              'ите терминал', reply_markup=markup)

        elif message.text == "Чистка всех корзин":
            mess = "Устройство " + str(device) + " Идёт сброс билетов на всех стойках, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            bot.send_message(message.chat.id, 'Идёт сброс билетов на всех стойках...')
            exits_bar = BAR[10:]
            for bar in exits_bar:
                devices.reset_tickets(bar)
            bot.send_message(message.chat.id, 'Сброс билетов завершен!')
            bot.send_message(1422691786, "Действие завершено!")

        elif message.text in BAR_NAME:
            devices.test_pglsvrem()
            global barier
            bar = message.text
            index = BAR_NAME.index(bar)
            barier = BAR[index]
            print(barier)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for command in COMMAND_BAR:
                markup.add(command)
            bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)


        # прописываем команды стоек
        # 2.0 перезагрузка стоек
        elif message.text == COMMAND_BAR[0]:
            mess = "Устройство " + str(barier) + " Устройство перезагружено, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.barrier_device(barier)
            bot.send_message(message.chat.id, "Устройство перезагружено")
            bot.send_message(1422691786, "Действие завершено!")

        # 2.1 заблокировать
        elif message.text == COMMAND_BAR[1]:
            mess = "Устройство " + str(barier) + " Устройство заблокировано, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.block_bar(barier)
            bot.send_message(message.chat.id, "Устройство заблокировано")
            bot.send_message(1422691786, "Действие завершено!")

        # 2.2 разблокировать
        elif message.text == COMMAND_BAR[2]:
            mess = "Устройство " + str(barier) + " Устройство разблокировано, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.un_block_bar(barier)
            bot.send_message(message.chat.id, "Устройство разблокировано")
            bot.send_message(1422691786, "Действие завершено!")

        # 2.4 открыть
        elif message.text == COMMAND_BAR[3]:
            mess = "Устройство " + str(barier) + " Устройство открыто, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.open_bar(barier)
            bot.send_message(message.chat.id, "Устройство открыто")
            bot.send_message(1422691786, "Действие завершено!")

        # 2.5 закрыть
        elif message.text == COMMAND_BAR[4]:
            mess = "Устройство " + str(barier) + " Устройство закрыто, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.close_bar(barier)
            bot.send_message(message.chat.id, "Устройство закрыто")
            bot.send_message(1422691786, "Действие завершено!")

        # 2.6 не работает
        elif message.text == COMMAND_BAR[5]:
            mess = "Устройство " + str(barier) + " Устройство  не работает, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.not_work_bar(barier)
            bot.send_message(message.chat.id, "Устройство  не работает")
            bot.send_message(1422691786, "Действие завершено!")

        # 2.7 работает
        elif message.text == COMMAND_BAR[6]:
            mess = "Устройство " + str(barier) + " Устройство в работе, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.work_bar(barier)
            bot.send_message(message.chat.id, "Устройство в работе")
            bot.send_message(1422691786, "Действие завершено!")


        # 2.8 сброс стоек
        elif message.text == COMMAND_BAR[7]:
            mess = "Устройство " + str(barier) + " Билеты сброшены, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.reset_tickets(barier)
            bot.send_message(message.chat.id, "Билеты сброшены")
            bot.send_message(1422691786, "Действие завершено!")


            # 2.9 команда 94
        elif message.text == COMMAND_BAR[8]:
            mess = "Устройство " + str(barier) + " Команда 94 выполняется, пользователь:" + message.from_user.username
            bot.send_message(1422691786, mess)
            devices.command_94(barier)
            bot.send_message(message.chat.id, "Команда 94 выполняется... По завершении перезагрузите стойку!")
            bot.send_message(1422691786, "Действие завершено!")

        else:
            mess = "Ошибочка вышла, товарищ! "
            bot.send_message(message.chat.id, mess)

    else:
        bot.send_message(message.chat.id, 'Отправьте заявку на вступление в бота разработчику @' + ADM_USER)


def reboot(message):
    message = message.text
    mess = 'Устройство ' + str(device) + ' перезагружено...'
    print(mess)
    bot.send_message(message.chat.id, mess)
    devices.terminal_device(device)


# поиск проездов по номеру за месяц:
def number_search(message):
    number = message.text
    print(message)
    number = cs.convert_number(number)
    if number == "некорректный номер":
        bot.send_message(message.chat.id, "некорректный номер")
    info = cs.client_tr_month(number)
    for inf in info:
        bot.send_message(message.chat.id, inf)


# добавляем польователя
def new_users(message):
    user = message.text
    mess = users.new_user(user)
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, "Действие завершено")


# удаляем пользователя
def dell_users(message):
    user = message.text
    mess = users.dell_user(user)
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, "Действие завершено")


bot.infinity_polling()
