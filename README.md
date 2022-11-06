# SmartAidKit
RESTFul service with Django for effective tracking of drugs.

## Built With

- [Python](https://www.python.org/) 3.6.x
- [Django Rest Framework](http://www.django-rest-framework.org/) 3.8.x


## Features:
<li>Login/Register</li>
<li>Creation of First Aid Kit info</li>
<li>Effective management of drugs in aid kit based on their amount, expire date and type</li>
<li>Share Kit with other users</li>

## Installation

Create new directory:

```shell
$ mkdir SmartAidKit && cd SmartAidKit
```
Create new virtual environment:

```shell
$ python -m venv venv
```
Activate virtual environment:

```shell
$ source venv/bin/activate  (For Linux)
$ venv/Scripts/activate  (For Windows)
```
Clone this repository:

```shell
$ git clone git@github.com:cdoos/SmartAidKit.git && cd SmartAidKit/project
```
Install requirements:

```shell
$ pip install -r requirements.txt
```
Check for any project errors:

```shell
$ python manage.py check
```
Run Django migrations to create database tables:

```shell
$ python manage.py migrate
```
Run the development server:

```shell
$ python manage.py runserver
```
