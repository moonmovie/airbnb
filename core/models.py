from django.db import models

# Create your models here.


class TimeStampedmodel(models.Model):

    created = models.DateTimeField(auto_now_add=True)  # 모델이 생성된 날짜 구할 수 있음
    updated = models.DateTimeField(auto_now=True)  # 새로운 날짜로 업데이트

    class Meta:
        abstract = True  # no register to db

