from rest_framework import serializers
from .models import YoutubeURL

class YoutubeURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeURL
        fields = '__all__'
