from django.core.management.base import BaseCommand


def searching_entry_by_parameter(argument, position):

    """
    Функция выполняет поиск записи в справочнике по имени или фамилии

    :param argument: (str) имя или фамилия для поиска
    :param position: (int) номер позиции в списке
    :return: contact (str) запись для вывода в консоль
    """

    with open('контакты.txt', 'r') as file:
        labels = [
            "\033[1mid\033[0m", "\033[1mName\033[0m", "\033[1mSurname\033[0m", "\033[1mPatronymic\033[0m",
            "\033[1mOrganization\033[0m", "\033[1mWork_phone\033[0m", "\033[1mCell_phone\033[0m"
        ]
        temp = file.read().splitlines()
        contact = False
        for people in temp:
            human = people.split(', ')
            if human[position] == argument:
                contact = ""
                for label, value in zip(labels, human):
                    contact += f"{label}: {value}, "

        return contact


def searching_entry_by_parameters(name, surname):

    """
    Функция выполняет поиск записи в справочнике по имени и фамилии

    :param name: (str) имя для поиска
    :param surname: (str) фамилия для поиска
    :return: contact (str) запись для вывода в консоль
    """

    with open('контакты.txt', 'r') as file:
        labels = [
            "\033[1mid\033[0m", "\033[1mName\033[0m", "\033[1mSurname\033[0m", "\033[1mPatronymic\033[0m",
            "\033[1mOrganization\033[0m", "\033[1mWork_phone\033[0m", "\033[1mCell_phone\033[0m"
        ]
        temp = file.read().splitlines()
        contact = False
        for people in temp:
            human = people.split(', ')
            if human[1] == name and human[2] == surname:
                contact = ""
                for label, value in zip(labels, human):
                    if value == 'None':
                        value = '---'
                    contact += f"{label}: {value}\n"

        return contact


class Command(BaseCommand):
    help = 'Поиск записей по одной или нескольким характеристикам. Поиск по имени и/или фамилии'

    def add_arguments(self, parser):
        parser.add_argument('-N', '--name', default=None, type=str, help='Имя')
        parser.add_argument('-S', '--surname', default=None, type=str, help='Фамилия')

    def handle(self, *args, **options):
        if options['name'] and options['surname']:
            name = options['name']
            surname = options['surname']
            contact = searching_entry_by_parameters(name, surname)
            if contact:
                self.stdout.write(contact)
            else:
                self.stdout.write('Таких имени и фамилии нет в записной книжке')
        elif options['name']:
            name = options['name']
            position = 1
            contact = searching_entry_by_parameter(name, position)
            if contact:
                self.stdout.write(contact)
            else:
                self.stdout.write('Такого имени нет в записной книжке')
        elif options['surname']:
            surname = options['surname']
            position = 2
            contact = searching_entry_by_parameter(surname, position)
            if contact:
                self.stdout.write(contact)
            else:
                self.stdout.write('Такой организации нет в записной книжке')
