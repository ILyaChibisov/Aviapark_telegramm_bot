
from cryptography.fernet import Fernet


# def write_key():
# # Создаем ключ и сохраняем его в файл
#     key = Fernet.generate_key()
#     with open('crypto.key', 'wb') as key_file:
#         key_file.write(key)
#
# def load_key():
# # Загружаем ключ 'crypto.key' из текущего каталога
#     return open('crypto.key', 'rb').read()
#
# write_key()
# key = load_key()

key = '_KWGEobfDR3zahj0VlO6F7-5sORBEp3QS7Cx0rJdz1o='


# Зашифруем файл и записываем его
def encrypt(filename, key):

    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)


# записать зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


# encrypt('conf_user.txt', key)


# Расшифровка файла
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


# decrypt('conf_user.txt', key)