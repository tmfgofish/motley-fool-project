from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('article/', include('articles.urls')),
    path('comments/', include('comments.urls')), 
]
