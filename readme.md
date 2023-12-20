# Техническое задание business_shell_django

## Стек технологий
### Backend:
`Django`, `Django Rest Framework`


## Описание проекта
Необходимо создать сайт-блог, на главной странице которого будет отображаться список постов. 
Администраторы сайта могут создавать новые посты.
При нажатии на пост пользователь будет перенаправлен на отдельную страницу, где будет отображаться 
выбранный пост и комментарии, оставленные под ним. Комментарии могут оставлять любые зарегистрировавшиеся пользователи.

## Запуск проекта
- Сделать команду git clone https://github.com/iolshn04/business_shell_django.git в вашем терминале
- Установить все пакеты зависимости pip install -r requirements.txt
- Перейти в папку с проектом cd mysite
- Применить миграции python manage.py migrate
- Создать суперпользователя python manage.py createsuperuser
- Перейти на сайт, можно зарегистрироваться, войти или выйти
Чтобы создать пост нужен суперпользователь(администратор) его можно настроить в админке
- Чтобы создать комментарий на пост, нужно быть авторизованным
- Просматривать посты и комментарии могут все по ТЗ

## Технические требования

### Backend
- Разработка модели `Post` для представления поста.
- Разработка модели `Comment` для представления комментария.
- Разработка API для выполнения следующих действий:
  - Создание нового поста(только для администратора)
  - Получение списка всех постов.
  - Получение конкретного поста и связанных с ним комментариев.
  - Создание нового комментария под определенным постом(только для зарегистрированных пользователей).
  - Аутентификация и авторизация пользователей (вход, регистрация).

Апи должен реализовываться с помощью Django Rest Framework. 
Входящие и исходящие данные должны быть провалидированы 
с помощью валидаторов из Django Rest Framework

