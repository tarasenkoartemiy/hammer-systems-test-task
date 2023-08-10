# Реализовать простую реферальную систему
### [ЗАДАНИЕ](https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FsIkUIoDPKjKqu5Y8u3%2BpM3wtbcyGG4QhBctk2RNusLzVSR6RmgFjlwdE82mJ9iBHq%2FJ6bpmRyOJonT3VoXnDag%3D%3D&name=%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%BB%D1%8F%20Python%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0-2.docx)
# Разворачивание
1. [Установить](https://docs.docker.com/compose/install/) Docker 
2. [Установить](https://git-scm.com/downloads) Git
3. Клонировать репозиторий:
```no-highlight
https://github.com/tarasenkoartemiy/hammer-systems-test-task.git
```
4. В корневой папке проекта создать файл `.env` и заполнить, используя `template.env`
5. Из корневой папки проекта запустить сервисы:
```no-highlight
docker compose up
```
# Описание
1. Для получения кода подтверждения нужно перейти по эндпоинту POST http://0.0.0.0:8000/api/v1/login/ c телом запроса:
```no-highlight
{
    "phone_number": +79581881543
}
```
2. В теле ответа будет находиться код подтверждения:
```no-highlight
{
    "auth_code": 7247
}
```
3. Для завершения аутентификации нужно перейти по эндпоинту POST http://0.0.0.0:8000/api/v1/activate/ c телом запроса:
```no-highlight
{   
    "phone_number": +79581881543,
    "auth_code": 7247
}
```
4. В теле ответа будет находиться токен. (В проекте используется аутентификации по токенам). Все последующие запросы должны быть с хэдером:
```no-highlight
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
5. Профиль пользователя -> GET http://0.0.0.0:8000/api/v1/me/
6. Добавить activated_invite_code -> PATCH http://0.0.0.0:8000/api/v1/me/
7. Swagger можно найти тут -> GET http://0.0.0.0:8000/swagger/