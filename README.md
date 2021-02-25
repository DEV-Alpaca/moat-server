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
- [ ] Change Password
- [x] Update Profile
- [ ] Add Club to Favourites
- [x] Register (Create User)
- [x] Login (JWT)
- [ ] JWT Authentication
- [x] Login with Mobile Number
- [ ] SMS sending Mobile Number Authentication
- [ ] SMS sending feature upon successful registration

### Reservation API Actions
- [ ] Add Club to Reservations List of the User

### List API Actions
- [ ]

### Review API Actions
- [ ]

### Later... User API Actions
- [ ] Mail sending feature upon successful registration
- [ ] Social Auth Endpoints(Login using fb/google)
- [ ] REST API to login with OTP (Same API endpoint as for OTP Verification; Set `is_login: true` while sending JSON request)
- [ ] Signal based mails
- [ ] Generic Configuration based on settings.py
- [ ] Mail based activation (optional alternative for OTP based activation)

# Reference

git-hook / pre-commit.yaml 작성 : https://pre-commit.com/index.html
도커 배포 : https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
user 참고 : https://github.com/101Loop/drf-user
django-environ docs : https://django-environ.readthedocs.io/en/latest/
