import code_decode as cd


# функция чтения файлов клиентской иформации
def read_users():
    cd.decrypt('conf_user.txt', cd.key)
    with open('conf_user.txt', 'r') as f:
        lines = f.readlines()
        users = lines[0].split()
        str_users = ' '.join(users)
    cd.encrypt('conf_user.txt', cd.key)
    return str_users


# добавление  пользователей в телеграмм:
def new_user(user):
    cd.decrypt('conf_user.txt', cd.key)
    with open('conf_user.txt', 'r') as f:
        lines = f.readlines()
        users = lines[0].split()
        str_users = ' '.join(users)
    if user in users:
        cd.encrypt('conf_user.txt', cd.key)
        return "Такой пользователь уже создан!"
    else:
        users.append(user)
        lines = [' '.join(users)]
        with open('conf_user.txt', "w") as file:
            for line in lines:
                file.write(line + '\n')
        cd.encrypt('conf_user.txt', cd.key)
        return "Пользователь успешно добавлен!"


# удаление пользователей в телеграмм:
def dell_user(user):
    cd.decrypt('conf_user.txt', cd.key)
    with open('conf_user.txt', 'r') as f:
        lines = f.readlines()
        users = lines[0].split()
        str_users = ' '.join(users)
    if user not in users:
        cd.encrypt('conf_user.txt', cd.key)
        return "Такой пользователь не существует"
    else:
        users.remove(user)
        lines = [' '.join(users)]
        with open('conf_user.txt', "w") as file:
            for line in lines:
                file.write(line + '\n')
        cd.encrypt('conf_user.txt', cd.key)
        return "Пользователь успешно удален!"


