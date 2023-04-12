from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class CommonInfo(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(default=now)
    class Meta:
        abstract = True

class Movie(CommonInfo):
    title = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=512, blank=True)
    uuid = models.UUIDField()

class Collection(CommonInfo):
    title = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    movie = models.ManyToManyField(Movie)
    uuid = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)