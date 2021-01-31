# Moat-API-server

Moat-API를 Docker & Github Action으로 배포

# 환경

- docker
- docker-compose
- nginx
- gunicorn
- postgres
- python 3.8
- django 3.1

# 배포 전 기억할 사항

- pipenv를 사용했기 때문에 pipenv lock --requirements > requirements.txt 명령어로 생성

# Reference

도커 배포 : https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ \

pipenv로 Docker build 관리 : https://pythonspeed.com/articles/pipenv-docker/ \
