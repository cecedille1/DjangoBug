from django.db import models


class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().defer('an_expensive_value')


class MyModel(models.Model):
    objects = MyManager()

    value = models.CharField(
        max_length=64,
    )
    an_expensive_value = models.BinaryField()
