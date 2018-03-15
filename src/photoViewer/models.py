# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PhotoUploader(models.Model):
    title = models.CharField(max_length =120)
    image = models.ImageField()
