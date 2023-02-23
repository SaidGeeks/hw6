import re
class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color
    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value
data = open('MOCK_DATA.txt', 'r')
content = data.read()
data.close()
while True:
    print('1 - Считать имена и фамилии')
    print('2 - Считать все емайлы')
    print('3 - Считать названия файлов')
    print('4 - Считать цвета')
    print('5 - Выход')
    command = input('Введите команду: ')
    if command == '5':
        print('Вы вышли из программы')
        break
    elif command == '1':
        with open('name_surname.txt', 'w') as file:
            names_list = re.findall(r'\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b', content)
            for name in names_list:
                file.write(name+'\n')
    elif command == '2':
        with open('emails.txt', 'w') as file:
            emails_list = re.findall(r'(\b[\w\-]+[@][\w\-]+(\.[\w\-]+)+)', content)
            for email in emails_list:
                file.write(email[0]+'\n')
    elif command == '3':
        with open('files.txt', 'w') as file:
            files_list = re.findall(r'[\t\s][\w]+\.[\w]+\b', content)
            for files in files_list:
                file.write(files[1:]+'\n')
    elif command == '4':
        with open('colors.txt', 'w') as file:
            color_list = re.findall(r'#[a-f0-9]{6}\n', content)
            for color in color_list:
                file.write(color)

    else:
        print('Wrong command')









#ДЗУрок6 Дэдлайн 22.02.2023 23 59
"""ДЗ**: У вас есть файл MOCK_DATA.txt, в котором 1000 строк с данными (Имя и Фамилия, емайл, название файла с расширением и код цвета)

1. Написать программу, где отображается меню с опциями: 1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход
2. При выборе опции меню необходимо считать соответствующую информацию из файла с данными при помощи регулярных выражений и сохранить считанные данные в новый файл.
3. Если пользователь выбирает пункт в меню 1: считываются все имена и фамилии (1000 строк) и сохраняются в файл под названием names.txt. Если пользователь выбирает пункт в меню 2: считываются все емайлы (1000 строк) и сохраняются в файл под названием emails.txt и тд.
4. До тех пор пока пользователь не выбрал пункт 5 программа работает и предлагает опции меню.
5. При повторном выборе какого-то из пунктов меню, существующий файл с данными, например names.txt - полностью перезаписывается."""