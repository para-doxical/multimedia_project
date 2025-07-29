from django.db import models

# Create your models here.

class MediaFile(models.Model):
    """A media file can be an image file, an audio file or a video file."""
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='') # This will upload to MULTIMEDIA_PROJECT/media
    file_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def __repr__(self):
    #     return self.title
    def __str__(self):
        return self.title