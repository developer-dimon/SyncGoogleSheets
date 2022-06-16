# DRF+REACT+NGINX+CELERY+REDIS+POSTGRES+DOCKER

### Инструкция:
  1. Создать сервисный аккаунт гугл для подключение к таблице (подробная инструкция https://habr.com/ru/post/575160/)
  2. Полученный файл json с кредами скопировать в папку backend. Указать название файла, диапазон ячеек и Id таблицы в .env
  3. Запустить docker: ```docker-compose up --build```
  4. При повторном запуске закомментировать ```python manage.py migrate``` и ```python manage.py collectstatic``` в файле ```deploy.sh```
