# pull official base image
FROM python:3.8.3-alpine

# set work directory
ENV APP=/app
RUN mkdir $APP
WORKDIR $APP

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    # install Pillow dependencies
    && apk add jpeg-dev zlib-dev libjpeg

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY config/docker/entrypoint.sh /app

# copy project
COPY . $APP

# run entrypoint.sh
ENTRYPOINT ["/app/docker/entrypoint.sh"]
