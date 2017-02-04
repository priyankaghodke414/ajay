from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publioshed_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publioshed_date = timezone.now()
        self.save()

    def __str__(self):
            return self.title


