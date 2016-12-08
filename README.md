# Cyqlo - Exploring NYC and beyond on a bike

## Development setup

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

Install Postgres locally. We recommend [Postgres.app](http://postgresapp.com/)
for mac. Make sure to set the `$PATH` variable as described in the instructions.
Connect to Postgres via the command line to create a database and user
```
$ psql postgres
$ CREATE DATABASE cyqlo;
$ CREATE USER cyqlo WITH PASSWORD 'yourpassword';
$ GRANT ALL PRIVILEGES ON DATABASE cyqlo TO cyqlo;
```

We will store passwords and sensitive information in our `main/settings.py` file.
Because of this, we do not want to check in our settings.py file into git.
We use a template for the settings file, `/main/settings_example.py`. Copy this file
to `/main/settings.py` and change the database info to match your database name, user, and password.

Make and run [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/)
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create Django superuser so you can access the admin portal
```
$ python manage.py createsuperuser
```

Start server
```
$ python manage.py runserver
```

## Development Workflow

### Tests & pull requests

Any well built app needs to have an expansive testing suite. When you create a pull request, there should one of the following included in the code or documentation of the PR:
 - a specific test for the code you wrote
 - an explanation of what tests already cover your code
 - an explanation of why your code might not need tests

Any code you write and submit in a PR should pass all the tests in Cyqlo's testing suite.

To run Cyqlo's existing tests:
```
$ python manage.py test main.tests
```
To better gauge our overall coverage of testing, it is no surprise that Coverage.py is of use.
```
$ pip install coverage
```
To check for Cyqlo's test coverage simply run:
```
$ coverage run manage.py test main.tests
```

### Pylint

Pylint is code analysis for Python. Along with syntax checking, Pylint checks that your code is well formatted, free of duplicated or unused lines, and generally conforms to PEP 8 guidelines. Cyqlo strives to have a perfect Pylint score (10/10). Any PR you submit should, at the very least, not degrade the current Pylint score of the master branch. If you notice the score has dipped below 10 (before your PR), reach out to others to understand why that's the case.
Run Pylint on our main app:
```
$ pylint main
```
