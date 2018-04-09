from django.db import models
from django.contrib.auth.models import User

class kharj(models.Model):
    sharh = models.CharField(max_length=255)
    date = models.DateTimeField()
    mablagh = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):   #dar python 2.X => def __unicode__(self):
        return "{}---{}".format(self.date,self.mablagh)
        #return (self.sharh)


class daramad(models.Model):
    sharh = models.CharField(max_length=255)
    date = models.DateTimeField()
    mablagh = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{}---{}".format(self.date,self.mablagh)
