from django.db import models

from django.contrib.auth.models import User
class kharj(models.Model):
    sharh = models.CharField(max_length=255)
    date = models.DateTimeField()
    mablagh = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
