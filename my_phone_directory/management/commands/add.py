from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Добавление новой записи в телефонный справочник'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Имя')
        parser.add_argument('-S', '--surname', default='None', type=str, help='Фамилия')
        parser.add_argument('-P', '--patronymic', default='None', type=str, help='Отчество')
        parser.add_argument('-O', '--organization', default='None', type=str, help='Организация')
        parser.add_argument('-W', '--work_phone', default='None', type=str, help='Телефон рабочий')
        parser.add_argument('-C', '--cell_phone', default='None', type=str, help='Телефон сотовый')

    def handle(self, *args, **options):
        name = options['name']
        surname = options['surname']
        patronymic = options['patronymic']
        organization = options['organization']
        work_phone = options['work_phone']
        cell_phone = options['cell_phone']
        with open('контакты.txt', 'r') as file:
            count = len(file.read().splitlines())
        with open('контакты.txt', 'a') as file:
            file.write(f'\n{count + 1}, {name}, {surname}, {patronymic}, {organization}, {work_phone}, {cell_phone}')
        self.stdout.write('Запись успешно добавлена')
