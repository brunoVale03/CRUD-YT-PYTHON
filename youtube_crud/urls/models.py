from django.db import models

class YoutubeURL(models.Model):
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
