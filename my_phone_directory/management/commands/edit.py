from django.core.management.base import BaseCommand


def write_a_new_line(old_line, new_string):

    """
    Функция записывает новую строку

    :param old_line: (str) строка для внесения изменений
    :param new_string: (str) строка с внесёнными изменениями
    :return: None
    """

    with open('контакты.txt', 'r') as file:
        old_data = file.read()
    new_data = old_data.replace(old_line, new_string)

    with open('контакты.txt', 'w') as file:
        file.write(new_data)


def search_string(id_records):

    """
    Функция выполняет поиск строки для внесения изменений

    :param id_records: (int) номер строки для внесения изменений
    :return:
        people (str): строка для внесения изменений
        human (int): список строки для внесения изменений
    """

    with open('контакты.txt', 'r') as file:
        temp = file.read().splitlines()
        for people in temp:
            human = people.split(', ')
            if human[0] == str(id_records):
                return people, human

    return False, False


def creating_new_line(list_string, options):

    """
    Функция формирует новую строку для перезаписи в справочнике

    :param list_string: (int) список строки для внесения изменений
    :param options: (dict) словарь с параметрами для внесения изменений
    :return: new_string (str) строка с внесёнными изменениями
    """

    if options['name']:
        list_string[1] = options['name']
    if options['surname']:
        list_string[2] = options['surname']
    if options['patronymic']:
        list_string[3] = options['patronymic']
    if options['organization']:
        list_string[4] = options['organization']
    if options['work_phone']:
        list_string[5] = options['work_phone']
    if options['cell_phone']:
        list_string[6] = options['cell_phone']
    new_string = ', '.join(elem for elem in list_string)

    return new_string


class Command(BaseCommand):
    help = 'Редактирование записей в справочнике по id в записной книжке'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID записи')
        parser.add_argument('-N', '--name', default=None, type=str, help='Имя')
        parser.add_argument('-S', '--surname', default=None, type=str, help='Фамилия')
        parser.add_argument('-P', '--patronymic', default=None, type=str, help='Отчество')
        parser.add_argument('-O', '--organization', default=None, type=str, help='Организация')
        parser.add_argument('-W', '--work_phone', default=None, type=str, help='Телефон рабочий')
        parser.add_argument('-C', '--cell_phone', default=None, type=str, help='Телефон сотовый')

    def handle(self, *args, **options):
        id_records = options['id']
        replacement_string, list_string = search_string(id_records)
        if replacement_string:
            new_string = creating_new_line(list_string, options)
            write_a_new_line(replacement_string, new_string)
            self.stdout.write('Запись отредактирована')
        else:
            self.stdout.write('Такой записи не существует')
