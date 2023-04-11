from django.db import models


class RequestCounterModel(models.Model):
    counter = models.IntegerField(default=0)