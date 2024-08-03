# My learn
### ОПИСАНИЕ:
**My learn** - это учебный Pet-проект - платформа электронного обучения, 
созданный в рамках изучения чистого Django. Преподаватели управляют курсами 
и их модулями, загружают по ним контент; студенты зачисляются на курсы,
просматривают необходимую информацию, общаются с другими студентами в чате.
В проекте реализован следующий функционал:
* приложения: курсы (courses), студенты (students), чат (chat);
созданы модели, формы, представления (viewsets), пути, шаблоны.
* система аутентификации, авторизации и регистрации студентов.
* группы и разрешения для ограничения доступа студентов к представлениям.
* кастомное поле OrderField для нумерации и сортировки курсов и модулей при 
  отображении в шаблонах. 
* полиморфная модель загрузки контента различного типа - text, file, image,
video (через ContentType).
* просмотр контента, в т.ч. видео (библиотека embed_video)
* formsets для одновременного создания нескольких модулей.
* интегрирована готовая функция перетаскивания на JavaScript для изменения 
  порядка модулей курса и их содержимого в шаблонах.
* система кэширования Memcached и Redis.
* чат студентов (Django Channels), асинхронный WebSocket-потребителя
и WebSocket-клиента, связь между потребителями через канальный уровень с 
резидентным хранилищем Redis. Интегрирован готовый JS-скрипт.
* REST API (DRF) - сериализаторы, представления, разрешения, маршрутизаторы, 
аутентификация.
* запуск проекта через docker-compose (контейнеры Postgres, Redis, NGINX/uWSGI 
и ASGI-сервер Daphne для Django Channels), защита соединения через TLS/SSL 
(HTTPS).

### СТЕК ТЕХНОЛОГИЙ:

Python 3.12, Django 5.0.7, DRF 3.15.2, Redis 5.0.8, 

### ЛОКАЛЬНАЯ УСТАНОВКА (для Windows):

1. Клонируй проект и перейди в него:
```shell
git clone git@github.com:smaspb17/my_learn.git
cd my_learn
```

2. Найди файл hosts твоей машины. Если используешь Linux/macOS, то файл hosts 
находится в /etc/hosts. Если же у тебя Windows,
то C:\Windows\System32\Drivers\etc\hosts. Отредактируй файл hosts,
добавив следующую ниже строку:
```
127.0.0.1 educaproject.com www.educaproject.com
```

3. Создай SSL/TLS сертификат командой ниже находясь в директории educa/ssl. 
В итоге каталог educa/ssl/ будет содержать два файла: educa.key (приватный 
   ключ) и educa.crt (сертификат).
```
openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes \
-keyout ssl/educa.key -out ssl/educa.crt \
-subj '/CN=*.educaproject.com' \
-addext 'subjectAltName=DNS:*.educaproject.com'
```

4. Создай и активируй виртуальное окружение: 
```shell
python -m venv venv
venv/Scripts/activate
```

5. Установи зависимости:
```shell
pip install -r requirements.txt
```

6. При необходимости обнови пакетный менеджер pip:
```shell
python -m pip install --upgrade pip
```

7. Создай файл .env (в контейнере проекта `my_learn/`) и заполни его 
   переменными, указанными в файле example.env.

8. Перейди в пакет проекта (`my_learn/educa/`, где находится файл
   manage.py) и выполни миграции:
```shell
cd my_shop/
python manage.py makemigrations
python manage.py migrate
```

9. Создай суперпользователя:
```shell
python manage.py createsuperuser
```

10. Выполни сбор статики:
```shell
python manage.py collectstatic
```

11. Запусти сервер разработки и пройди на главную страницу
```shell
python manage.py runserver
https://educaproject.com
```

Теперь ты можешь использовать проект на своём компьютере. 
Если ты хочешь остановить проект, нажми Ctrl+C в терминале, 
а затем деактивируй виртуальное окружение командой:
```shell
deactivate
```

### АВТОР:
Шайбаков Марат

### ЛИЦЕНЗИЯ:
Apache License 2.0

### КОНТАКТЫ:
smaspb17@yandex.ru