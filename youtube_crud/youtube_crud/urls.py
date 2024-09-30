from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from urls.views import YoutubeURLViewSet

router = DefaultRouter()
router.register(r'urls', YoutubeURLViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
