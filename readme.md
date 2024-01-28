# API ДЗ

API доступен в интернете по адресу ```https://djangoapitest.pythonanywhere.com/```
<br/>
Также документация была сделана через swagger, она доступна по
адресу ```https://djangoapitest.pythonanywhere.com/swagger```

## В чем заключается задача API

Задача API заключается в том, что через него будут производиться задачи в мобильном приложении такие, как создание
записи, ее редактирование, а
также получение конкретной записи по её id и изменение конкретной записи.

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
  "status": 200
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
  "date_added": "2024-01-28T13:14:02.784357+05:00",
  "raw_data": {
    "title": "title"
  },
  "images": [
    {
      "id": 1
    }
  ],
  "status": "new",
  "user_email": null
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
  "status": 200
}
```

### GET /submit-data/{id}/

Resource URL<br/>

```https://djangoapitest.pythonanywhere.com/api/v1/submit-data/{id}/```

Parameters<br/>

|        Parameters        | Description |
|:------------------------:|:-----------:|
| data<br/><i>required</i> |    JSON     |
|  id<br/><i>required</i>  |     Int     |

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
  "date_added": "2024-01-28T13:14:02.784357+05:00",
  "raw_data": {
    "title": "title"
  },
  "images": [
    {
      "id": 1
    }
  ],
  "status": "new",
  "user_email": null
}
```
