# Cyqlo

## Development Setup

```
# Setup virtual environment (install virtualenv first)
$ virtualenv cyqlo_env
$ cd cyqlo_env

# start virtual enviornment
$ source bin/activate

# install dependencies in your evniorment
$ pip install -r requirments.txt

# Now let's retrieve our project and get it running
$ git clone https://github.com/johnplaydrums/cyqlo
$ cd cyqlo
# make and run [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/)
$ python manage.py makemigrations
$ python manage.py migrate
# start server
$ python manage.py runserver

