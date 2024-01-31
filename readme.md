# API ДЗ

API доступен в интернете по адресу ```https://djangoapitest.pythonanywhere.com/```
<br/>
Также документация была сделана через swagger, она доступна по
адресу ```https://djangoapitest.pythonanywhere.com/swagger```

## В чем заключается задача API

Задача API заключается в том, что через него будут производиться задачи в мобильном приложении такие, как создание
записи, ее редактирование, а
также получение конкретной записи по её id и получение всех записей у которых есть определенный email.

## Стек технологий

1. Python
2. Django
3. Django Rest Framework
4. Swagger
5. PostgreSQL

Все библиотеки, которые использовались при создании, хранятся в файле requirements.txt

## API v1

* [GET /api/v1/submit-data/](#get-submit-data)
* [POST /api/v1/submit-data](#post-submit-data)
* [GET /api/v1/submit-data/{id}/](#get-submit-dataid)
* [PATCH /api/v1/submit-data/{id}/](#patch-submit-dataid)

### GET /submit-data/

Resource URL<br/>

```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/```

Parameters<br/>

|           Parameters            | Description |
|:-------------------------------:|:-----------:|
| user__email<br/><i>optional</i> |   String    |

Example Request
<br/>
<br/>
Request URL:
<br/>
<br/>
GET ```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/?user__email=user-email```
<br/>
<br/>
Response:

```json
{
  "status": 200,
  "data": []
}
```

### POST /submit-data/

Resource URL<br/>

```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/```

Parameters<br/>

|          Parameters          | Description |
|:----------------------------:|:-----------:|
| raw_data<br/><i>required</i> |    JSON     |
|  images<br/><i>required</i>  |    JSON     |

Example Request
<br/>
<br/>
Request URL:
<br/>
<br/>
POST ```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/```
<br/>
<br/>
Response:

```json
{
  "status": 200,
  "id": 1
}
```

### GET /submit-data/{id}/

Resource URL<br/>

```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/{id}/```

Parameters<br/>

|       Parameters       | Description |
|:----------------------:|:-----------:|
| id<br/><i>required</i> |     Int     |

Example Request
<br/>
<br/>
Request URL:
<br/>
<br/>
GET ```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/{id}/```
<br/>
<br/>
Response:

```json
{
  "id": 1,
  "date_added": "2024-01-31T17:12:54.001480+05:00",
  "raw_data": {
    "user": {
      "fam": "Фамилия",
      "otc": "Отчество",
      "name": "Имя",
      "email": "Адрес электронной почты",
      "phone": "Номер телефона"
    },
    "level": {
      "autumn": "1A",
      "spring": "",
      "summer": "1A",
      "winter": ""
    },
    "title": "Название",
    "coords": {
      "height": "height",
      "latitude": "latitude",
      "longitude": "longitude"
    },
    "connect": "connect",
    "add_time": "2024.01.31 12:09:00",
    "beautyTitle": "beautyTitle",
    "other_titles": "other_titles"
  },
  "images": [
    {
      "id": 1,
      "title": ""
    }
  ],
  "status": "new"
}
```

Bad response:

```json
{
  "status": 404,
  "message": "Не найдено"
}
```

### PATCH /submit-data/{id}/

Resource URL<br/>

```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/```

Parameters<br/>

|          Parameters          | Description |
|:----------------------------:|:-----------:|
| raw_data<br/><i>required</i> |    JSON     |
|  images<br/><i>required</i>  |    JSON     |

Example Request
<br/>
<br/>
Request URL:
<br/>
<br/>
PATCH ```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/```
<br/>
<br/>
Response:

```json
{
  "state": 1
}
```

Bad response:

```json
{
  "state": 0,
  "message": "Текст ошибки"
}
```