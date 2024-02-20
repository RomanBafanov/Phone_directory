from django.core.management.base import BaseCommand


def define_page_boundaries(page):

    """
    Функция преобразует номер искомой страницы в начальную и конечную строку отображения

    :param page: (int) номер искомой строки
    :return:
        start (int): первая строка для отображения
        end (int): последняя строка для отображения
    """

    end = 5 * page
    start = end - 5

    return start, end


def output_generation(guide, start=None, end=None):

    """
    Функция собирает записи из справочника с определённой страницы для вывода на экран.
    Если страница не выбрана пользователем собираются все записи в справочнике

    :param guide: (list) список всех записей в справочнике
    :param start: (int) первая строка для отображения
    :param end: (int) последняя строка для отображения
    :return: contacts (str): записи для вывода в консоль
    """

    labels = [
        "\033[1mid\033[0m", "\033[1mName\033[0m", "\033[1mSurname\033[0m", "\033[1mPatronymic\033[0m",
        "\033[1mOrganization\033[0m", "\033[1mWork_phone\033[0m", "\033[1mCell_phone\033[0m"
    ]
    contacts = ""
    for people in guide[start:end]:
        human = people.split(', ')
        for label, value in zip(labels, human):
            if value == 'None':
                value = '---'
            contacts += f"{label}: {value}, "
        contacts += "\n"

    return contacts


class Command(BaseCommand):
    help = 'Вывод постранично записей из справочника на экран'

    def add_arguments(self, parser):
        parser.add_argument('-P', '--page', default=None, type=int, help='Номер страницы. По 5 номеров на странице')

    def handle(self, *args, **options):
        if options['page']:
            page = options['page']
            start, end = define_page_boundaries(page)
            with open('контакты.txt', 'r') as file:
                temp = file.read().splitlines()
                if len(temp) < start:
                    self.stdout.write('Такой страницы нет в справочнике')
                else:
                    if len(temp) < end:
                        end = len(temp)
                    contacts = output_generation(temp, start, end)
                    self.stdout.write(contacts)
        else:
            with open('контакты.txt', 'r') as file:
                guide = file.read().splitlines()
                contacts = output_generation(guide)
                self.stdout.write(contacts)
