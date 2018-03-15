# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse

from .forms import PhotoUploaderForm
from .models import PhotoUploader


#Open user uploaded file and displays it on page
def home(request):
    title = "Upload your photo"
    form = PhotoUploaderForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        print request.POST
        if form.is_valid():
            print request
            instance = form.save(commit=False)
            instance.save()
        instance = PhotoUploader.objects.get(id=instance.id)
        image_full_path = instance.image.path
        image_data = open(image_full_path, "rb").read()
        return HttpResponse(image_data, content_type="image/jpg")
    context = {
    "title" : title,
    "form" : form
    }
    return render(request, "home.html",context)
