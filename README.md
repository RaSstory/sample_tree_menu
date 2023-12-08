# Описание

Тестовый проект, для создания древовидных меню с использованием teplatetags
Debug Toolbar уже встроен, и активирован.
## Установка
После выполнения команды ```python manage.py runserver```
перейдите в админку проекта и создайте Меню, для теста есть готовый вариант main_menu, но его обязательно нужно создать в админке.




```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
cd myproject/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```


## Меню

Для отображения меню перейдите во вкладку http://127.0.0.1:8000
