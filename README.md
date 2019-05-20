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

## REST API

Rest API is exposed in http://localhost/api

#### Resources 

##### Subbasin: http://localhost/api/subbasins

Get All
```
GET http://localhost/api/subbasins/
```

Get one
```
GET http://localhost/api/subbasins/1
```

Create 
```
POST http://localhost/api/subbasins/

{
    "detail_json": <JSON COntent>
}
```