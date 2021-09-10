<br />
<br />
<br />
<p align="center">
    <a href="https://www.django-rest-framework.org/"><img src="https://drfrakib.files.wordpress.com/2017/11/rest-logo.png" /></a>
  
  <p align="center">
    <img src="https://img.shields.io/badge/license-MIT-black.svg" />
    <img src="https://img.shields.io/badge/python-v3.9.7-orange.svg" />
    <img src="https://img.shields.io/badge/django-v3.4.1-blue.svg">
    <img src="https://img.shields.io/badge/DRF-v3.12.4-red.svg">
  </p>
  
  <p align="center">
    File Transfer Server with Python, designed and developed by Ball
    <br />
    <a href="https://github.com/Jinho-Choi123?tab=repositories">Look more for Ball's Project</a>
  </p>
</p>


# About

FTP Server helps **User who needs to transfer large amount of data** without using physical drive or wired connection. While this service is open for public, **anyone who wants to transfer files** is able to upload and download. Please feel free to use our service.


This Project is being maintained by [Ball](https://github.com/Jinho-Choi123)

We're expecting our users to transfer their Large size videos or images. There is no strict restrictions on contents that users upload.

Please contact us to get more detailed information.

If you're looking for frontend codes, you can find it in [here](https://github.com/Jinho-Choi123/FTP-Frontend)

# Previews

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
    - [Running Development Server](#running-development-server)
        - [Using pip](#pip)
- [Proxy API Requests](#proxy-api-requests)
- [Authentication](#authentication)
- [Built With](#built-with)
- [Folder Structure](#folder-structure)
- [Authors](#authors)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

**You’ll need to have Python 3.9.7 on local development or production machine**. You can use [docker](https://www.docker.com/) to easily set dev environment.
Python. That's all you need.

```sh
$ python --version // 3.9.7
```
### sqlite3
For simple dev setup, we will use sqlite3 database. In official use, please [use other database](https://docs.djangoproject.com/en/3.2/topics/db/multi-db/) like [MongoDB](https://www.mongodb.com/), [MySQL](https://www.mysql.com/) or [Postgresql](https://www.postgresql.org/). 

## Getting Started

### Running Development Server
```
Since our default database is sqlite3, you don't need to install or start a database.
```

### pip

Run dev server

```sh
$ pip install -r requirements.txt //Installing dependencies with pip
$ python manage.py makemigrations //migration is required
$ python manage.py migrate 
$ python manage.py runserver
// Follow the instructions on terminal
```

## Proxy API Requests

Using http-proxy-middleware, all requests are proxied to localhost:8000 on which our API server is located.

## Authentication

For unsophisticated use of service, we don't have any authentication system. However, to secure user's file, [only allow request from frontend server's ip address](https://www.django-rest-framework.org/api-guide/permissions/).

## Built with

* [UUID](https://docs.python.org/3/library/uuid.html)

## Folder Structure
```
FTP-Server
├── README.md
├── LICENSE
├── checkserver
├── filedownload
├── fileupload
├── ftp_server
│   ├── _pycach_
│   ├── __init__.py
│   ├── setting.py - Contains Project Settings
│   ├── asgi.py
│   ├── urls.py - Contains Routing info
│   └── wsgi.py
├── ResetMigration.sh - reset db and migrations. run the server
├── .gitignore
└── manage.py  - Entry point
```


## Contributing

Please checkout [CONTRIBUTING.md](CONTRIBUTING.md) for more.


## Authors

* **Ball** - [Cookie](https://github.com/Jinho-Choi123)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
