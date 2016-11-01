### Get the Cyqlo web app running on your local machine

Make sure you have Python 3.5.2 installed. We use [Conda](http://conda.pydata.org/docs/index.html) to manage different Python environments. [Virtualenv](https://virtualenv.pypa.io/en/stable/) is another more lightweight option.

Retrieve our project
```
$ git clone https://github.com/johnplaydrums/cyqlo
$ cd cyqlo
```

Install dependencies in your environment
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
