from django import forms
from .models import MediaFile


class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'file']