## Running

1. Create `.env` file

```shell
$ cp .env.example .env
```
2. Edit `.env` to match your system criteria

```shell
$ docker-compose up -d
$ docker-compose exec web ./manage.py migrate
$ docker-compose exec web ./manage.py createsuperuser
```