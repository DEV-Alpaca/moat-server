import base64
import datetime
import hashlib
import hmac
import time
from random import randint

import requests
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedModel


class User(AbstractUser):

    """ User Model Definition """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    username = models.CharField(_("username"), max_length=64, blank=True)
    superhost = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(verbose_name="휴대폰 번호", max_length=11, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

    USERNAME_FIELD = "phone_number"  # 로그인 phone_number 로
    REQUIRED_FIELDS = ["username", "birthday", "gender"]

    def __str__(self):
        return self.username


class AuthSms(TimeStampedModel):
    phone_number = models.CharField(
        verbose_name="휴대폰 번호", primary_key=True, max_length=50
    )
    auth_number = models.IntegerField(verbose_name="인증 번호")

    class Meta:
        db_table = "auth_sms"

    def save(self, *args, **kwargs):
        self.auth_number = randint(1000, 10000)
        super().save(*args, **kwargs)
        self.send_sms()  # 인증번호가 담긴 SMS 를 전송

    def send_sms(self):
        service_id = settings.SERVICE_ID
        url = "https://sens.apigw.ntruss.com"
        uri = "/sms/v2/services/" + service_id + "/messages"
        api_url = url + uri

        body = {
            "type": "SMS",
            "contentType": "COMM",
            "from": settings.SMS_SEND_PHONE_NUMBER,
            "content": f"[테스트] 인증 번호 [{self.auth_number}]를 입력해주세요.",
            "messages": [{"to": self.phone_number}],
        }

        time_stamp = str(int(time.time() * 1000))
        access_key = settings.SUB_ACCOUNT_ACCESS_KEY
        string_to_sign = "POST " + uri + "\n" + time_stamp + "\n" + access_key
        signature = self.make_signature(string_to_sign)

        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-ncp-apigw-timestamp": time_stamp,
            "x-ncp-iam-access-key": access_key,
            "x-ncp-apigw-signature-v2": signature,
        }

        requests.post(api_url, headers=headers, json=body)

    def make_signature(self, string):
        secret_key = bytes(settings.SMS_SERVICE_SECRET, "UTF-8")
        string = bytes(string, "UTF-8")
        string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
        string_base64 = base64.b64encode(string_hmac).decode("UTF-8")
        return string_base64

    @classmethod
    def check_auth_number(cls, p_num, c_num):
        time_limit = timezone.now() - datetime.timedelta(minutes=5)
        result = cls.objects.filter(
            phone_number=p_num, auth_number=c_num, modified__gte=time_limit
        )
        if result:
            return True
        return False
