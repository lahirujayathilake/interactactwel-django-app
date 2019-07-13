## Run Vue js app in development mode

Go to interactwel/dashboard directory

Run ```npm run serve``` to locally run the vue app

## Build Vue js app for production use

Run ```npm run build``` 

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
Afer running above commands, to create a superuser run,
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