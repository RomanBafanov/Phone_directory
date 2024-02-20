# Phone_directory
 
Телефонный справочник.

## Как установить

Python3 должен быть уже установлен. Затем используйте pip 
(или pip3, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
``` 

### будет установлен:

Django~=5.0.2

## Использование

Команда 
```bash
python manage.py add
```

добавляет контакт в справочник

**positional arguments:** 
* name - Имя

**options:**  
* -h, --help - Выдаст справочное сообщение
* -S, --surname - Фамилия
* -P, --patronymic - Отчество
* -O, --organization - Организация
* -W, --work_phone - Телефон рабочий
* -C, --cell_phone - Телефон сотовый

Команда 
```bash
python manage.py output
```

выводит контакты из справочника

**options:**  
* -h, --help - Выдаст справочное сообщение
* -P, --page - Номер страницы. По 5 номеров на странице

Команда 
```bash
python manage.py search
```

ведёт поиск контакта в справочнике по имени и\или фамилии

**options:**  
* -h, --help - Выдаст справочное сообщение
* -N, --name - Имя
* -S, --surname - Фамилия

Команда 
```bash
python manage.py edit
```

редактирует запись в справочнике по его id

**positional arguments:** 
* id - ID записи

**options:**  
* -h, --help - Выдаст справочное сообщение
* -N, --name - Имя
* -S, --surname - Фамилия
* -P, --patronymic - Отчество
* -O, --organization - Организация
* -W, --work_phone - Телефон рабочий
* -C, --cell_phone - Телефон сотовый

## Цели проекта

Тестовое задание на позицию Python backend developer

 