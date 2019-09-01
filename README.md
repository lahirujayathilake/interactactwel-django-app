# Getting Started

First, setup the airavata-django-portal locally. See
https://github.com/apache/airavata-django-portal.

Then, activate the virtual environment for the airavata-django-portal:

```
cd ../airavata-django-portal
source venv/bin/activate
```

Then, change to the directory of this project and install this project as a
python package in the airavata-django-portal's virtual environment:

```
cd ../interactactwel-django-app/
pip install -r requirements.txt
python setup.py develop
```

Now build the Vue JS app

```
cd interactwel/
npm run build
```

Go back to the airavata-django-portal and start the server

```
cd /path/to/airavata-django-portal
python manage.py migrate
python manage.py runserver
```

The InterACTWEL Dashboard will be available at http://localhost:8000/interactwel/

## Run Vue js app in development mode

Go to interactwel/ directory

Run ```npm run serve``` to locally run the vue app

## Build Vue js app for production use

Run ```npm run build``` 

----
**Older instructions**

## To start the Django app

Go to interactwel directory

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

##Wagtail CMS
After running above commands, to create a superuser run,
```
./manage.py createsuperuser
```

Browse the admin panel using

```
localhost:8000/cms
```

Browse the web site using

```
localhost:8000/home
```

----


## REST API

Rest API is exposed in http://localhost:8000/api

#### Resources 

##### Subbasin: http://localhost:8000/api/subbasins

Get All
```
GET http://localhost:8000/api/subbasins/
```

Get one
```
GET http://localhost:8000/api/subbasins/1
```

Create 
```
POST http://localhost:8000/api/subbasins/

{
    "detail_json": <JSON COntent>
}
```
