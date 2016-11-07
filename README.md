# Cyqlo - Explore NYC on a bike

### Development setup

Make sure you have Python 3.5.2 installed. We use [Conda](http://conda.pydata.org/docs/index.html) to manage different Python environments. [Virtualenv](https://virtualenv.pypa.io/en/stable/) is another more lightweight option.

Retrieve our project
```
$ git clone https://github.com/johnplaydrums/cyqlo
$ cd cyqlo
```

Install Postgres locally. We recommend Postgres.app(http://postgresapp.com/)
for mac. Make sure to set the `$PATH` variable as described in the instructions.
Connect to Postgres via the command line to create a database and user
```
$ psql postgres
$ CREATE DATABASE cyqlo
$ CREATE USER cyqlo WITH PASSWORD 'yourpassword'
$ GRANT ALL PRIVILEGES ON DATEBASE cyqlo TO cyqlo;
```
Copy `/main/settings_example.py` to `/main/settings.py` and change the database info
to match your database name, user, and password.

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
