# dailyrippl

throwing smooth washed pebbles / as far as I can

## dev setup

```
pip install -r requirements.txt
python rippl/manage.py migrate
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
