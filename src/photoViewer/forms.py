from django import forms

from .models import PhotoUploader

class PhotoUploaderForm(forms.ModelForm):
    class Meta:
        model = PhotoUploader
       # fields = forms.ImageField
        fields = ["image"]