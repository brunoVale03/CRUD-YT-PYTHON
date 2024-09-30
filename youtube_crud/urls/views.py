from rest_framework import viewsets
from .models import YoutubeURL
from .serializers import YoutubeURLSerializer

class YoutubeURLViewSet(viewsets.ModelViewSet):
    queryset = YoutubeURL.objects.all()
    serializer_class = YoutubeURLSerializer
