from django.shortcuts import render
from django.http import HttpResponse

from .models import MediaFile
from .forms import MediaUploadForm
import os
from django.conf import settings
# Create your views here.


def home(request):
    # Gets latest file (if anyone exists)
    media = MediaFile.objects.last()  

    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Delete existing files
            for old in MediaFile.objects.all():
                file_path = os.path.join(settings.MEDIA_ROOT, str(old.file))
                if os.path.exists(file_path):
                    os.remove(file_path)
                old.delete()

            # Create new media file
            new_media = form.save(commit=False)
            filename = str(new_media.file.name).lower()

            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                new_media.type = 'image'
            elif filename.endswith(('.mp3', '.wav', '.ogg')):
                new_media.type = 'audio'
            elif filename.endswith(('.mp4', '.webm', '.mov')):
                new_media.type = 'video'
            else:
                new_media.type = 'image'  # default fallback

            new_media.save()
            media = new_media  # update the latest media

    else:
        form = MediaUploadForm()

    return render(request, 'media_app/media_page.html', {'form': form, 'media': media})