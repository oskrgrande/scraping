# scraping

# backend

backend is a project in python is REST API with flask

## Installation

previamente necesitamos tener isntalado python en nuestro ordenador
luego instalar pip el manejador de paquetes de python

```
cd /backend
pip3 install flask virtualenv pymongo flask-pymongo newspapper3k
```

para optimizar la funcionalidad y tiempo de respuesta ya que el module de scrapign newspapper3k
retrasa el timepo de espuesta se recomienda
ejecutar primero la petición al endpoint
/api/v1/save-articles - GET - get 15 articles by url and save in database
ya que este guarda 15 registros en la base

## Endpoints

/api/v1/save-articles - GET - get 15 articles by url and save in database

/api/v1/users - get all users
/api/v1/create-user - POST - create and save an user
/api/v1/news - GET - get all news
/api/v1/filter - POST - filter and search in news articles by a string on send body
/api/v1/daily-new - GET - get a one article by source for a dailyarticle
/api/v1/new/<id> - GET - get a detail by article
/api/v1/best-author/ - GET - get a random autho from database on articles documents
/api/v1/users/<id> - GET - get a detail from a users
/api/v1/add-subs - POST - add email on emails subcribers on database.subcribers
/api/users/<id> - DELETE - delete a user

# frontend

## Project setup

```
cd /frontend
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```
