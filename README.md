# Cyqlo

## Development Setup

Setup virtual environment (install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) first)
```
# Create enviornment directory
$ virtualenv cyqlo_env
$ cd cyqlo_env

# start virtual enviornment
$ source bin/activate
```

Retrieve our project and get it running
```
$ git clone https://github.com/johnplaydrums/cyqlo
$ cd cyqlo
```

Install dependencies in your evniorment
```
$ pip install -r requirements.txt
```

Make and run [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/)
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Start server
```
$ python manage.py runserver
```
