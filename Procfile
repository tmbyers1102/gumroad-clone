release: python3 manage.py migrate
release: export DJANGO_READ_DOT_ENV_FILE=True
web: gunicorn config.wsgi --log-file -