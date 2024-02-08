# Настройка переменных окружения в Django-проекте

Для улучшения безопасности и гибкости конфигурации, рекомендуется использовать переменные окружения для управления конфигурационными данными вашего Django-проекта, включая настройки подключения к базе данных.

## Шаги для настройки

### 1. Создание файла `.env`

В корневой директории вашего проекта создайте файл `.env` и добавьте в него следующие переменные окружения:

```makefile
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
