import os

# Устанавливаем переменную окружения
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

# Настройки Gunicorn
bind = '0.0.0.0:8000'
workers = 7