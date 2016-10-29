from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Provider(models.Model):
    provider = models.CharField(max_length=30)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.provider


class Service(models.Model):
    type = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    def __unicode__(self):
        return self.name


class Feature(models.Model):
    feature = models.CharField(max_length=30)

    class Meta:
        unique_together=('feature','id')

    def __unicode__(self):
        return self.feature


class ProviderService(models.Model):
    provider = models.ForeignKey(Provider)
    service = models.ForeignKey(Service)

    def __unicode__(self):
        return self.value


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service)
    feature = models.ForeignKey(Feature)


class BenchMark(models.Model):
    provider = models.ForeignKey(Provider)
    service = models.ForeignKey(Service)
    feature = models.ForeignKey(Feature)
    thirdparty_rating=models.IntegerField()


class UserFeedback(models.Model):
    provider = models.ForeignKey(Provider)
    service = models.ForeignKey(Service)
    feature = models.ForeignKey(Feature)
    user_rating = models.IntegerField()


