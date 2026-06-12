from django.db import models


class GeneralSetting(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=255, default='', blank=True)
    parameter = models.CharField(max_length=255, default='', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name