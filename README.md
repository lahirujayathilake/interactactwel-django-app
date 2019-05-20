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
python manage.py migrate
python manage.py runserver
```