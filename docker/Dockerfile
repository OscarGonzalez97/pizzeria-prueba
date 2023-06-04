FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

RUN mv pizzeria/local_settings_docker.py pizzeria/local_settings.py

RUN python manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "pizzeria.wsgi:application", "--bind", "0.0.0.0:5000"]
