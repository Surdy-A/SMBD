"""imdb URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie.views import HomeView, MostWatched

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('movies/', include('movie.urls', namespace='movies')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

