web: gunicorn config.wsgi:application
worker: celery worker --app=fb_wall.taskapp --loglevel=info
