import cx_Oracle
import datetime


# Поиск проездов клиента по номеру авто за последний месяц
def client_tr_month(client):
    date = str(datetime.date.today())
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    yestarday = str(today - datetime.timedelta(days=1))
    year = date_list[0]
    month = date_list[1]
    result = []

    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()

        request_str = "SELECT  tactiontime, sdevice, clicenseplate " \
                      "FROM udbidentdata_" + year + "M" + month + " WHERE (clicenseplate like '%" + client + "%'" \
                                                                                                             ") ORDER BY tactiontime DESC"

        c.execute(request_str)

        for row in c:
            result.append(row)

        for i in range(len(result)):
            result[i] = list(result[i])

        conn.close()

    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')
        return result

    return output_tr(replay(result))


# красивый вывод транзакций
def output_tr(client_tr):
    res = []
    for i in range(len(client_tr)):
        if int(client_tr[i][1]) < 200:
            res.append(
                'Клиент: ' + str(client_tr[i][2]) + ' Уст-во №' + str(client_tr[i][1]) + ' Время въезда: ' + str(
                    client_tr[i][0]) + ' ')
        else:
            res.append(
                'Клиент: ' + str(client_tr[i][2]) + ' Уст-во №' + str(client_tr[i][1]) + ' Время выезда: ' + str(
                    client_tr[i][0]) + ' ')
    return res


# удаление повторов
def replay(transactions):
    temp = []
    for x in transactions:
        if x not in temp:
            temp.append(x)
    transactions = temp
    return transactions


# проверка валидности номера
def convert_number(number_avto):
    new_number = []
    convert_rus_big = 'АВЕКМНОРСТУХ'
    convert_rus_lit = 'авекмнорстух'
    convert_eng = 'ABEKMHOPCTYX'
    digit = '0123456789'
    for number in number_avto:
        if number in convert_eng:
            new_number.append(number)
        elif number in convert_rus_big:
            for i in range(len(convert_rus_big)):
                if number == convert_rus_big[i]:
                    new_number.append(convert_eng[i])
        elif number in convert_rus_lit:
            for i in range(len(convert_rus_lit)):
                if number == convert_rus_lit[i]:
                    new_number.append(convert_eng[i])
        elif number in digit:
            for i in range(len(digit)):
                if number == digit[i]:
                    new_number.append(digit[i])
        else:
            pass

    new_number_str = ''.join(new_number)
    if len(new_number_str) > 9 or len(new_number_str) < 3:
        return "некорректный номер"

    return new_number_str