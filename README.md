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

## API Actions

### User API Actions

- [ ] Mobile Number
- [ ] Single field for full name
- [ ] REST API to register
- [ ] REST API to login
- [ ] MultiModelBackend: User can login using either of mobile, email or
      username
- [ ] REST API to login with OTP (Same API endpoint as for OTP Verification; Set
      `is_login: true` while sending JSON request)
- [ ] OTP Verification for mobile and email
- [ ] API to register / login with OTP (no pre-registration required)
- [ ] API to set user's profile image
- [ ] Mail sending feature upon successful registration
- [ ] SMS sending feature upon successful registration
- [ ] Change Password
- [ ] Update Profile
- [ ] Generic Configuration based on settings.py
- [ ] Signal based mails
- [ ] Mail based activation (optional alternative for OTP based activation)
- [ ] Social Auth Endpoints(Login using fb/google)

# Reference

도커 배포 : https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
user 참고 : https://github.com/101Loop/drf-user
