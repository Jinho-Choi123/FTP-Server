<br />
<br />
<br />
<p align="center">
    <a href="https://www.django-rest-framework.org/"><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" alt="Logo" height="150"><title>Django</title><path d="M11.146 0h3.924v18.166c-2.013.382-3.491.535-5.096.535-4.791 0-7.288-2.166-7.288-6.32 0-4.002 2.65-6.6 6.753-6.6.637 0 1.121.05 1.707.203zm0 9.143a3.894 3.894 0 00-1.325-.204c-1.988 0-3.134 1.223-3.134 3.365 0 2.09 1.096 3.236 3.109 3.236.433 0 .79-.025 1.35-.102V9.142zM21.314 6.06v9.098c0 3.134-.229 4.638-.917 5.937-.637 1.249-1.478 2.039-3.211 2.905l-3.644-1.733c1.733-.815 2.574-1.53 3.109-2.625.561-1.121.739-2.421.739-5.835V6.059h3.924zM17.39.021h3.924v4.026H17.39z" /></svg></a>
  
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

FTP Server helps **Users who needs to transfer large amount of data** without using physical drive or wired connection. While this service is open for public, **anyone who wants to transfer files** are able to upload and download files. Please feel free to use our service.


This Project is being maintained by [Ball](https://github.com/Jinho-Choi123)

We're expecting our users transfer their Large size videos or images. There is no strict restrictions on contents that users upload.

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
- [Deployment](#deployment)
- [Authors](#authors)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Prerequisites

**You’ll need to have Python 3.9.7 or local development and production machine**. You can use [docker](https://www.docker.com/) to easily switch Python versions between different projects.
Python. That's all you need.

```sh
$ python --version // 3.9.7
```
### sqlite3
For simple dev setup, we will use sqlite3 database. In official use, please [use other database](https://docs.djangoproject.com/en/3.2/topics/db/multi-db/) like [MongoDB](https://www.mongodb.com/), [MYSQL](https://www.mysql.com/), [Postgresql](https://www.postgresql.org/). 

## Getting Started

### Running Development Server
```
Since our default database is sqlite3, you don't need to install or start a database.
```

### pip

Run django-rest-framework dev server

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
│
├── .gitignore
└── manage.py  - Entry point
```


## Contributing

Please checkout [CONTRIBUTING.md](CONTRIBUTING.md) for more.


## Authors

* **Ball** - [Cookie](https://github.com/Jinho-Choi123)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
