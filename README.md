# dailyrippl

throwing smooth washed pebbles / as far as I can

## dev setup

in a separate directory
```
git clone https://github.com/unitedstates/congress-legislators
```

prereqs
```
brew install yarn
brew install pyenv-virtualenvwrapper
mkvirtualenv rippl -p python3.5
```

database setup
```
brew install postgresql
brew services start postgresql
psql -U postgres -h localhost -f scripts/db_setup.sql
```

in here
```
pip install -r requirements.txt
python rippl/manage.py migrate
python rippl/manage.py createsuperuser
python rippl/manage.py import_reps <path to legislators-current.yaml>
python rippl/manage.py import_bills --start_date "2016-12-01"

yarn install
brunch build # can use brunch watch for live reloading

python rippl/manage.py runserver
```

## running tests

```
tox
```

## architecture

Probably something like this

![architecture](architecture.jpg)

[Django for web](https://docs.djangoproject.com)

[Deepstream for realtime](https://deepstream.io)

[PostgreSQL for DB](https://www.postgresql.org/)
