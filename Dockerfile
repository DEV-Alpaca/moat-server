# pull official base image
FROM python:3.8.3-alpine

# set work directory
RUN mkdir /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev py3-psycopg2

# install dependencies
RUN pip install --upgrade pip
#RUN pip install pipenv
#COPY Pipfile* /
#RUN cd /app && pipenv lock --keep-outdated --requirements > requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /app

# copy project
COPY . /app/

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]