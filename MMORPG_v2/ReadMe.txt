Задание:
Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной
MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность
- зарегистрироваться в нём по e-mail,
- получив письмо с кодом подтверждения регистрации.
После регистрации им становится доступно
- создание и редактирование объявлений.
Объявления состоят из:
    - заголовка и
    - текста, внутри которого могут быть картинки, встроенные видео и другой контент.

Кроме того, пользователь обязательно должен определить объявление в одну из
следующих категорий:
Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Пользователи могут отправлять
- отклики на объявления других пользователей, состоящие из простого текста.

При отправке отклика пользователь должен
- получить e-mail с оповещением о нём.

Также пользователю должна быть доступна
- приватная страница с откликами на его объявления,
    внутри которой он может
        - фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик,
        - также должно прийти уведомление).

Также мы бы хотели иметь возможность отправлять пользователям
- новостные рассылки.
--------------------------------------------------------------------------
ICONS from
https://fontawesome.com/search?q=logout&o=r

python manage.py makemigrations
python manage.py migrate

Переводы
Поскольку у нас уже были записи в базе данных, надо будет ввести команду
python manage.py update_translation_fields
Везде вставить
from django.utils.translation import gettext as _

Для обновления переводов в django.po
python manage.py makemessages -l en
и скомпиллировать
python manage.py compilemessages

-------------------------------------------------------------
{% load i18n %}
<form action="{% url 'set_language' %}" method="POST"> {% csrf_token %} <!-- Не забываем по csrf_token для POST запросов -->
    <input type="hidden" name="next" value="{{ redirect_to }}"></form>

    <select name="language" id="">
        {% get_available_languages as LANGUAGES %} <!-- получаем языки -->
        {% get_language_info_list for LANGUAGES as languages %} <!-- Помещаем их в список languages -->

        {% for language in languages %} <!-- Итерируясь по списку, выводим их название на языке пользователя и код -->
            <option value="{{ language.code }}" {% if language.code == LANGUAGE_CODE %} selected {% endif %}>
                {{ language.name_local }} - {{ language.code }}
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="set">
-------------------------------------------------------------
For Celery & Redis

worker — это часть системы, которая отправляет задачи из очереди на исполнение.

Все задачи принято хранить в файлах с названием tasks.py. В таком случае Celery сможет самостоятельно 
находить задачи. Любая задача представляет собой обычную функцию с одной особенностью: 
она должна быть обернута в декоратор.

1. Запустить сервер: 
(venv) PS C:\MMORPG_v2\gamers_pool\> python manage.py runserver

2. Запустить Redis
C:\Program Files\Redis\redis-server.exe

3. Запустить Celery:
C:\MMORPG_v2\gamers_pool\
(venv) PS C:\MMORPG_v2\gamers_pool\> celery -A gamers_pool worker -l INFO --pool=solo

4. Запустить Beat:
(venv) PS C:\MMORPG_v2\gamers_pool\> Celery -A gamers_pool beat -l INFO  