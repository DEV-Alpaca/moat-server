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

# API Actions

### Club API Actions

- [x] List Clubs
- [x] See Club
- [x] Create Clubs
- [x] Delete Club
- [x] Update Club
- [ ] Search Clubs

### User API Actions
- [x] Single field for full name
- [x] See Profile
- [x] Change Password
- [x] Update Profile
- [x] Register (Create User)
- [x] Login (JWT)
- [x] JWT Authentication
- [x] Login with Mobile Number
- [x] SMS sending Mobile Number Authentication
- [ ] SMS sending feature upon successful registration

### Reservation API Actions
- [ ] Add Club to Reservations List of the User

### List API Actions
- [ ]

### Review API Actions
- [ ]

### Later... User API Actions
- [ ] Add Club to Favourites
- [ ] Mail sending feature upon successful registration
- [ ] Social Auth Endpoints(Login using fb/google)
- [ ] REST API to login with OTP (Same API endpoint as for OTP Verification; Set `is_login: true` while sending JSON request)
- [ ] Signal based mails
- [ ] Generic Configuration based on settings.py
- [ ] Mail based activation (optional alternative for OTP based activation)

# TEST
### Commands for Making Test Instance
- [x] Make `python manage.py seed_town` command
- [x] Make `python manage.py seed_area` command
- [x] Make `python manage.py seed_address` command
- [x] Make `python manage.py seed_clubtype` command
- [x] Make `python manage.py seed_user` command
- [x] Make `python manage.py seed_club` command
- [ ] Add func to add automatically `club_photos` in seed_club command

# Deploy
1. Github Action 설정 확인 (.github/workflows/deploy.yml)
2. Github Secrets에 필요한 값 설정
    - DEPLOY_USERNAME:
    - ENV: `.env` file 에 들어갈 key-value 값 전체
    - ENV_PROD: `.env.prod` file 에 들어갈 key-value 값 전체
    - ENV_PROXY: `.env.prod.proxy-companion` file 에 들어갈 key-value 값 전체
    - HOST: 배포할 remote 서버 host
    - USERNAME: 배포할 remote 서버의 username _ex) ubuntu_
    - KEY: 배포할 remote 서버로 접근 가능한 ssh key 전문

- 소스는 ec2 ubuntu 기준 /home/{DEPLOY_USERNAME}/srv/django-docker로 배포됩니다


# Reference

git-hook / pre-commit.yaml 작성 : https://pre-commit.com/index.html  \
도커 배포 : https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/  \
도커 nginx-proxy : https://testdriven.io/blog/django-lets-encrypt/  \
user 참고 : https://github.com/101Loop/drf-user  \
django-environ docs : https://django-environ.readthedocs.io/en/latest/  \
Naver SMS Authentication : https://yuda.dev/284  \
https://github.com/marketplace/actions/rsync-deployments-action \
https://zzsza.github.io/development/2020/06/06/github-action/  \
